from django.contrib import admin
from .models import Activity

# Register your models here.
admin.site.register(Activity)


class ActivityList(admin.ModelAdmin):
    list_display = ('type', 'start_time')
    list_display = ('type', 'start_time')
    search_fields = ('title', 'type')
    ordering = ['type']
