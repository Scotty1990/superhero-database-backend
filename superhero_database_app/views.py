from django.shortcuts import render, redirect
from .models import SuperVillain, SuperHero
from .forms import SuperHeroForm, SuperVillainForm

# Create your views here.

def superhero_list(request):
    superheroes = SuperHero.objects.all()
    return render(request, 'superhero_database_app/superhero_list.html', {'superheroes': superheroes})

def supervillain_list(request):
    supervillains = SuperVillain.objects.all()
    return render(request, 'superhero_database_app/supervillain_list.html', {'supervillains': supervillains})

def superhero_detail(request, pk):
    superhero = SuperHero.objects.get(pk=pk)
    return render(request, 'superhero_database_app/superhero_detail.html', {'superhero': superhero})

def supervillain_detail(request, pk):
    supervillain = SuperVillain.objects.get(pk=pk)
    return render(request, 'superhero_database_app/supervillain_detail.html', {'supervillain': supervillain})

def superhero_create(request):
    if request.method == 'POST':
        form = SuperHeroForm(request.POST)
        if form.is_valid():
            superhero = form.save()
            return redirect('superhero_detail', pk=superhero.pk)
    else:
        form = SuperHeroForm()
    return render(request, 'superhero_database_app/superhero_form.html', {'form': form})

def supervillain_create(request):
    if request.method == 'POST':
        form = SuperVillainForm(request.POST)
        if form.is_valid():
            supervillain = form.save()
            return redirect('supervillain_detail', pk=supervillain.pk)
    else:
        form = SuperVillainForm()
    return render(request, 'superhero_database_app/supervillain_form.html', {'form': form})

def superhero_edit(request, pk):
    superhero = SuperHero.objects.get(pk=pk)
    if request.method == "POST":
        form = SuperHeroForm(request.POST, instance=superhero)
        if form.is_valid():
            superhero = form.save()
            return redirect('superhero_detail', pk=superhero.pk)
    else:
        form = SuperHeroForm(instance=superhero)
    return render(request, 'superhero_database_app/superhero_form.html', {'form': form})

def supervillain_edit(request, pk):
    supervillain = SuperVillain.objects.get(pk=pk)
    if request.method == "POST":
        form = SuperVillainForm(request.POST, instance=supervillain)
        if form.is_valid():
            supervillain = form.save()
            return redirect('supervillain_detail', pk=supervillain.pk)
    else:
        form = SuperVillainForm(instance=supervillain)
    return render(request, 'superhero_database_app/supervillain_form.html', {'form': form})

def superhero_delete(request, pk):
    SuperHero.objects.get(pk=pk).delete()
    return redirect('superhero_list')

def supervillain_delete(request, pk):
    SuperVillain.objects.get(pk=pk).delete()
    return redirect('supervillain_list')

