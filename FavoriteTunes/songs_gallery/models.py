from django.db import models
from auth_app.models import User

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return self.name  
    

      



class Audio(models.Model):
    title = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    audio_file = models.FileField(upload_to='audio/', blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    
    
