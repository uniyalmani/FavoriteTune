from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Artist, Audio
from auth_app.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
import random
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
# Create your views here.



class UploadSongs(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]
    def post(self, request):
        try:

            if not request.info["valid"]:
                messages.error(request, 'Invalid token. for uploading images please loging')
                return redirect('/auth/login')
            
        
        
            
        
        # Get artist name from the form data
            artist_name = request.data.get('artist', '')
            
            song_name = request.data.get('songname', '')
            
            # Strip leading and trailing whitespaces and convert to uppercase
            artist_name = artist_name.strip().upper()
            
            artist = create_or_get_artist(artist_name=artist_name)

            # Get the uploaded MP3 file
            mp3_file = request.data.get('songs', None)
            

            
            user = request.info["user"]
            audio = Audio(title= song_name,user=user, audio_file=mp3_file, artist=artist)
            audio.save()
                        
                
        
            

            return redirect('/user/songs')
        except Exception as e:
            messages.error(request, e.messages)
            return redirect('/auth/login')
        

    def get(self, request):
        response = render(request, template_name="upload_song.html")
        return response 
    

class Songs(APIView):

    # permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    # parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def get(self, request):
        try:
        
            if not request.info["valid"]:
                messages.error(request, 'Invalid token. for viewing images please loging')
                return redirect('/auth/login')
            
            user_email = request.info["user"].email
            user = User.objects.get(email=user_email)
        
        
            Audio_file = Audio.objects.filter(user=user)
            
            
    
            context = {"audio_files": Audio_file}
            return render(request, template_name="song_list.html", context=context)
        except Exception as e:
            messages.error(request, e.messages)
            return redirect('/auth/login')




def home(request):

    return render(request, template_name="home.html")
    

def profile(request):
    return render(request, template_name="profile.html")


def check_email(request):
    email = request.GET["email"]

    # Check if the email address already exists in the database
    
    
    try:

        User.objects.get(email=email)
        res = JsonResponse({"exists": True}, status = 200)

        return res
    except User.DoesNotExist:
        res = JsonResponse({"exists": False}, status = 400)
        return res



def create_or_get_artist(artist_name):
    # Check if the artist already exists
    existing_artist = Artist.objects.filter(name=artist_name).first()

    if existing_artist:
        # If the artist exists, return the existing instance
        return existing_artist
    else:
        # If the artist doesn't exist, create a new entry
        new_artist = Artist(name=artist_name)
        new_artist.save()
        return new_artist
        

  