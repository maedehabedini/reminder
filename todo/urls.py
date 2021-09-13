from django.urls import path
from .views import TaskCreateView, TaskListView, TaskDetailView,CategoryListView,CategoryCreateView,CategorizedTaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/new', TaskCreateView.as_view(), name='new_task'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/new', CategoryCreateView.as_view(), name='new_category'),
    path('categories/<int:pk>', CategorizedTaskListView.as_view(), name='category_tasks'),

]
