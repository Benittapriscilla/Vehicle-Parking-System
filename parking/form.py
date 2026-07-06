from django import forms
from .models import Parking

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields='__all__'