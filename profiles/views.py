from django.shortcuts import render

# Create your views here.


def become_member(request):
    return render(request, "auth/become-member.html")


def become_volunteer(request):
    return render(request, "auth/become-volunteer.html")