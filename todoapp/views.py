from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render( request, 'todoapp/index.html')


def homepage(request):
    return render( request, 'todoapp/homepage.html')
