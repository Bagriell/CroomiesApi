from django.db.models import fields
from rest_framework import serializers
from .models import Address
from django.contrib.auth.models import User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'address', 'country', 'postcode')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user