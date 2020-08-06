from django.shortcuts import render

def home_view(request):
    return render(request, 'accounts/home.html')

def register(request):
    return render(request, 'accounts/register.html')
# Create your views here.
