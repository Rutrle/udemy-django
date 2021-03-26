from django.shortcuts import render
from .models import User
from .forms import UserForm

# Create your views here.


def indexview(request):
    users = User.objects.order_by('second_name')
    context = {'users': users}

    return render(request, 'index.html', context=context)


def help_view(request):
    context = {"header": "Help page"}
    return render(request, "help_page.html", context=context)


def input_view(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return indexview(request)
        else:
            print("Error, form invalid")

    context = {"form": form}

    return render(request, "input_page.html", context=context)
