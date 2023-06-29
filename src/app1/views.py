import csv
import datetime
import os.path

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from app1.forms import UserForm


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


def save_name(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        age = request.POST.get("age")
        if not os.path.exists("/home/user/pythonProject/DjangoKS/src/app1/user_data.csv"):
            with open("/home/user/pythonProject/DjangoKS/src/app1/user_data.csv", "w") as my_file:
                csvwriter = csv.writer(my_file)
                csvwriter.writerow(["name", "lastname", "age"])
        with open("/home/user/pythonProject/DjangoKS/src/app1/user_data.csv", "a") as my_file:
            csvwriter = csv.writer(my_file)
            csvwriter.writerow([name, lastname, age])
        return HttpResponse("SAVED")
    else:
        template = loader.get_template("django_04.html")
        response = template.render({}, request)
        return HttpResponse(response)


def full_form(request):
    if request.method == "GET":
        return render(request, "django_06_form.html", {"form":UserForm()})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd.get("name")
            lastname = cd.get("lastname")
            age = cd.get("age")
            content = {"name": name, "lastname": lastname, "age": age}
            return render(request, "django_06_display.html", content)
        else:
            errors = form.errors
            return HttpResponse(f'errors {errors}')

