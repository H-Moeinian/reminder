from django import forms
from .models import Task
from django.contrib.admin import widgets


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        # widgets = {
        #     'set_to_time': widgets.AdminSplitDateTime(),
        # }



