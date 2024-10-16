from django.urls import path
from .views import get_users, create_user, user_detail
from .views import get_tasks, create_task, task_detail

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),
    path('tasks/', get_tasks, name='get_tasks'),
    path('tasks/create', create_task, name='create_task'),
    path('tasks/<int:pk>', task_detail, name='task_detail'),
]