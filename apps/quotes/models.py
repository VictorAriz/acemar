from django.db import models

# Create your models here.


class Quotes(models.Model):
    name = models.CharField(max_length=50)
    document = models.PositiveSmallIntegerField(null=True)
    phone = models.PositiveSmallIntegerField(null=True)
    mail = models.EmailField(null=True)
    typematerial = models.CharField(max_length=50, null=True)
    description = models.TextField()
    # text = models.CharField(max_length=50, null=True)



    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)