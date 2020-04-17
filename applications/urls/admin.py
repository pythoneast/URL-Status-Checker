from django.contrib import admin
from .models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    fields = ('url', )
