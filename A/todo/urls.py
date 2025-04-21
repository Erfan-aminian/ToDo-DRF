from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('get/', views.TodoView.as_view(), name='get_todo'),
    path('get/<int:pk>/', views.TodoView.as_view(), name='get_update')

]