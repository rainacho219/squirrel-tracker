from django.shortcuts import render
from sightings.models import Sightings
import random

def map(request):
    sample = random.sample(range(Sightings.objects.count()),100)
    sightings = [Sightings.objects.all()[i] for i in sample]
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/map.html', context)

# Create your views here.
