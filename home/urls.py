from django.urls import path, include
from . import views

urlpatterns = [
    # Association Paths

    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('settings/updateSettings/<int:id>', views.updateSettings, name='updateSettings'),
    # path('page-reset-password/', views.password, name='password'),
    # # path('page-reset-password/<int:id>', views.changePassword, name='changePassword'),
]
