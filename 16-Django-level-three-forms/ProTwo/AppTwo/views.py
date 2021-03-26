from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.


def indexview(request):
    users = User.objects.order_by('second_name')
    context = {'users': users}

    return render(request, 'index.html', context=context)


def help_view(request):
    context = {"header": "Help page"}
    return render(request, "help_page.html", context=context)
