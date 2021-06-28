from django.contrib import admin
from .models import UrlDetailes
# Register your models here.


class UrlDetailesAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'shorted_url']


admin.site.register(UrlDetailes, UrlDetailesAdmin)
