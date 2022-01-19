from rest_framework import serializers
from .models import SuperHero, SuperVillain

class SuperHeroSerializer(serializers.HyperlinkedModelSerializer):
    # superhero_posts = serializers.HyperlinkedRelatedField(
    #     view_name='superhero_post_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = SuperHero
        fields = ('id', 'name', 'creators', 'alter_ego', 'place_of_residence', 'description', 'origin_story', 'career', 'image_url', 'aliases', 'powers', 'comics', 'movies', 'other_forms_of_media')

class SuperVillainSerializer(serializers.HyperlinkedModelSerializer):
    # supervillain_posts = serializers.HyperlinkedRelatedField(
    #     view_name='supervillain_post_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = SuperVillain
        fields = ('id', 'name', 'creators', 'alter_ego', 'place_of_residence', 'description', 'origin_story', 'career', 'image_url', 'aliases', 'powers', 'comics', 'movies', 'other_forms_of_media')

# class SuperVillainSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         supervillains = serializers.HyperlinkedRelatedField(
#             view_name='supervillain_detail',
#             many=True,
#             read_only=True
#         )

# class SuperHeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         supervillains = serializers.HyperlinkedRelatedField(
#             view_name='supervillain_detail',
#             many=True,
#             read_only=True
#         )

# class SuperHeroPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SuperHeroPost
#         fields = ('superhero', 'title', 'author', 'body',)

# class SuperVillainPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SuperVillainPost
#         fields = ('supervillain', 'title', 'author', 'body',)
