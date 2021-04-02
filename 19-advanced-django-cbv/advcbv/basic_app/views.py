from django.shortcuts import render
from django.views.generic import (
    View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'  # redefines name

    # returns school_list  - automatically


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')
