from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Login,student,python


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class pythonSerializer(serializers.ModelSerializer):
    class Meta:
        model = python
        fields = "__all__"
        
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"