
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onetoone/', include('onetoone.urls'),name='onetoone'),
    path('OneToMany/', include('OneToMany.urls'),name='OneToMany'),
    path('manytomany/', include('manytomany.urls'),name='manytomany')

]
