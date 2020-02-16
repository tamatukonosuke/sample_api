from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'age', 'mail')

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('title')
