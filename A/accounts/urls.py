from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token_views

app_name = 'accounts'
urlpatterns = [
    path('token/', auth_token_views.obtain_auth_token),
    path('register/', views.UserRegisterView.as_view(), name='register'),
]