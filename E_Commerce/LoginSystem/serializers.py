from rest_framework import serializers
from .models import LoginSystem

# class LoginSystemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField(max_length=25) 
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     country = serializers.CharField(max_length=20)
#     Immigration_Status = serializers.BooleanField(default=False)
#     password = serializers.CharField(max_length=25)


# Model Serializer
class LoginSystemSerializer(serializers.ModelSerializer):
 class Meta:
        model = LoginSystem
        fields = ['id', 'username', 'first_name', 'last_name', 'country', 
                  'Immigration_Status', 'password']
