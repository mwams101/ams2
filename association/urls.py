from django.urls import path, include
from . import views

urlpatterns = [
    # Association Paths

    path('association/', views.indexAssociation, name='indexAssociation'),
    path('association/addAssociation/', views.addAssociation, name=' '),
    path('association/update/<int:id>', views.updateAssociation, name='update'),
    path('association/delete/<int:id>', views.deleteAssociation, name='delete'),

    # Association Staff Paths

    path('associationStaff/', views.indexAssociationStaff, name='indexAssociationStaff'),
    path('associationStaff/add/', views.addAssociationStaff, name=' '),
    path('associationStaff/update/<int:id>', views.updateAssociationStaff, name='update'),
    path('associationStaff/delete/<int:id>', views.deleteAssociationStaff, name='delete'),

    # Memebership Paths

    path('membership/', views.indexMembership, name='indexMembership'),
    path('membership/add/', views.addMembership, name=' '),
    path('membership/update/<int:id>', views.updateMembership, name='update'),
    path('membership/delete/<int:id>', views.deleteMembership, name='delete'),

    # Subscription Paths

    path('subscription/', views.indexSubscription, name='indexSubscription'),
    path('subscription/add/', views.addSubscription, name=' '),
    path('subscription/update/<int:id>', views.updateSubscription, name='update'),
    path('subscription/delete/<int:id>', views.deleteSubscription, name='delete'),

    # Events Paths

    path('events/', views.indexEvent, name='indexEvent'),
    path('events/add/', views.addEvent, name=' '),
    path('events/update/<int:id>', views.updateEvent, name='update'),
    path('events/delete/<int:id>', views.deleteEvent, name='delete'),
]
