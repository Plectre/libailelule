from django import forms
from .models import Logs

""" class LogForm(forms.Form):
    appareil = forms.CharField(label="appareil", max_length=255, required=False)
    depart = forms.CharField(label="depart", max_length=255, required=False)
    retour = forms.CharField(label="retour", max_length=255, required=False)
    observations = forms.CharField(label="observations", max_length=255, required=False) """

class LogForm(forms.ModelForm):

    class Meta:
        model = Logs
        fields = ['appareil', 'depart', 'retour', 'observations']

        def __init__(self, *args, **kwargs):
            super(Logs, self).__init__(*args, **kwargs)
            self.fields['appareil'].widget.attrs.update({'class': 'form-control', 'placeholder': 'appareil'})