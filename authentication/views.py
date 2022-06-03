from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                msg = '<p style="color:red">Invalid credentials</p>'
        else:
            msg = '<p style="color: red ;">Error validating the form</p>'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='admin')
            user.groups.add(group)

            msg = 'User created - please <a href="/login" style="color:red;">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = '<p style="color:red;">Form is not valid</p>'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
