from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Shop(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=CASCADE)

# Create your models here.
