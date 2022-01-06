from django.db import models
from django.contrib.auth.models import User


class SubUsers(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
