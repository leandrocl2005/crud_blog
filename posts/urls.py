from django.urls import path
from .views import post_list, post_create
from .views import post_delete_list, post_delete, post_edit_list, post_edit, list_post

urlpatterns = [
    path('list', post_list, name='post_list'),
    path('create',post_create,name='post_create'),
    path('delete_list/',post_delete_list,name='post_delete_list'),
    path('delete/<int:id>',post_delete,name='post_delete'),
    path('edit_list/',post_edit_list,name='post_edit_list'),
    path('edit/<int:id>',post_edit,name='post_edit'),
    path('list/<int:id>',list_post, name='list_post'),
]