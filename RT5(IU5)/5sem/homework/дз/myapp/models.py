from django.db import models


class User2(models.Model):
    id = models.AutoField(primary_key=True,)  # Тип поля
    name = models.CharField(max_length=255)
    idconcert = models.ForeignKey('Concert')

class Concert(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

