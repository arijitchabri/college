from django.contrib import admin
from .models import Quote, Department, SubDepartment

# Register your models here.

admin.site.register(Quote)
admin.site.register(Department)
admin.site.register(SubDepartment)