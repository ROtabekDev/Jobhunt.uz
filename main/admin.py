from django.contrib import admin

from .models import (
    CustomUser,
    Region,
    District,
    Social_networks,
    Social_network_types,
    Indisturial_sector,
    Speciality,
    Currency_types
)

admin.site.register(CustomUser)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region_id') 
    list_display_links = ('name',)
    list_filter = ('region_id',)
    search_fields = ('name',)
 
admin.site.register(Social_networks)
admin.site.register(Social_network_types)
admin.site.register(Indisturial_sector)
admin.site.register(Speciality)
admin.site.register(Currency_types)



