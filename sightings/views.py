from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sightings
from .forms import SightingForm
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Count

def index(request):
    sightings = Sightings.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/all.html', context)

def stats(request):
    sightings_age = Sightings.objects.values('Age').order_by('Age').annotate(age_count=Count('Age'))
    sightings_shift = Sightings.objects.values('Shift').order_by('Shift').annotate(shift_count=Count('Shift'))
    sightings_primaryfurcolor = Sightings.objects.values('PrimaryFurColor').order_by('PrimaryFurColor').annotate(primaryfurcolor_count=Count('PrimaryFurColor'))
    sightings_location =  Sightings.objects.values('Location').order_by('Location').annotate(location_count=Count('Location'))
    sightings_running = Sightings.objects.values('Running').order_by('Running').annotate(running_count=Count('Running'))

    context = {
        'sightings_age': sightings_age,
        'sightings_shift': sightings_shift,
        'sightings_primaryfurcolor': sightings_primaryfurcolor,
        'sightings_location': sightings_location,
        'sightings_running': sightings_running,
    }
    return render(request, 'sightings/sightings_statistics.html', context)

class AddSighting(CreateView):
    model = Sightings
    fields = '__all__'

def update(request, pk):
    obj = Sightings.objects.get(UniqueSquirrelID=pk)
    form = SightingForm(request.POST or None, instance=obj)
    context={'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {'form':form}
        messages.success(request, 'This sighting has been updated successfully!')
        return render(request, 'sightings/sightings_form_update.html', context)
    else:
        context={'form':form, 'error':'The sighting was not updated successfully.'}
        return render(request, 'sightings/sightings_form_update.html', context)

def delete(request, pk):
    obj = Sightings.objects.filter(UniqueSquirrelID=pk)
    if request.method=="POST":
        obj.delete()
        return redirect('index')
    return render(request, 'sightings/sightings_confirm_delete.html') 

# Create your views here.
