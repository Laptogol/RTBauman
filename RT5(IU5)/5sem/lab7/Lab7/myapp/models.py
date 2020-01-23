from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    idconcert = models.harField(max_length=3)

    class Meta:
        ordering = ["-name"]


    def __unicode__(self):
        return self.name

