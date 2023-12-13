from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


from .permissions import IsOwner
from .models import News
from .serializers import (
    NewsCreateSerializer,
    NewsListSerializer,
    NewsSerializer,
)


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'partial_update', 'update']:
            return NewsListSerializer
        elif self.action == 'create':
            return NewsCreateSerializer
        elif self.action == 'retrieve':
            return NewsSerializer
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