from rest_framework import serializers
from .models import Card
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta :
        model = Card
        fields = ("id", 'title', 'info', 'owner',)


class UserSerializer(serializers.ModelSerializer):
    card = CardSerializer(many=True, source='user')

    class Meta:
        model = User
        fields = ('id', 'username', 'card')
