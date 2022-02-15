from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    value = models.PositiveSmallIntegerField(null=True)


    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)