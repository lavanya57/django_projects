from tabnanny import verbose
from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200, null=True, blank=True)
    video_link =models.FileField(null=True, upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date = models.DateField()

    def  __str__(self):
        return  self.caption 
    
    class Meta:

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'