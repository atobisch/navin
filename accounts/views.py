from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from travello.models import Destination


def home_view(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        passsword2 = request.POST['password2']
        email = request.POST['email']

        #Checks
        if password1==passsword2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-Mail already taken')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'user created')
                return redirect('accounts:login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('accounts:register')
    else: # Dann ist die Method GET
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('accounts:login')
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def write(request):
    if request.method == 'GET':
        return render(request, 'accounts/write.html')
    elif request.method == 'POST':
        # Userinputs in Variablen speichern
        ort=request.POST['name']
        beschreibung=request.POST['desc']
        preis=int(request.POST['price'])

        newdest = Destination.objects.create() #Object anlegen
        #Objectattribute beschreiben
        newdest.name=(ort)
        newdest.desc = (beschreibung)
        newdest.price = (preis)
        newdest.save() #In die Datenbank speichern
        return redirect('travello:home')


def logout(request):
    auth.logout(request)
    return redirect('accounts:home')