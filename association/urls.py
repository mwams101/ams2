from django.urls import path, include
from . import views

urlpatterns = [
    # Association Paths

    path('association/', views.indexAssociation, name='indexAssociation'),
    path('association/addAssociation/', views.addAssociation, name='addAssociation'),
    path('association/update/<int:id>', views.updateAssociation, name='update'),
    path('association/delete/<int:id>', views.deleteAssociation, name='deleteAssociation'),
    path('association/export', views.exportExcel, name='export-excel'),

    # Association Staff Paths

    path('associationStaff/', views.indexAssociationStaff, name='indexAssociationStaff'),
    path('associationStaff/add/', views.addAssociationStaff, name='addAssociationStaff'),
    path('associationStaff/update/<int:id>', views.updateAssociationStaff, name='update'),
    path('associationStaff/delete/<int:id>', views.deleteAssociationStaff, name='deleteAssociationStaff'),

    # Memebership Paths

    path('membership/', views.indexMembership, name='indexMembership'),
    path('membership/add/', views.addMembership, name='addMembership'),
    path('membership/update/<int:id>', views.updateMembership, name='update'),
    path('membership/delete/<int:id>', views.deleteMembership, name='deleteMembership'),

    # Subscription Paths

    path('subscription/', views.indexSubscription, name='indexSubscription'),
    path('subscription/add/', views.addSubscription, name='addSubscription'),
    path('subscription/update/<int:id>', views.updateSubscription, name='update'),
    path('subscription/delete/<int:id>', views.deleteSubscription, name='deleteSubscription'),

    # Events Paths

    path('events/', views.indexEvent, name='indexEvent'),
    path('events/add/', views.addEvent, name='addEvent'),
    path('events/update/<int:id>', views.updateEvent, name='update'),
    path('events/delete/<int:id>', views.deleteEvent, name='deleteEvent'),
]
