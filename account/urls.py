from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_views


urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='account/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='account/logout.html'),
         name='logout'),
    path('register/', account_views.register, name='register'),
    path('profile/', account_views.profile, name='profile'),
    path('change-profile/', account_views.change_profile, name='change_profile')
]