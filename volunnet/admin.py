from django.contrib import admin
from .models import Activity


class ActivityList(admin.ModelAdmin):
    list_display = ('type', 'start_time')
    list_display = ('type', 'start_time')
    search_fields = ('title', 'type')
    ordering = ['type']


# Register your models here.
admin.site.register(Activity)