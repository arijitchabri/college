from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Quote)
admin.site.register(models.QuoteMSC)
admin.site.register(models.QuoteBSC)