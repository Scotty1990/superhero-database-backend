from django.urls import path
from . import views

urlpatterns = [
    path('', views.superhero_list, name='superhero_list'),
    path('villains/', views.supervillain_list, name='supervillain_list'),
    path('heroes/<int:pk>', views.superhero_detail, name='superhero_detail'),
    path('villains/<int:pk>', views.supervillain_detail, name='supervillain_detail'),
    path('heroes/new', views.superhero_create, name='superhero_create'),
    path('villains/new', views.supervillain_create, name='supervillain_create'),
    path('heroes/<int:pk>/edit', views.superhero_edit, name='superhero_edit'),
    path('villains/<int:pk>/edit', views.supervillain_edit, name='supervillain_edit'),
    path('heroes/<int:pk>/delete', views.superhero_delete, name='superhero_delete'),
    path('villains/<int:pk>/delete', views.supervillain_delete, name='supervillain_delete'),
]