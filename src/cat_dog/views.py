from django.shortcuts import render
import requests


# Create your views here.
def catdog_home(request):
    if request.method == "GET":
        return render(request, "home_page.html")
    else:
        if "dog" in request.POST:
            resp_dict = requests.get("https://dog.ceo/api/breeds/image/random").json()
            resp = resp_dict["message"]
            content = {"url" : resp}
        elif "cat" in request.POST:
            resp_list = requests.get("https://api.thecatapi.com/v1/images/search").json()
            resp_dict = resp_list[0]
            resp = resp_dict["url"]
            content = {"url" : resp}
        else:
            raise AttributeError("at home")
        return render(request, "cat.html", context = content)
