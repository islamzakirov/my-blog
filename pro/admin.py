from django.contrib import admin

# Register your models here.
from .models import *

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_display_links = ('name',)
    search_fields = ('name')

admin.site.register(Blog)