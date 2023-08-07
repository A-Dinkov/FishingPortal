from django import forms

from FishingPortal.business.models import Business


class BusinessCreationForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ('lake_name', 'city', 'coordinates', 'location', 'description', 'business_images')

        labels = {
            'lake_name': '',
            'city': '',
            'coordinates': '',
            'location': '',
            'description': '',
        }

        widgets = {
            'lake_name': forms.TextInput(
                attrs={
                    'placeholder': 'Name of your business(lake)'
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Name of the city/village or the one nearby'
                }
            ),

            'coordinates': forms.TextInput(
                attrs={
                    'placeholder': 'Enter coordinates in format: 41.40338, 2.17403'
                }
            ),

            'location': forms.Textarea(
                attrs={
                    'rows': 5,
                    'cols': 40,
                    'placeholder': 'Enter the location of the business. Make it easy for customer to reach you.'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'rows': 5,
                    'cols': 40,
                    'placeholder': 'Shortly describe type of fishing. General requirements. '
                                   'Additional services provided'
                }
            ),

        }
