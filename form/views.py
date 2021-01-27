from django.shortcuts import render
from django.http import HttpResponse

def start(request):
	return render(request,'form/start.html')

def home(request):
	return render(request,'form/base.html')