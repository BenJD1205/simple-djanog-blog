from django.urls import path
from . import views

urlpatterns = [
    path('blog/',views.index,name='blog-index'),
    path('blog_detail/<int:pk>/',views.blog_detail,name='blog-detail'),
    path('blog_edit/<int:pk>/',views.blog_edit,name='blog-edit'),
    path('blog_delete/<int:pk>/',views.blog_delete,name='blog-delete'),
]
