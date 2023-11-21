from django.db import models


class Cat(models.Model):
    breeder = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    hairiness = models.CharField(max_length=50)