from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PingPong
from .serializers import PingPongSerializer

class PingPongViews(APIView):

    def get(self, request):
        pingPong = PingPong()
        pingPong.pong = 'pong'
        serializer = PingPongSerializer(pingPong, many = False)
        return Response(serializer.data)
