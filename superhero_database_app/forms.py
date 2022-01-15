from django import forms
from .models import SuperHero, SuperVillain

class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHero
        fields = ('name', 'creators', 'alter_ego', 'place_of_residence', 'description', 'origin_story', 'career', 'image_url', 'aliases', 'powers', 'comics', 'movies', 'other_forms_of_media',)

class SuperVillainForm(forms.ModelForm):
    class Meta:
        model = SuperVillain
        fields = ('name', 'creators', 'alter_ego', 'place_of_residence', 'description', 'origin_story', 'career', 'image_url', 'aliases', 'powers', 'comics', 'movies', 'other_forms_of_media',)