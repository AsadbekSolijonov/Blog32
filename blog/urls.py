from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('not_published/', views.home_out, name='home_out'),
    path('create/', views.create, name='create'),
    path('<int:blog_id>/detail', views.detail, name='detail'),
    path('<int:blog_id>/update', views.update, name='update'),
    path('<int:blog_id>/delete', views.delete, name='delete'),
]
