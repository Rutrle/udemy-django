from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexview(request):
    return HttpResponse('<em>My second app</em>')
