from django.shortcuts import render, redirect
from .models import Association, AssociationStaff, Subscription, Membership, Event
from .forms import AssociationForm, AssociationStaffForm, SubscriptionForm, MembershipForm, EventForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template import loader
import datetime, xlwt
from authentication.decorator import allowed_user


# Create your views here.
@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
def indexAssociation(request):
    association = Association.objects.all().values()
    template = loader.get_template("association/Association.html")

    context = {
        'association': association,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
def addAssociation(request):
    form = AssociationForm()
    if request.method == 'POST':
        form = AssociationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexAssociation')

    context = {'form': form}
    return render(request, 'association/addAssociation.html', context)


@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
def updateAssociation(request, id):
    association = Association.objects.get(id=id)
    form = AssociationForm(instance=association)

    if request.method == 'POST':
        form = AssociationForm(request.POST, instance=association)
        if form.is_valid():
            form.save()
            return redirect('indexAssociation')

    context = {'form': form}
    return render(request, 'association/addAssociation.html', context)


@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
def deleteAssociation(request, id):
    association = Association.objects.get(id=id)

    if request.method == 'POST':
        association.delete()
        return redirect('indexAssociation')

    context = {'item': association}
    return render(request, 'association/delete.html', context)


# *************************************************************************
# Association Staff Views

@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
def indexAssociationStaff(request):
    association = AssociationStaff.objects.all().values()
    template = loader.get_template("associationStaff/AssociationStaff.html")

    context = {
        'association': association,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
def indexMembership(request):
    membership = Membership.objects.all().values()
    template = loader.get_template("membership/Membership.html")

    context = {
        'membership': membership,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
def indexSubscription(request):
    subscription = Subscription.objects.all().values()
    template = loader.get_template("subscription/Subscription.html")

    context = {
        'subscription': subscription,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
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
@allowed_user(allowed_roles=['admin'])
def deleteEvent(request, id):
    event = Event.objects.get(id=id)

    if request.method == 'POST':
        event.delete()
        return redirect('indexEvent')

    context = {'item': event}
    return render(request, 'events/delete.html', context)

######################################################################################
# Export to Excel

def exportExcel(request):

    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; Filename=Associations' + \
        str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Spreadsheet')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Name', 'Type', 'Headquarters']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Association.objects.values_list('name', 'type', 'headquarters')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response



