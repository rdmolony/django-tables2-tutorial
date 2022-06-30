from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")

    def __str__(self) -> str:
        return self.name