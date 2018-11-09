from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def recruguide(request):
    return render(request, 'main/recruguide.html')

def forstudent(request):
    return render(request, 'main/forstudent.html')

def forteachers(request):
    return render(request, 'main/forteachers.html')

def roadmap(request):
    return render(request, 'main/roadmap.html')

def contractcode(request):
    return render(request, 'main/contractcode.html')

def mytransaction(request):
    return render(request, 'main/mytransaction.html')