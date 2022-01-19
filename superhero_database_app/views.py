from django.shortcuts import render, redirect
from .models import SuperVillain, SuperHero, SuperHeroPost, SuperVillainPost
from .forms import SuperHeroForm, SuperVillainForm, SuperHeroPostForm, SuperVillainPostForm
from rest_framework import generics
from .serializers import SuperHeroSerializer, SuperVillainSerializer

# Create your views here.

class SuperHeroList(generics.ListCreateAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer

class SuperHeroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer

class SuperVillainList(generics.ListCreateAPIView):
    queryset = SuperVillain.objects.all()
    serializer_class = SuperVillainSerializer

class SuperVillainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperVillain.objects.all()
    serializer_class = SuperVillainSerializer

# def superhero_list(request):
#     superheroes = SuperHero.objects.all()
#     return render(request, 'superhero_database_app/superhero_list.html', {'superheroes': superheroes})

# def supervillain_list(request):
#     supervillains = SuperVillain.objects.all()
#     return render(request, 'superhero_database_app/supervillain_list.html', {'supervillains': supervillains})

# def superhero_detail(request, pk):
#     superhero = SuperHero.objects.get(pk=pk)
#     return render(request, 'superhero_database_app/superhero_detail.html', {'superhero': superhero})

# def supervillain_detail(request, pk):
#     supervillain = SuperVillain.objects.get(pk=pk)
#     return render(request, 'superhero_database_app/supervillain_detail.html', {'supervillain': supervillain})

# def superhero_create(request):
#     if request.method == 'POST':
#         form = SuperHeroForm(request.POST)
#         if form.is_valid():
#             superhero = form.save()
#             return redirect('superhero_detail', pk=superhero.pk)
#     else:
#         form = SuperHeroForm()
#     return render(request, 'superhero_database_app/superhero_form.html', {'form': form})

# def supervillain_create(request):
#     if request.method == 'POST':
#         form = SuperVillainForm(request.POST)
#         if form.is_valid():
#             supervillain = form.save()
#             return redirect('supervillain_detail', pk=supervillain.pk)
#     else:
#         form = SuperVillainForm()
#     return render(request, 'superhero_database_app/supervillain_form.html', {'form': form})

# def superhero_edit(request, pk):
#     superhero = SuperHero.objects.get(pk=pk)
#     if request.method == "POST":
#         form = SuperHeroForm(request.POST, instance=superhero)
#         if form.is_valid():
#             superhero = form.save()
#             return redirect('superhero_detail', pk=superhero.pk)
#     else:
#         form = SuperHeroForm(instance=superhero)
#     return render(request, 'superhero_database_app/superhero_form.html', {'form': form})

# def supervillain_edit(request, pk):
#     supervillain = SuperVillain.objects.get(pk=pk)
#     if request.method == "POST":
#         form = SuperVillainForm(request.POST, instance=supervillain)
#         if form.is_valid():
#             supervillain = form.save()
#             return redirect('supervillain_detail', pk=supervillain.pk)
#     else:
#         form = SuperVillainForm(instance=supervillain)
#     return render(request, 'superhero_database_app/supervillain_form.html', {'form': form})

# def superhero_delete(request, pk):
#     SuperHero.objects.get(pk=pk).delete()
#     return redirect('superhero_list')

# def supervillain_delete(request, pk):
#     SuperVillain.objects.get(pk=pk).delete()
#     return redirect('supervillain_list')

# def superhero_post_list(request):
#     superhero_posts = SuperHeroPost.objects.all()
#     return render(request, 'superhero_database_app/superhero_post_list.html', {'superhero_posts': superhero_posts})

# def supervillain_post_list(request):
#     supervillain_posts = SuperVillainPost.objects.all()
#     return render(request, 'superhero_database_app/supervillain_post_list.html', {'supervillain_posts': supervillain_posts})

# def superhero_post_detail(request, pk):
#     superhero_post = SuperHeroPost.objects.get(pk=pk)
#     return render(request, 'superhero_database_app/superhero_post_detail.html', {'superhero_post': superhero_post})

# def supervillain_post_detail(request, pk):
#     supervillain_post = SuperVillainPost.objects.get(pk=pk)
#     return render(request, 'superhero_database_app/supervillain_post_detail.html', {'supervillain_post': supervillain_post})

# def superhero_post_create(request):
#     if request.method == 'POST':
#         form = SuperHeroPostForm(request.POST)
#         if form.is_valid():
#             superhero_post = form.save()
#             return redirect('superhero_post_detail', pk=superhero_post.pk)
#     else:
#         form = SuperHeroPostForm()
#     return render(request, 'superhero_database_app/superhero_post_form.html', {'form': form})

# def supervillain_post_create(request):
#     if request.method == 'POST':
#         form = SuperVillainPostForm(request.POST)
#         if form.is_valid():
#             supervillain_post = form.save()
#             return redirect('supervillain_post_detail', pk=supervillain_post.pk)
#     else:
#         form = SuperVillainPostForm()
#     return render(request, 'superhero_database_app/supervillain_post_form.html', {'form': form})

# def superhero_post_edit(request, pk):
#     superhero_post = SuperHeroPost.objects.get(pk=pk)
#     if request.method == "POST":
#         form = SuperHeroPostForm(request.POST, instance=superhero_post)
#         if form.is_valid():
#             superhero_post = form.save()
#             return redirect('superhero_post_detail', pk=superhero_post.pk)
#     else:
#         form = SuperHeroPostForm(instance=superhero_post)
#     return render(request, 'superhero_database_app/superhero_post_form.html', {'form': form})

# def supervillain_post_edit(request, pk):
#     supervillain_post = SuperVillainPost.objects.get(pk=pk)
#     if request.method == "POST":
#         form = SuperVillainPostForm(request.POST, instance=supervillain_post)
#         if form.is_valid():
#             supervillain_post = form.save()
#             return redirect('supervillain_post_detail', pk=supervillain_post.pk)
#     else:
#         form = SuperVillainPostForm(instance=supervillain_post)
#     return render(request, 'superhero_database_app/supervillain_post_form.html', {'form': form})

# def superhero_post_delete(request, pk):
#     SuperHeroPost.objects.get(pk=pk).delete()
#     return redirect('superhero_post_list')

# def supervillain_post_delete(request, pk):
#     SuperVillainPost.objects.get(pk=pk).delete()
#     return redirect('supervillain_post_list')


# class SuperHeroView(generics.ListAPIView):
#     model = SuperHero
#     serializer_class = SuperHeroSerializer

# class SuperVillainView(generics.ListAPIView):
#     model = SuperVillain
#     serializer_class = SuperVillainSerializer

# class SuperHeroPostView(generics.ListAPIView):
#     model = SuperHeroPost
#     serializer_class = SuperHeroPostSerializer

# class SuperVillainPostView(generics.ListAPIView):
#     model = SuperVillainPost
#     serializer_class = SuperVillainPostSerializer

# def index(request, *args, **kwargs):
#     return render(request, 'superhero_database_app/index.html')
