from django.contrib import admin
from .models import Quote
# Register your models here.


admin.site.site_header = 'CTCJ College'
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('content', 'data_created')
    search_fields = ('content',)

    filter_horizontal = ()
    list_filter = ('data_created',)
    fieldsets = ()

admin.site.register(Quote, QuoteAdmin)