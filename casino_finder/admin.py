from django.contrib import admin

# Register your models here.
from casino_finder.models import Casino


@admin.register(Casino)
class CassinoAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','created_at', 'modified_at')