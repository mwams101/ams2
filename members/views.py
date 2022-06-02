from django.shortcuts import render, redirect
from .models import Club, ClubStaff
from .forms import ClubForm, ClubStaffForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template import loader
import datetime, xlwt


# Create your views here.
@login_required(login_url='/login')
def indexClub(request):
    club = Club.objects.all().values()
    template = loader.get_template("club/Club.html")

    context = {
        'club': club,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def addClub(request):
    form = ClubForm()
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexClub')

    context = {'form': form}
    return render(request, 'club/add.html', context)


@login_required(login_url='/login')
def updateClub(request, id):
    club = Club.objects.get(id=id)
    form = ClubForm(instance=club)

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('indexClub')

    context = {'form': form}
    return render(request, 'club/update.html', context)


@login_required(login_url='/login')
def deleteClub(request, id):
    club = Club.objects.get(id=id)

    if request.method == 'POST':
        club.delete()
        return redirect('indexClub')

    context = {'item': club}
    return render(request, 'club/delete.html', context)


# *************************************************************************
# Association Staff Views

@login_required(login_url='/login')
def indexClubStaff(request):
    club = ClubStaff.objects.all().values()
    template = loader.get_template("clubStaff/ClubStaff.html")

    context = {
        'club': club,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def addClubStaff(request):
    form = ClubStaffForm()
    if request.method == 'POST':
        form = ClubStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexClubStaff')

    context = {'form': form}
    return render(request, 'clubStaff/add.html', context)


@login_required(login_url='/login')
def updateClubStaff(request, id):
    club = ClubStaff.objects.get(id=id)
    form = ClubStaffForm(instance=club)

    if request.method == 'POST':
        form = ClubStaffForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('indexClubStaff')

    context = {'form': form}
    return render(request, 'clubStaff/update.html', context)


@login_required(login_url='/login')
def deleteClubStaff(request, id):
    club = ClubStaff.objects.get(id=id)

    if request.method == 'POST':
        club.delete()
        return redirect('indexClubStaff')

    context = {'item': club}
    return render(request, 'clubStaff/delete.html', context)


# *************************************************************************
# Export to excel

def exportClub(request):

    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; Filename=Clubs' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Spreadsheet')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Name', 'Address']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Club.objects.values_list('name', 'address')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response