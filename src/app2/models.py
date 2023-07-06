from django.db import models

# Create your models here.

from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    age = models.SmallIntegerField()
    profession = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name



