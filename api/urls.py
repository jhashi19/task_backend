from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView, UserCreateView


urlpatterns = [
    path('accounts/create/', UserCreateView.as_view(), name='user_create'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/list/', TaskListView.as_view(), name='task_list'),
    path(
        'tasks/detail/<uuid:pk>/',
        TaskDetailView.as_view(),
        name='task_detail'),
]
