from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def teju(request):
    return render(request,'teju.html')

def bokkapapa(request):
    return HttpResponse('<h1>iam foodie</h1>')

def chandu(request):
    return render(requesr,'chandu.html')

def dog(request):
    return HttpResponse('<h1>iam workholic</h1>')

def bhavya(request):
    return render(request,'bhavya.html')

def snupie(request):
    return HttpResponse('<h1>iam taller</h1>')

