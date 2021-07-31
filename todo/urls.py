from django.urls import path

from todo.views import TaskListView, TaskDetailView, \
    CategoryView, CategorizedTaskListView, Index, NewTaskView, \
    ExpiredTasksView, NewCategoryView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tasks/', TaskListView.as_view(), name='tasks_list'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('add_new_task/', NewTaskView.as_view(), name="add_task"),
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('category/<int:pk>', CategorizedTaskListView.as_view(), name='category_tasks'),
    path('add_new_category/', NewCategoryView.as_view(), name="add_category"),
    path('expired_tasks/', ExpiredTasksView.as_view(), name='expired_tasks')
]
