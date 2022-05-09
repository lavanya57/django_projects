import re
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Video
from .serializer import VedioListSerializer, VideoUploadSerializer
from rest_framework import status
import json
# Create your views here.


class VideoUploadViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request): 
        video = Video.objects.all()
        serializer = VedioListSerializer(video ,many=True)
        return Response(serializer.data)

    def create(self, request):
        if request.data['type'] == 'text':
            request.data._mutable = True
            del request.data['type']
            serializer = VideoUploadSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VedioListSerializer
    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes] 