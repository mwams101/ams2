from django.contrib import admin
from .models import Association, AssociationStaff, Event, Subscription, Membership

admin.site.register(Association)
admin.site.register(AssociationStaff)
admin.site.register(Membership)
admin.site.register(Subscription)
admin.site.register(Event)
