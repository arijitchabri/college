from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Quote)
admin.site.register(models.QuoteBCA)
admin.site.register(models.QuoteBSC)
admin.site.register(models.QuoteMSC)
