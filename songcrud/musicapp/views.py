from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


from .models import Artiste, Lyric, Song
from .serializers import ArtisteSerializer, LyricSerializer, SongSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
class ArtisteListAPIView(APIView):
    # 1. List all
    def get(self, request, *args, **kwargs):

        """
        List all the Artiste
        """
        artiste = Artiste.objects.all()
        serializer = ArtisteSerializer(artiste, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 2. Create a new Artiste
    def post(self, request, *args, **kwargs):
        """
        Create a new Artiste with a given Artiste data
        """
        data ={
          'first_name':  request.data.get('first_name'),
          'last_name': request.data.get('last_name'),
          'age': request.data.get('age'),
        }
        serializer = ArtisteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Artistes Songs
class ArtisteSongsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """
        List all the songs of an artiste

        """
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        """
        Create a new SOng with a given Artiste data)
        """
        data ={
          'title':  request.data.get('title'),
          'date_released': request.data.get('date_released'),
          'likes': request.data.get('likes'),
          'artiste_id': request.data.get('artiste_id'),
        }
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Artistes Lyric
class ArtisteLyricAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """
        List all the lyric of a song
        """
        lyric = Lyric.objects.all()
        serializer = LyricSerializer(lyric, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self, request, *args, **kwargs):
        """                
        Create a new Lyric with a given Artiste data)                
        """
        data ={
          'content':  request.data.get('content'),
          'song_id': request.data.get('song_id')
        }
        serializer = LyricSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# updating 
@api_view(['POST'])
def update_artiste(request, pk):
    item = Artiste.objects.get(pk=pk)
    data = ArtisteSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['POST'])
def update_song(request, pk):
    item = Song.objects.get(pk=pk)           
    data = SongSerializer(instance=item, data=request.data)           
    if data.is_valid():           
        data.save()           
        return Response(data.data)           
    else:           
        return Response(status=status.HTTP_404_NOT_FOUND)           
        
@api_view(['POST'])
def update_lyric(request, pk):
    item = Lyric.objects.get(pk=pk)           
    data = LyricSerializer(instance=item, data=request.data)           
    if data.is_valid():           
        data.save()           
        return Response(data.data)           
    else:           
        return Response(status=status.HTTP_404_NOT_FOUND)


# # deleting 
@api_view(['DELETE'])

def delete_artiste(request, pk):           
    try:           
        item = Artiste.objects.get(pk=pk)           
        item.delete()           
        return Response(status=status.HTTP_204_NO_CONTENT)           
    except Artiste.DoesNotExist:          
        return Response(status=status.HTTP_404_NOT_FOUND)           
        
@api_view(['DELETE'])
def delete_song(request, pk):           
    try:           
        item = Song.objects.get(pk=pk)           
        item.delete()           
        return Response(status=status.  HTTP_204_NO_CONTENT)           
    except Song.DoesNotExist:           
        return Response(status=status.HTTP_404_NOT_FOUND)           
        
@api_view(['DELETE'])
def delete_lyric(request, pk):           
    try:           
        item = Lyric.objects.get(pk=pk)            
        item.delete()            
        return Response(status=status.HTTP_204_NO_CONTENT)            
    except Lyric.DoesNotExist:           
        return Response(status=status.HTTP_404_NOT_FOUND)       