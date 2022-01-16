from django.contrib import admin
from .models import SuperHero, SuperVillain, SuperHeroPost, SuperVillainPost, SuperHeroComment, SuperVillainComment

# Register your models here.
admin.site.register(SuperHero)
admin.site.register(SuperVillain)
admin.site.register(SuperHeroPost)
admin.site.register(SuperVillainPost)
admin.site.register(SuperHeroComment)
admin.site.register(SuperVillainComment)