from django.db import models

# Create your models here.

class Quote(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.content}'

class QuoteMSC(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.content}'

class QuoteBSC(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.content}'