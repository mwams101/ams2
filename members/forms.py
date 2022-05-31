from django.forms import ModelForm
from .models import Club, ClubStaff

class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'

class ClubStaffForm(ModelForm):
    class Meta:
        model = ClubStaff
        fields = '__all__'
