from django.shortcuts import render
from django.http import HttpResponse
def myfunction(request):
	s='<html><body bgcolor="blue"><h1><font color="white">welcome to my first django</font></h1></body></html>'
	return HttpResponse(s) 