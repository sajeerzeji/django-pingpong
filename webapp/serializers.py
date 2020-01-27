from rest_framework import serializers
from .models import PingPong

class PingPongSerializer(serializers.ModelSerializer):

    class Meta:
        model = PingPong
        # fields = ('pong')
        fields = '__all__'