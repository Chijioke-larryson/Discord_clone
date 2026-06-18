from django.shortcuts import render
from django.http import Http404
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


rooms = [
    {"id" : 1 , "name": "Let us Learn Python"},
     {"id" :2, "name": "Let us Learn Javascript"},
    {"id" : 3 , "name": "Let us Learn Django"},
    {"id" : 4 , "name": "Code with me"},
    {"id" : 5 , "name": "Let us  answers questions"},
]
context = {'rooms': rooms}
def home(request):
    rooms = Room.objects.all()      
    return render(request, 'base/home.html', context)
def room(request, pk):
    try:
        room_id = int(pk)
        room = next(i for i in rooms if i['id'] == room_id)
    except (ValueError, StopIteration):
        raise Http404('Room does not exist')

    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html', {'room': room})


    
