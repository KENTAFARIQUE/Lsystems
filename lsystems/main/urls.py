from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('create', views.create_view, name='create'),
    path('gallery', views.gallery_view, name='gallery'),
    path('mygallery', views.my_gallery_view, name='mygallery'),
    path('delete/<int:pk>/', views.delete_image, name='delete_image'),
]
