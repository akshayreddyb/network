from __future__ import unicode_literals

from django.db import models

class Administrator(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=15)
    phone_number=models.CharField(max_length=14)

    def __str__(self):
        return self.username
