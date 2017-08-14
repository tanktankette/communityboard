from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    context_dict = {'tasks': Task.objects.all()}
    return render(request, 'tasklist/index.html', context_dict)


def check(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        checked = request.POST.get('check')
        Task.objects.get(pk=pk).completed = checked
    else:
        return HttpResponse('Not a POST request')
