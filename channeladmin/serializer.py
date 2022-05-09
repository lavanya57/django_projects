from rest_framework import serializers
from .models import Video

class VedioListSerializer(serializers.Serializer):
   caption = serializers.CharField(max_length=200)
   video = serializers.FileField()
   date = serializers.DateField()

   class Meta:
      model = Video
      fields = ['id', 'caption', 'video_id','video_link' 'date']

   def get_id(obj):
      return obj.id

   def get_id(obj):
      return obj.caption

   def get_video_id(obj):
      return obj.video_id
   
   def get_video_link(obj):
      return obj.video_link

   def get_date(obj):
      return obj.date


class VideoUploadSerializer(serializers.ModelSerializer):
   caption = serializers.CharField(max_length=200)
   video_id = serializers.CharField(allow_null=True, allow_blank=True)
   video_link = serializers.FileField(allow_null=True)
   date = serializers.DateField()

   class Meta:
      model = Video
      fields = ('__all__')

