from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import TodoItem
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'users/profile.html')
def users(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def todos (request):
  items = TodoItem.objects.all()
  return render(request, 'todos.html', {"todos": items})
