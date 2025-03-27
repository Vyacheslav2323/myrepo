from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import TodoItem
def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def todos (request):
  items = TodoItem.objects.all()
  return render(request, 'todos.html', {"todos": items})