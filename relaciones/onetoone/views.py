from django.shortcuts import render
from django.http import HttpResponse
from.models import Place,Restaurant

# Create your views here.

def create (resquest):

#creamos lugar
## place=Place (name ="Centro", addres="calle 45 No 20 - 12")
## place.save()

  #Creamos restaurant

##  restaurant = Restaurant(place=place, employees=25)
## restaurant.save()
  restaurante= Restaurant.objects.get(place_id=2)
  print(restaurante.place.addres)

  return HttpResponse (restaurante.place.addres)


 ## return HttpResponse ("Datos guardades corectamente")



