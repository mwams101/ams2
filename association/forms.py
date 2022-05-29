from django.forms import ModelForm
from .models import Association, AssociationStaff, Event, Subscription, Membership


class AssociationForm(ModelForm):
    class Meta:
        model = Association
        fields = '__all__'


class AssociationStaffForm(ModelForm):
    class Meta:
        model = AssociationStaff
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'
