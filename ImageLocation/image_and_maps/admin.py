from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date_uploaded')
    search_fields = ('name', 'description')
    list_filter = ('date_uploaded',)
    ordering = ('-date_uploaded',)
