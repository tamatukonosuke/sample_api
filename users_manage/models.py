from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    mail = models.EmailField()

class Entry(models.Model):
    title = models.CharField(max_length=128)
