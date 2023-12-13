from django.contrib import admin

from .models import (
    AdmissionsPage,
    AdmissionsImage
)

admin.site.register(AdmissionsPage)
admin.site.register(AdmissionsImage )