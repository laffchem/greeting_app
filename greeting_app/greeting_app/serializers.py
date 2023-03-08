from rest_framework import serializers
from .models import Greeting


class GreetingSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=100)