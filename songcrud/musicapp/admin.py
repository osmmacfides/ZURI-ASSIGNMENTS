from django.contrib import admin
from .models import Artiste, Song, Lyric

# Register your models here.
admin.site.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
  list_display = ('first_name','last_name', 'age' )

admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
  list_display = ('title', 'date_released', 'likes', 'artiste_id')
admin.site.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
  list_display = ('content', 'song_id')