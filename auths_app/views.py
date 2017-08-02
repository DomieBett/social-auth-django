from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
# Create your views here.

def index(request):
    email = "email@example.com"
    password = "password"
    string = (str(email) + " " + str(password))
    return HttpResponse("Whodiss" + string)

def login(request):
    pass

def home(request):
   context = {'user': request.user}
   return render(request=request, template_name='home.html', context=context)