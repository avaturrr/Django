from django.shortcuts import render

from school.models import Group, Student


# Create your views here.
def all_groups(request):
    data_dict_with_groups = Group.objects.all()
    return render(request, "templ.html", context={"groups": data_dict_with_groups})


def all_students_of_group(request, group_id):
    group = Group.objects.get(id=group_id)
    gr_students = Student.objects.filter(group_id=group_id)
    return render(request, "list_st.html", context={"students" : gr_students, 'group': group})
