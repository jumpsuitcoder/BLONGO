from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class CreatePostTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='root')
        self.client.login(username='admin', password='root')
        
    def test_create_post(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'author': self.user
        })
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.filter(title='Test Post').first()
        self.assertEqual(post.content, 'This is a test post content.')
        self.assertEqual(post.author, self.user)


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='root')
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')
        self.assertContains(response, self.user.username)

class AddCommentToPostTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='root')
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_add_comment_to_post(self):
        response = self.client.post(reverse('main:add_comment_to_post', kwargs={'post_id': self.post.pk}), {
            'author': self.user.pk,
            'text': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.get(post=self.post)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.text, 'This is a test comment.')
        response = self.client.get(reverse('main:post_detail', kwargs={'pk': self.post.pk}))
        self.assertContains(response, 'This is a test comment.')
