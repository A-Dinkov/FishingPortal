# Django imports
from django import forms

# Application imports
from FishingPortal.adventure.models import Adventure
from FishingPortal.business.models import Business
from FishingPortal.competition.models import Competition
from FishingPortal.picture.models import Picture


class UploadPictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = ('title', 'image', 'related_adventure', 'related_business',
                  'related_competition', 'description', 'upload_date')

        labels = {
            'title': '',
            'description': '',
            'upload_date': ''
        }

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Photo title'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter photo description'}
            ),
            'upload_date': forms.DateInput(
                attrs={'class': 'datepicker'}
            )

        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        print(user)
        super(UploadPictureForm, self).__init__(*args, **kwargs)

        if user is not None:

            if user.is_owner:
                self.fields['related_adventure'].queryset = Adventure.objects.filter(adventurer=user)
                businesses_owned_by_user = Business.objects.filter(owner=user)
                self.fields['related_competition'].queryset = Competition.objects.filter(
                    business__in=businesses_owned_by_user)
                self.fields['related_business'].queryset = Business.objects.filter(owner=user)

            else:
                del self.fields['related_business']
                self.fields['related_competition'].queryset = Competition.objects.filter(participants=user)
                self.fields['related_adventure'].queryset = Adventure.objects.filter(adventurer=user)

        else:
            pass


class PhotoEditForm(UploadPictureForm):
    class Meta(UploadPictureForm.Meta):
        model = Picture
        fields = ('title', 'description', 'upload_date')


