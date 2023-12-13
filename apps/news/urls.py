from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet


router = DefaultRouter()
router.register('', NewsViewSet, 'news')


urlpatterns = [
]

urlpatterns += router.urls