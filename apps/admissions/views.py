from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)

from apps.news.permissions import IsOwner
from .models import (
    AdmissionsPage,
    AdmissionsInfo
)
from .serializers import (
    AdmissionsCreateSerializer,
    AdmissionsListSerializer,
    AdmissionsPageSerializer,
    AdmissionsInfoCreateSerializer,
    AdmissionsInfoListSerializer,
    AdmissionsInfoSerializer,
)


class AdmissionsPageViewSet(ModelViewSet):
    queryset = AdmissionsPage.objects.all()
    serializer_class = AdmissionsPageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return AdmissionsListSerializer
        elif self.action == 'create':
            return AdmissionsCreateSerializer
        elif self.action == 'retrieve':
            return AdmissionsPageSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAdminUser, IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes in [IsOwner, IsAdminUser]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner, IsAdminUser]
        return super().get_permissions()


class AdmissionsInfoViewSet(ModelViewSet):
    queryset = AdmissionsInfo.objects.all()
    serializer_class = AdmissionsInfoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return AdmissionsInfoListSerializer
        elif self.action == 'create':
            return AdmissionsInfoCreateSerializer
        elif self.action == 'retrieve':
            return AdmissionsInfoSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAdminUser, IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes in [IsOwner, IsAdminUser]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner, IsAdminUser]
        return super().get_permissions()