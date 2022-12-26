from django.contrib import admin

from .models import (
    Worker,
    Education,
    Education_level,
    Work_experience,
    Languages,
    Language_types,
    Skills,
    Driver_licenses
)

admin.site.register(Worker)
admin.site.register(Education)
admin.site.register(Education_level)
admin.site.register(Work_experience)
admin.site.register(Languages)
admin.site.register(Language_types)
admin.site.register(Skills)
admin.site.register(Driver_licenses)
