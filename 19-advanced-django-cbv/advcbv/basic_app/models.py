from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(
        School, related_name='students', null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
