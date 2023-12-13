from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AdmissionsPageViewSet,
    AdmissionsInfoViewSet,
)


router = DefaultRouter()
router.register('page', AdmissionsPageViewSet, 'admissions')
router.register('info', AdmissionsInfoViewSet, 'admissions_info')


urlpatterns = [
]

urlpatterns += router.urls
