from django.urls import path

from django.contrib.auth import views as auth_views

from .views import *

app_name = 'main_app'

urlpatterns = [
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('welcome/', welcome, name='welcome'),

    # Auth
    # path("login/", auth_views.LoginView.as_view(template_name="main_app/login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(template_name="main_app/login.html", next_page="login"), name="logout"),

    path('login/', auth_views.LoginView.as_view(template_name='main_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('register/', register, name='register'),

]
