from django.db import models
from datetime import datetime

# Create your models here.

class Quote(models.Model):
    content = models.CharField(max_length= 100)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.content}'