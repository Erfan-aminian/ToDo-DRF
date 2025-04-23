from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token_views

app_name = 'accounts'
urlpatterns = [
    path('api-token-auth/', auth_token_views.obtain_auth_token),

]