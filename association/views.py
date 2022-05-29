from django.shortcuts import render, redirect
from .models import Association, AssociationStaff, Subscription, Membership, Event
from .forms import AssociationForm, AssociationStaffForm, SubscriptionForm, MembershipForm, EventForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template import loader


# Create your views here.
@login_required(login_url='/login')
def indexAssociation(request):
    association = Association.objects.all().values()
    template = loader.get_template("association/Association.html")

    context = {
        'association': association,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def addAssociation(request):
    form = AssociationForm()
    if request.method == 'POST':
        form = AssociationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'association/addAssociation.html', context)


@login_required(login_url='/login')
def updateAssociation(request, id):
    association = Association.objects.get(id=id)
    form = AssociationForm(instance=association)

    if request.method == 'POST':
        form = AssociationForm(request.POST, instance=association)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'association/addAssociation.html', context)


@login_required(login_url='/login')
def deleteAssociation(request, id):
    association = Association.objects.get(id=id)

    if request.method == 'POST':
        association.delete()
        return redirect('index')

    context = {'item': association}
    return render(request, 'association/delete.html', context)


# *************************************************************************
# Association Staff Views

@login_required(login_url='/login')
def indexAssociationStaff(request):
    association = AssociationStaff.objects.all().values()
    template = loader.get_template("associationStaff/AssociationStaff.html")

    context = {
        'association': association,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def addAssociationStaff(request):
    form = AssociationStaffForm()
    if request.method == 'POST':
        form = AssociationStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexAssociationStaff')

    context = {'form': form}
    return render(request, 'associationStaff/add.html', context)


@login_required(login_url='/login')
def updateAssociationStaff(request, id):
    association = AssociationStaff.objects.get(id=id)
    form = AssociationStaffForm(instance=association)

    if request.method == 'POST':
        form = AssociationStaffForm(request.POST, instance=association)
        if form.is_valid():
            form.save()
            return redirect('indexAssociationStaff')

    context = {'form': form}
    return render(request, 'associationStaff/update.html', context)


@login_required(login_url='/login')
def deleteAssociationStaff(request, id):
    association = AssociationStaff.objects.get(id=id)

    if request.method == 'POST':
        association.delete()
        return redirect('indexAssociationStaff')

    context = {'item': association}
    return render(request, 'associationStaff/delete.html', context)


# *************************************************************************
# Membership Views

@login_required(login_url='/login')
def indexMembership(request):
    membership = Membership.objects.all().values()
    template = loader.get_template("membership/Membership.html")

    context = {
        'membership': membership,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def addMembership(request):
    form = MembershipForm()
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexMembership')

    context = {'form': form}
    return render(request, 'membership/add.html', context)


@login_required(login_url='/login')
def updateMembership(request, id):
    membership = Membership.objects.get(id=id)
    form = MembershipForm(instance=membership)

    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            return redirect('indexMembership')

    context = {'form': form}
    return render(request, 'membership/update.html', context)


@login_required(login_url='/login')
def deleteMembership(request, id):
    membership = Membership.objects.get(id=id)

    if request.method == 'POST':
        membership.delete()
        return redirect('indexMembership')

    context = {'item': membership}
    return render(request, 'membership/delete.html', context)


# *************************************************************************
# Subscription Views

@login_required(login_url='/login')
def indexSubscription(request):
    subscription = Subscription.objects.all().values()
    template = loader.get_template("mubscription/Subscription.html")

    context = {
        'subscription': subscription,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def addSubscription(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexSubscription')

    context = {'form': form}
    return render(request, 'subscription/add.html', context)


@login_required(login_url='/login')
def updateSubscription(request, id):
    subscription = Subscription.objects.get(id=id)
    form = SubscriptionForm(instance=subscription)

    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('indexSubscription')

    context = {'form': form}
    return render(request, 'subscription/update.html', context)


@login_required(login_url='/login')
def deleteSubscription(request, id):
    subscription = Subscription.objects.get(id=id)

    if request.method == 'POST':
        subscription.delete()
        return redirect('indexSubscription')

    context = {'item': subscription}
    return render(request, 'subscription/delete.html', context)


# *************************************************************************
# Event Views

@login_required(login_url='/login')
def indexEvent(request):
    event = Event.objects.all().values()
    template = loader.get_template("events/Event.html")

    context = {
        'event': event,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def addEvent(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexEvent')

    context = {'form': form}
    return render(request, 'events/add.html', context)


@login_required(login_url='/login')
def updateEvent(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('indexEvent')

    context = {'form': form}
    return render(request, 'events/update.html', context)


@login_required(login_url='/login')
def deleteEvent(request, id):
    event = Event.objects.get(id=id)

    if request.method == 'POST':
        event.delete()
        return redirect('indexEvent')

    context = {'item': event}
    return render(request, 'events/delete.html', context)
