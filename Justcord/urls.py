

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse   



# def home(request):
#     return HttpResponse('Welcome Home')

# def room(request):
#     return HttpResponse("Welcome to the Room")



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('base.urls')) 
  
    
]
