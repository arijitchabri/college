from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Departments'

class SubDepartment(models.Model):
    subDep = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.subDep}'

    class Meta:
        verbose_name_plural = 'SubDepartments'

class Quote(models.Model):
    tag = models.ForeignKey('Department', on_delete = models.CASCADE, default = 1)
    tag2 = models.ForeignKey('SubDepartment', on_delete = models.CASCADE, default = 1)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.id} : {self.tag} : {self.tag2} :: {self.content}'