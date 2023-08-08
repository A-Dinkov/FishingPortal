from django import forms
from .models import Competition
from ..business.models import Business


class CompetitionCreationForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(CompetitionCreationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['business'].queryset = Business.objects.filter(owner=user)

    business = forms.ModelChoiceField(queryset=Business.objects.none())  # Set an empty default queryset

    class Meta:
        model = Competition
        fields = ('name', 'place', 'date', 'business', 'description')

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
                attrs={'placeholder': 'Additional info', 'rows': 5, 'cols': 40}
            ),


        }


