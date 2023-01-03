from django.db import models


# Create your models here.
class user_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


def __str__(self):
    return self.username


class about(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    image = models.FileField(default=0)
