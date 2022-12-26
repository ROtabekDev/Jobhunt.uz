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
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Social_networks)
admin.site.register(Social_network_types)
admin.site.register(Indisturial_sector)
admin.site.register(Speciality)
admin.site.register(Currency_types)



