import datetime

from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
import requests

from cat_dog.forms import PetFilter
from cat_dog.models import AnimalImage
from src.settings import URL_FOR_DOGS, URL_FOR_CATS


# from src.settings import URL_FOR_CATS, URL_FOR_DOGS


# Create your views here.
def catdog_home(request):
    if request.method == "GET":
        data = {"form": PetFilter()}
        return render(request, "home_page.html", context=data)
    else:
        request.session.set_expiry(30)
        if "dog" in request.POST:
            resp_dict = requests.get(URL_FOR_DOGS).json()
            resp = resp_dict["message"]
            content = {"url": resp}
            type_im = resp.split(".")[-1]
            data_for_session = {"url": resp, "spieces": "dog", "type": type_im}
            request.session["data_for_session"] = data_for_session
            # AnimalImage.objects.create(url=resp, spieces="Cat", created_at=datetime.datetime.now(),
            #                            type=type_im)
        elif "cat" in request.POST:
            resp_list = requests.get(URL_FOR_CATS).json()
            resp_dict = resp_list[0]
            resp = resp_dict["url"]
            content = {"url": resp}
            type_im = resp.split(".")[-1]
            data_for_session = {"url": resp, "spieces": "cat", "type": type_im}
            request.session["data_for_session"] = data_for_session
            # AnimalImage.objects.create(url=resp, spieces="Dog", created_at=datetime.datetime.now(), type=type_im)
        else:
            raise AttributeError("at home")
        return render(request, "cat.html", context=content)


def save_catdog(request):
    if request.method == "POST":
        if request.method == "POST":
            data_for_writte = request.session["data_for_session"]
            AnimalImage.objects.create(url=data_for_writte["url"], spieces=data_for_writte["spieces"],
                                       created_at=datetime.datetime.now(), type=data_for_writte["type"])
            content = {"url": data_for_writte["url"]}
            return render(request, "save_cat_dog.html", context=content)


def send(request):
    url = request.POST.get("url")
    mail_for_send = request.POST.get("mail")
    send_mail(
        "Subject here",
        f"Это не фишинг {url}",
        EMAIL_HOST_USER,
        [mail_for_send],
        fail_silently=False,
    )
    return render(request, "sended_page.html", {"url": url})


def pet_filter(request):
    if request.method == "POST":
        form = PetFilter(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pets = AnimalImage.objects.filter(spieces=data.get("pet"), type=data.get("type_img"))
            return render(request, "list_pets.html", {"pets" : pets})

