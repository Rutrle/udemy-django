from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexview(request):
    return HttpResponse('<em>My second app</em>')


def help_view(request):
    context = {"header": "Help page"}
    return render(request, "help_page.html", context=context)
