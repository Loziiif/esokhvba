from rest_framework import serializers
from .models import User, Orshinsuu, Tulbur, Notification, Sanal, Soh  # <-- '.' заавал нэм

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrshinsuuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orshinsuu
        fields = '__all__'

class TulburSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tulbur
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class SanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanal
        fields = '__all__'

class SohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soh
        fields = '__all__'
