from django.shortcuts import render

def home(request):
    return render(request,'home.html')


from django.shortcuts import render
from CarName.models import Car

def home(request):
    data = Car.objects.all()
    return render(request,'home.html',{'data' : data})