from django.urls import path, include
from . import views

urlpatterns = [
    # Association Paths

    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('settings/updateSettings/<int:id>', views.updateSettings, name='updateSettings'),
    # path('association/delete/<int:id>', views.deleteAssociation, name='delete'),
]