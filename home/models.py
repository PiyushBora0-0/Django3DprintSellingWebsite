from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    desc = models.TextField(max_length=225)
    date=models.DateField()
    def __str__(self):
        return f'{self.name} - {self.email}'
# Create your models here.
