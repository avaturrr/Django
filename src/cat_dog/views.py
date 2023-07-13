from django.shortcuts import render


# Create your views here.
def catdog_home(request):
    if request.method == "GET":
        return render(request, "home_page.html")
    else:
        if "cat" in request.POST:
            content = {"url" : "https://images.dog.ceo/breeds/greyhound-italian/n02091032_6537.jpg"}
        elif "dog" in request.POST:
            content = {"url" : "https://cdn2.thecatapi.com/images/60c.jpg"}
        else:
            raise AttributeError("at home")
        return render(request, "cat.html", context = content)
