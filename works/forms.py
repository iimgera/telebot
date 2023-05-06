from django import forms
from works.models import Appeal


class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = (
            'name',
            'email',
            'message',
        )
