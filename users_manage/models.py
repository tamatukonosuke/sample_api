from django.db import models
from django.core.validators import MinValueValidator

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    mail = models.EmailField()

    def __repr__(self):
      return "{}: {}".format(self.pk, self.name)

      __str__ = __repr__  # __str__にも同じ関数を適用

class Entry(models.Model):
    title = models.CharField(max_length=128)
