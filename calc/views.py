from django.shortcuts import render, redirect
from django.urls import reverse


def home_view(request):
    return render(request,'calc/home.html')

def add_view(request):
    if request.method == 'POST':
        val1 = float(request.POST['num1'])
        val2 = float(request.POST['num2'])
        res = val1 + val2
        return render(request, 'calc/result.html', {'result': res})
    elif request.method == 'GET':
        return render(request, 'calc/add_view.html')

def mult_view(request):
    if request.method == 'POST':
        val1 = float(request.POST['num1'])
        val2 = float(request.POST['num2'])
        res = val1 * val2
        return render(request, 'calc/result.html', {'result': res})
    elif request.method == 'GET':
        return render(request, 'calc/mult_view.html')

def sub_view(request):
    if request.method == 'POST':
        val1 = float(request.POST['num1'])
        val2 = float(request.POST['num2'])
        res = val1 - val2
        return render(request, 'calc/result.html', {'result': res})
    elif request.method == 'GET':
        return render(request, 'calc/sub_view.html')