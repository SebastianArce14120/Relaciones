from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

# Create your views here.

def create(request):
  art1 = Article(headline = "Articulo 1")
  art2 = Article(headline = "Articulo 2")
  art3 = Article(headline = "Articulo 3")

  art1.save()
  art2.save()
  art3.save()

  pub1 = Publication(title="Titulo 1")
  pub2 = Publication(title="Titulo 2")
  pub3 = Publication(title="Titulo 3")
  pub4 = Publication(title="Titulo 4")
  pub5 = Publication(title="Titulo 5")
  pub6 = Publication(title="Titulo 6")
  pub7 = Publication(title="Titulo 7")
  pub8 = Publication(title="Titulo 8")

  pub1.save()
  pub2.save()
  pub3.save()
  pub4.save()
  pub5.save()
  pub6.save()
  pub7.save()
  pub8.save()

  #Relacionar modelos.

  art1.publications.add(pub1)
  art1.publications.add(pub2)
  art1.publications.add(pub3)
  art1.publications.add(pub4)
  art1.publications.add(pub5)
  art1.publications.add(pub6)
  art1.publications.add(pub7)
  art1.publications.add(pub8)

  return HttpResponse("Datos creados may to many")


def  consultar (request, id):
  r = Publication.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (r)
  return HttpResponse (f"Id: {r.id},Titulo: {r.title}")  

def  modificar(request,title,id):
    
  r = Publication.objects.get(id=id)
  r.title = title
  r.save()
  

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  r = Publication.objects.get(id=id)
  r.delete()
  return HttpResponse ("Registro Eliminado")