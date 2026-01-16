from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from .serializers import UserSerializer

class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.all().order_by("id")