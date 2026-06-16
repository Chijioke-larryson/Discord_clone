from django.shortcuts import render
from  django.http import HttpResponse,request


# # Create your views here.
# def home(request):
#     return render(request, 'home.html')

# def room(request):
#     return render(request, 'room.html')



def home(request):
    return render(request, 'base/home.html')

def room(request):
    return render(request, 'base/room.html')



    