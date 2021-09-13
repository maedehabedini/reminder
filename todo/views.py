from .models import *
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import reverse


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    queryset = Task.objects.filter(is_done=False)


class TaskCreateView(CreateView):
    model = Task
    template_name = 'todo/new_task.html'
    fields = ['title', 'description', 'due_date', 'categories']

    def get_success_url(self):
        return reverse('task_list')


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'todo/new_category.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('category_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'todo/category_list.html'
    queryset = Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['empty'] = Category.empty_category.all()
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class CategorizedTaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(categories__pk=self.kwargs['pk'])
