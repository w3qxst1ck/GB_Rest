from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .serializers import UserModelSerializer

User = get_user_model()


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

