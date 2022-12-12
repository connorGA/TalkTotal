from django.shortcuts import render
from .models import Room
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Working on project'},
#     {'id':2, 'name': 'world cup chat'},
#     {'id':3, 'name': 'python practice'},

# ]


def home(request):
    rooms = Room.objects.all()
    context = { 'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)