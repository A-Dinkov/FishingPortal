from django import forms
from FishingPortal.adventure.models import Adventure


class AdventureCreationForm(forms.ModelForm):
    class Meta:
        model = Adventure
        fields = ('name', 'place', 'date', 'description')

        labels = {
            'name': '',
            'place': '',
            'date': '',
            'description': ''
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Name your adventure'}
            ),

            'place': forms.TextInput(
                attrs={'placeholder': 'Insert place'}
            ),

            'date': forms.DateTimeInput(
                attrs={'placeholder': 'Insert date', 'class': 'datepicker'}
            ),

            'description': forms.Textarea(
                attrs={'placeholder': 'Describe your adventure'}
            ),
        }


class AdventureEditForm(AdventureCreationForm):
    pass
