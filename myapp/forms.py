from .models import Position
from .models import student,Position
from django import forms

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'


class Positionform(forms.ModelForm):
    class Meta:
        model=Position
        fields='__all__'