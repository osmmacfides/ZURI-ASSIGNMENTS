# from django.conf.urls import url
from django.urls import include, path
from musicapp import views

from .views import ArtisteListAPIView, ArtisteLyricAPIView, ArtisteSongsAPIView

urlpatterns = [
  path('api', ArtisteListAPIView.as_view(), name='artiste-list'),
  path('api2/', ArtisteSongsAPIView.as_view(), name='artiste-songs'), 
  path('api3/', ArtisteLyricAPIView.as_view(), name='artiste-lyric'),
  path('updateartiste/<int:pk>/', views.update_artiste, name='artiste_detail'),
  path('updatesong/<int:pk>/', views.update_song, name='artiste_detail'),
  path('updatelyric/<int:pk>/', views.update_lyric, name='update-items'),
  path('song/<int:pk>/delete/', views.delete_song, name='delete-items'),
  path('artiste/<int:pk>/delete/', views.delete_artiste, name='delete-items'),
  path('lyric/<int:pk>/delete/', views.delete_lyric, name='delete-items')

]