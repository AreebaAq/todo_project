# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority', 'medium')  # Default to medium priority if not specified
        TodoItem.objects.create(title=title, priority=priority)
    return redirect('todo_list')

def complete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    todo.delete()
    return redirect('todo_list')
