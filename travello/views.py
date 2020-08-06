from django.shortcuts import render
from .models import Destination

def home_view(request):
    dests = Destination.objects.all()
    return render(request, 'travello/home.html', {'dests':dests})

