import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)

def number_2(request, number):
    sq_number = number**2
    return HttpResponse(f"number {number} squared  equals {sq_number}")