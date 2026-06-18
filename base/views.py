from django.shortcuts import render
from  django.http import HttpResponse,request
from .models import Room

# # Create your views here.
# def home(request):
#     return render(request, 'home.html')

# def room(request):
#     return render(request, 'room.html')


# rooms = [
#     { "id" : 1 , "name": "Let us Learn Python"},
#     { "id" : 2 , "name": "Let us Learn Javascript"},
#     { "id" : 3 , "name": "Let us Learn Django"},
#     { "id" : 4 , "name": "Code with me"},
# ]

# context = {'rooms': rooms}

def home(request):
    rooms = Room.objects.all()      
    return render(request, 'base/home.html')

def room(request,):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    #         context = {'room': room}

    # room = Room.objects.get(id=pk)  # Fetch the room with id=1
    return render(request, 'base/room.html')     


    