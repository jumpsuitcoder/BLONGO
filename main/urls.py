from django.urls import path
from .views import post_list, post_detail, post_new, post_edit, add_comment_to_post

app_name = 'main'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('new/', post_new, name='post_new'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
    path('posts/<int:post_id>/comment/', add_comment_to_post, name='add_comment_to_post'),
]
