from .serializers import (
    UserSerializer,
    OrshinsuuSerializer,
    TulburSerializer,
    NotificationSerializer,
    SanalSerializer,
    SohSerializer,
)
from .models import User, Orshinsuu, Tulbur, Notification, Sanal, Soh
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        return Response({
            "message": "Амжилттай нэвтэрлээ",
            "user_id": user.id
        })
    
    return Response({
        "error": "Нэвтрэх нэр эсвэл нууц үг буруу"
    }, status=400)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrshinsuuViewSet(viewsets.ModelViewSet):
    queryset = Orshinsuu.objects.all()
    serializer_class = OrshinsuuSerializer

class TulburViewSet(viewsets.ModelViewSet):
    queryset = Tulbur.objects.all()
    serializer_class = TulburSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class SanalViewSet(viewsets.ModelViewSet):
    queryset = Sanal.objects.all()
    serializer_class = SanalSerializer

class SohViewSet(viewsets.ModelViewSet):
    queryset = Soh.objects.all()
    serializer_class = SohSerializer
