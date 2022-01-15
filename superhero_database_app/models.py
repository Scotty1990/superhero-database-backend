from django.db import models

# Create your models here.
class SuperHero(models.Model):
    name = models.CharField(max_length=100, unique=True, default='name here')
    creators = models.CharField(max_length=100, default="no creators listed")
    alter_ego = models.CharField(max_length=100, default='no alter ego listed')
    place_of_residence = models.CharField(max_length=100, default="no place of residence")
    description = models.TextField(default="no description")
    origin_story = models.TextField(default="no origin listed")
    career = models.TextField(max_length=100, default="no career listed")
    image_url = models.TextField(default="no image given")
    aliases = models.CharField(max_length=100, default="no aliases listed")
    powers = models.CharField(max_length=300, default="no powers listed")
    comics = models.TextField(default="no comics")
    movies = models.TextField(default="no movies")
    other_forms_of_media = models.TextField(default="no media given")

    def __str__(self):
        return self.name

class SuperVillain(models.Model):
    name = models.CharField(max_length=100, unique=True, default='name here')
    creators = models.CharField(max_length=100, default="no creators listed")
    alter_ego = models.CharField(max_length=100, default='no alter ego listed')
    place_of_residence = models.CharField(max_length=100, default="no place of residence")
    description = models.TextField(default="no description")
    origin_story = models.TextField(default="no origin listed")
    career = models.TextField(max_length=100, default="no career listed")
    image_url = models.TextField(default="no image given")
    aliases = models.CharField(max_length=100, default="no aliases listed")
    powers = models.CharField(max_length=300, default="no powers listed")
    comics = models.TextField(default="no comics")
    movies = models.TextField(default="no movies")
    other_forms_of_media = models.TextField(default="no media given")

    def __str__(self):
        return self.name
    