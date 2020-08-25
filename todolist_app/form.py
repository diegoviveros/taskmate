# se importan los formularios de django
from django import forms
# se importa el modelo de la base de datos TaskLit
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']
