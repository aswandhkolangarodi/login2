from django.shortcuts import render

# Create your views here.
def loginfn(req):
    return render(req,'login.html')
def fnhome(req):
    return render(req,'home.html')
    

