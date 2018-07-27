from django.shortcuts import render
from django.http import HttpResponse
from .poke import get_pokemons
from .pokecard import get_card

from .models import Greeting

# Create your views here.
def index(request):
	payload = get_pokemons()
	return render(request, 'pope.html', payload)

def pokemon(request):
	payload = get_card()
	return render(request, 'card.html', {'d': payload})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

