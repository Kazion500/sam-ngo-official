from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
from sam.models import Profile
from sam.forms import ProfileModelForm


def home(request):
    if request.method == "POST":
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            EMAIL_TEMPLATE = f'Hi {form.data["first_name"]}, \nThank your for Registering with us \nFeel free to contact us at info@sam-group.com'

            send_mail(
                subject='Registration Success!!',
                message=EMAIL_TEMPLATE,
                from_email=f'sam-group.com <{settings.EMAIL_HOST_USER}>',
                recipient_list=[form.data["email"]],
                fail_silently=True,
            )
            user = form.save(commit=False)
            user_auth = authenticate(
                request, username=user.email, password=user.password)
            user.save()
            if user_auth == None:
                login(request, user)
                messages.success(request, "Thank you for registering!!")
                return redirect("home")
        else:
            messages.error(
                request, "Oops!! Sorry we couldn't create your account")

    else:
        form = ProfileModelForm()

    context = {
        "form": form
    }
    return render(request, "main/index.html", context)


def log_in(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_auth = authenticate(request, username=email, password=password)

        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, "Thank you for registering!!")
            return redirect("home")

        messages.error(request, "Oops!! Sorry we couldn't create your account")
        return redirect("home")
    return render(request, "main/index.html")


def log_out(request):
    logout(request)
    return redirect("home")
