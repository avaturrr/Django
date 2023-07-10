from django.shortcuts import render

from school.models import Group


# Create your views here.
def all_groups(request):
    data_dict_with_groups = Group.objects.all()
    return render(request, "templ.html", context={"groups" : data_dict_with_groups})
