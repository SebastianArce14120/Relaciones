from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def create(request):
##  repo = Reporter(first_name="Juan", last_name="Arce", email="juanarcev1412@gmail.com")
## repo.save()

##  art1 = Article.objects.create(headline="Django basico", pub_date=date(2024,4,3), reporter=repo)
##  art2 = Article.objects.create(headline="Django intermedio", pub_date=date(2024,5,3), reporter=repo)
##  art3 = Article.objects.create(headline="Django avanzado", pub_date=date(2024,5,3), reporter=repo)
  
  return HttpResponse("Uno a muchos")
def  consultar (request, id):
  r = Reporter.objects.get(id=id) #trae el registro que coincida con la llave primaria

  print (r)
  return HttpResponse (f"Primer Nombre: {r.first_name}, Apellido: {r.last_name}, email: {r.email}")

def  modificar(request,first_name,last_name,email,id):
    
  r = Reporter.objects.get(id=id)
  r.first_name = first_name
  r.last_name = last_name
  r.email = email
  r.save()
  

  return HttpResponse ('Se actualizaron los Datos')

def eliminar(request,id):
  r = Reporter.objects.get(id=id)
  r.delete()
  return HttpResponse ("Registro Eliminado")








  #repo = Reporter.objects.get(id=1)
  #query = repo.article_set.all()

  #return render (request, "index.html",{
  #'repo':repo,
  #'query':query
#})
  
