from django.contrib import admin
from . import models
# Register your models here.


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(models.Quote, QuoteAdmin)
admin.site.register(models.QuoteBSC, QuoteAdmin)
admin.site.register(models.QuoteMSC, QuoteAdmin)
