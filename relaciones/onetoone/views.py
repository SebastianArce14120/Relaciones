from django.shortcuts import render
from django.http import HttpResponse
from.models import Place, Restaurant

# Create your views here.

def create(request):
  place = Place(name= "centro", adress="calle 45 No 20 -13")
  place.save()

  restaurant = Restaurant(place=place, employees=25)
  restaurant.save()

  return HttpResponse("Datos creados correctamente")