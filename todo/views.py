from django import views
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewTaskForm
from .models import Task, Category
from django.core import serializers
import json
from random import randint


class Index(views.View):
    def get(self, request):
        return render(request, 'index.html')


class TaskListView(ListView):
    model = Task
    ordering = 'set_to_time'

    def post(self, request):
        JsonSerializer = serializers.get_serializer("json")
        json_serializer = JsonSerializer()
        with open(f'{randint(11111, 99999)}.json', mode='w') as file:
            json_serializer.serialize(super(TaskListView, self).get_queryset(), stream=file)

        return redirect(reverse('tasks_list'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView,self).get_context_data()
        context['tasks_count'] = len(self.get_queryset())
        return context


class TaskDetailView(DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data()
        context['priority'] = dict(Task.PRIORITY_CHOICES)
        return context


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tasks_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks_list')


class CategoryView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.annotate(num_tasks=Count('tasks')).filter(num_tasks__gt=0)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data()
        context['empty_category'] = Category.emptyCategory.all()
        return context


class CategorizedTaskListView(ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(category__pk=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategorizedTaskListView, self).get_context_data()
        context['from_category'] = True
        context['from_category_count'] = len(self.get_queryset())
        return context

    def post(self, request, pk):
        JsonSerializer = serializers.get_serializer("json")
        json_serializer = JsonSerializer()
        with open(f'{randint(11111, 99999)}.json', mode='w') as file:
            json_serializer.serialize(self.get_queryset(), stream=file)
        return redirect(Category.objects.get(pk=pk).get_absolute_url())


class NewTaskView(views.View):
    def get(self, request):
        new_task_form = NewTaskForm()
        return render(request, 'todo/add_new_task.html', {'form': new_task_form})

    def post(self, request):
        new_task_form = NewTaskForm(request.POST)
        if new_task_form.is_valid():
            new_task_form.save()
        else:
            return render(request, 'todo/add_new_task.html',
                          {'form': NewTaskForm(), 'errors': new_task_form.errors})
        return redirect(reverse('tasks_list'))


class NewCategoryView(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('index')


class ExpiredTasksView(ListView):
    model = Task

    def get_queryset(self):
        return Task.expiredTasks.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ExpiredTasksView, self).get_context_data()
        context['expired_tasks'] = True
        context['expired_tasks_count'] = len(self.get_queryset())
        return context

    def post(self, request):
        JsonSerializer = serializers.get_serializer("json")
        json_serializer = JsonSerializer()
        with open(f'{randint(11111, 99999)}.json', mode='w') as file:
            json_serializer.serialize(self.get_queryset(), stream=file)
        return redirect('expired_tasks')
