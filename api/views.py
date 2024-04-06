from django.shortcuts import render
from django.http import HttpResponse
from .models import MyNumber

def index (response):
    return HttpResponse('Hello world!')

def show_numbers(response):
    my_list = MyNumber.objects.all()
    return HttpResponse(my_list)