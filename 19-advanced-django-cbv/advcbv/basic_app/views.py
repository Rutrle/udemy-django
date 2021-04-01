from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models


class SchoolListView(ListView):
    model = models.School


class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'school_detail.html'
