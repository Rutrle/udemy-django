from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.second_name)
