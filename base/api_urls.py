from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, DeleteView

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', DeleteView.as_view(), name='task-delete'),
]
