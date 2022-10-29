from django.db import models

# Create your models here.

class Artiste(models.Model):
  first_name = models.CharField('Artiste first name', max_length=255)
  last_name = models.CharField( 'Artiste last name', max_length=255)
  age = models.IntegerField('Artistes Age')

class Song(models.Model):
  
  title = models.CharField(max_length=255)
  date_released = models.CharField( max_length=255)
  likes = models.CharField(max_length =255)
  artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
  
  content = models.CharField(max_length=255)
  song_id =models.ForeignKey(Song, on_delete=models.CASCADE)
  

  

  