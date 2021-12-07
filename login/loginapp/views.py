from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fnlogin(req):
    return render(req,"login.html")

