# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Artiste, Song, Lyric

# Create your views here.
def home(request):
    artistes = Artiste.objects.all()
    songs = Song.objects.all()
    lyrics = Lyric.objects.all()

    return render(request, "index.html", {
        "artistes": artistes,  "songs": songs, "lyrics": lyrics
    })
