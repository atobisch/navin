from django.db import models

# Create your models here.

class Destination(models.Model):
    #id : int
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


