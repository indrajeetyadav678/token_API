from rest_framework import serializers
from .models import*

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields="__all__"


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields="__all__"

