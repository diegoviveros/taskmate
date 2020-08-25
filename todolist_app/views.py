from django.shortcuts import render, redirect
from django.http import HttpResponse
# importar el modelo para traer los datos de la base de datos
from todolist_app.models import TaskList
# importar el formulario creado
from todolist_app.form import TaskForm
# importar mensajero de django
from django.contrib import messages
# pagination class
from django.core.paginator import Paginator
# se usan los decoradores para evitar acceso a personas no autenticadas
from django.contrib.auth.decorators import login_required


# Create your views here.
########################################################################################

# docorador de restriccion | login_required
@login_required
def todolist(request):
    # verificar el origen del metodo POST o GET
    if request.method == "POST":
        # se crea una variable form, recibe los datos del POST
        form = TaskForm(request.POST or None)
        # si es valido el formato, graba en la base de datos
        if form.is_valid():
            # se crea una instancia para retrazar el gradao a la base 
            instance = form.save(commit=False)
            # obteniendo asi el usuario actual con request. user, para poder insertar el id manage al commit
            instance.manage = request.user
            # luego se almacena normalmente
            instance.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        # preparado para paginador
        # all_task = TaskList.objects.all() --- trae todos los registros en total
        all_task = TaskList.objects.filter(manage=request.user)
        # paginado por 5 elementos
        paginator = Paginator(all_task, 8)
        # variable de paginador por get con nombre pg
        page = request.GET.get('pg')
        # seccionado de elementos por instancia paginator y variable get por modelo
        all_task = paginator.get_page(page)

    return render(request, 'todolist.html', {'all_task': all_task})

########################################################################################
# docorador de restriccion | login_required
@login_required
    # crea una funcion para borrar y se agrega el parametro que captura el id
def delete_task(request, task_id):
    # se crea variable task que trae solamente el id buscado
    task = TaskList.objects.get(pk=task_id)
    # solamente si el duenho de la tarea (trask) es igual a id del request se puede borrar
    if task.manage == request.user:
        # luego se ejecuta el borrado del mismo
        task.delete()
    # sino se envia un mensaje    
    else:
        messages.error(request, ("Access restricted, you're not allowed!"))    
    # se redirecciona a la app
    return redirect('todolist')

########################################################################################
# docorador de restriccion | login_required
@login_required
    # crea una funcion para cambiar el valor a completado y se agrega el parametro que captura el id
def complete_task(request, task_id):
    # se crea variable task que trae solamente el id buscado
    task = TaskList.objects.get(pk=task_id)
    # solamente si el duenho de la tarea (trask) es igual a id del request se puede completar
    if task.manage == request.user:
    # luego se ejecuta el borrado del mismo
        task.done = True
        task.save()
    # sino se envia un mensaje    
    else:
        messages.error(request, ("Access restricted, you're not allowed!"))
    # se redirecciona a la app
    return redirect('todolist')

########################################################################################
# docorador de restriccion | login_required
@login_required
    # crea una funcion para cambiar el valor a pendiete y se agrega el parametro que captura el id
def pending_task(request, task_id):
    # se crea variable task que trae solamente el id buscado
    task = TaskList.objects.get(pk=task_id)
    # luego se ejecuta el borrado del mismo
    task.done = False
    task.save()
    # se redirecciona a la app
    return redirect('todolist')

########################################################################################
# docorador de restriccion | login_required
@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        # se le envia tambien el instance que es el valor por defecto que se esta editando
        # en el form
        form = TaskForm(request.POST or None, instance = task)    
        # si es valido el formato, graba en la base de datos
        if form.is_valid():
            form.save()
        messages.success(request, ("Task edited!"))
        return redirect('todolist')
    else:
        task_object = TaskList.objects.get(pk=task_id)
    return render(request, 'edit.html', {'task_object': task_object})

########################################################################################

def contact(request):
    context = {
        'contact_text' : "Welcome to Contact Page.",
    }
    return render(request, 'contact.html', context)

########################################################################################

def about(request):
    context = {
        'about_text' : "Welcome to About Us Page.",
    }
    return render(request, 'about.html', context)

########################################################################################

def index(request):
    context = {
        'index_text' : "Welcome to index Page.",
    }
    return render(request, 'index.html', context)

########################################################################################       