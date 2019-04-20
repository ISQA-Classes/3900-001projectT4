from django.contrib import admin
from .models import Activity, Profile, Organization

#added by amber
from .models import Volunteer


class ActivityList(admin.ModelAdmin):
    list_display = ('type', 'start_time')
    list_display = ('type', 'start_time')
    search_fields = ('title', 'type')
    ordering = ['type']


#added by amber
class VolunteerList(admin.ModelAdmin):
    list_display = ('type', 'start_time')
    list_display = ('type', 'start_time')
    search_fields = ('vol_name', 'type')
    ordering = ['type']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'city', 'state', 'phone', 'zipcode', 'email']


# Register your models here.
admin.site.register(Activity)
admin.site.register(Profile)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Volunteer)
