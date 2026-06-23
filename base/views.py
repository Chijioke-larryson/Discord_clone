from django.shortcuts import get_object_or_404, render
from .models import Room


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = get_object_or_404(Room, id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


# def createRoom(request):
#     context = {}
#     return render(request, 'base/room_form.html', context)