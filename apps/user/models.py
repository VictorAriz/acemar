from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document = models.PositiveSmallIntegerField()
    phone = models.PositiveSmallIntegerField(null=True)
    mail = models.EmailField()
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=60, null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)
    user_name = models.CharField(max_length=50)



    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.name, self.last_name)

