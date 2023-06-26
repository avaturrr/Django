import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def get_data(request):
    data = datetime.datetime.now()
    return HttpResponse(data)


def number_2(request, number):
    sq_number = number ** 2
    return HttpResponse(f"number {number} squared  equals {sq_number}")


def even_number(request, word):
    if len(word) % 2 == 0:
        new_word = word[1::2]
        return HttpResponse(new_word)
    else:
        return redirect("home_page")
