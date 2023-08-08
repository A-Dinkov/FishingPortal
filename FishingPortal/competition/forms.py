from django import forms

from .models import Competition


class CompetitionCreationForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ('name', 'place', 'date', 'description')

        labels = {
            'name': '',
            'place': '',
            'date': '',
            'description': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Name competition'}
            ),

            'place': forms.TextInput(
                attrs={'placeholder': 'Location to take place'}
            ),

            'date': forms.DateTimeInput(
                attrs={'placeholder': 'Set a date', 'class': 'datepicker'}
            ),

            'description': forms.Textarea(
                attrs={'placeholder': 'Additional info'}
            ),

        }
