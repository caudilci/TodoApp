from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")

    return render(request, 'todo/index.html', {"todo_items": todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    inputTask = request.POST["task"]
    inputDescription = request.POST["description"]
    created_obj = Todo.objects.create(added_date=current_date, task=inputTask, description=inputDescription)
    return HttpResponseRedirect("/todo")

@csrf_exempt
def delete_todo(request, item_id):
    Todo.objects.get(id=item_id).delete()
    return HttpResponseRedirect("/todo")

def description(request, item_id):
    item = Todo.objects.get(id=item_id)
    return render(request, 'todo/description.html', {"item": item})
