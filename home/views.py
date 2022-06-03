from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from association.models import *
from members.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import Group
from authentication.forms import SignUpForm
from django.shortcuts import render

@login_required(login_url="/login/")
def index(request):

    context = {'segment': 'index'}

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dashboard(request):

    users = User.objects.all()
    total_users = users.count()
    events = Event.objects.all()
    total_events = Event.objects.count()
    association = Association.objects.all()
    total_associations = association.count()
    clubs = Club.objects.all()
    clubstaff = ClubStaff.objects.all()
    total_clubs = clubs.count()
    total_clubstaff = clubstaff.count()

    context = {'segment': 'dashboard',
               'association': association,
               'clubs': clubs,
               'clubstaff': clubstaff,
               'events': events,
               'total_events': total_events,
               'total_associations': total_associations,
               'total_clubs': total_clubs,
               'total_clubstaff': total_clubstaff,
               'total_users': total_users,
    }

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def settings(request):
    context = {'segment': 'settings'}

    html_template = loader.get_template('home/settings.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def updateSettings(request, id):

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']

    users = User.objects.get(id=id)
    users.first_name = first_name
    users.last_name = last_name
    users.username = username
    users.email = email
    users.save()
    return HttpResponseRedirect(reverse('settings'))


def addUser(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            group = Group.objects.get(name='members')
            user.groups.add(group)
            msg = 'User created'
            success = True

            # return redirect("/login/")

        else:
            msg = '<p style="color:red;">Form is not valid</p>'
    else:
        form = SignUpForm()

    return render(request, "home/add-user.html", {"form": form, "msg": msg, "success": success})
