from django.urls import path, include
from . import views

urlpatterns = [
    # Club Paths

    path('club/', views.indexClub, name='indexClub'),
    path('club/add/', views.addClub, name='addClub'),
    path('club/update/<int:id>', views.updateClub, name='updateClub'),
    path('club/delete/<int:id>', views.deleteClub, name='deleteClub'),
    path('club/export', views.exportClub, name='export-club'),

    # Club Staff Paths

    path('clubStaff/', views.indexClubStaff, name='indexClubStaff'),
    path('clubStaff/add/', views.addClubStaff, name='addClubStaff'),
    path('clubStaff/update/<int:id>', views.updateClubStaff, name='updateClubStaff'),
    path('clubStaff/delete/<int:id>', views.deleteClubStaff, name='deleteClubStaff'),
]