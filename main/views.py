from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Post, Comment
import traceback
from .forms import PostForm, CommentForm

def post_list(request):
    try:
        posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
        return render(request, 'main/post_list.html', {'posts': posts})
    except:
        traceback.print_exc()

def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.filter(approved_comment=True)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
                messages.success(request, 'Your comment has been submitted and is awaiting approval.')
                return redirect('main:post_detail', pk=post.pk)
        else:
            comment_form = CommentForm()
        return render(request, 'main/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
    except:
        traceback.print_exc()

@login_required
def post_new(request):
    try:
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                new_post = post_form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                messages.success(request, 'Your post has been created.')
                return redirect('main:post_detail', pk=new_post.pk)
        else:
            post_form = PostForm()
        return render(request, 'main/form_new.html', {'form_new': post_form, 'form_title': 'New Post' })
    except:
        traceback.print_exc()

@login_required
def post_edit(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        form_title = ''
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                updated_post = post_form.save()
                messages.success(request, 'Your post has been updated.')
                return redirect('main:post_detail', pk=updated_post.pk)
        else:
            post_form = PostForm(instance=post)
            form_title = f"Edit: {post_form.initial['title']}"
        return render(request, 'main/form_edit.html', {'form_edit': post_form, 'form_title': form_title})
    except:
        traceback.print_exc()


@login_required
def add_comment_to_post(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, 'Your comment was added successfully!')
                return redirect('main:post_detail', pk=post.id)
        else:
            form = CommentForm()
        return render(request, 'main/add_comment_to_post.html', {'post': post, 'form': form})
    except:
        traceback.print_exc()
