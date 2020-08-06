from django.shortcuts import render

def home_view(request):
    return render(request,'calc/home.html')

def add_view(request):
    return render(request, 'calc/add_view.html')

def add(request):
    val1 = float(request.POST['num1'])
    val2 = float(request.POST['num2'])
    res = val1 + val2
    return render(request, 'calc/result.html', {'result':res})

def mult_view(request):
    return render(request, 'calc/mult_view.html')

def mult(request):
    val1 = float(request.POST['num1'])
    val2 = float(request.POST['num2'])
    res = val1 * val2
    return render(request, 'calc/result.html', {'result':res})

def sub_view(request):
    return render(request, 'calc/sub_view.html')

def sub(request):
    val1 = float(request.POST['num1'])
    val2 = float(request.POST['num2'])
    res = val1 - val2
    return render(request, 'calc/result.html', {'result':res})