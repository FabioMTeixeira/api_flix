from django.contrib import admin
from movies.models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'release_date')
    search_fields = ('name', 'genre__name')
