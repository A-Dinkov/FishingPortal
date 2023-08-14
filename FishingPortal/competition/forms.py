# Django imports
from django import forms

# Application imports
from FishingPortal.business.models import Business
from FishingPortal.competition.models import Competition


class CompetitionCreationForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(CompetitionCreationForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['business'].queryset = Business.objects.filter(owner=user)

    business = forms.ModelChoiceField(queryset=Business.objects.none())

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


class CompetitionEditForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('date', 'description',)

