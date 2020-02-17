from django.db import models
from django.core.validators import MinValueValidator

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    mail = models.EmailField()

    def __repr__(self):
      return "{}: {}".format(self.pk, self.name)

      __str__ = __repr__

