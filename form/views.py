from django.shortcuts import render
from django.http import HttpResponse

def start(request):
	return render(request,'form/start.html')

def home(request):
	return render(request,'form/homepage.html')

def aboutus(request):
	return render(request,'form/aboutus.html')	

def disclaimer(request):
	return render(request,'form/disclaimer.html')	

def feedback(request):
	return render(request,'form/feedback.html')	

def profile(request):
	return render(request, 'users/profile.html')	