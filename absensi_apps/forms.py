from django import forms


from .models import Scan


class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan

        fields = ('peserta',)
        # widgets = {
        #     'peserta': forms.TextInput(attrs={
        #         'class': 'form-control', 'disabled': 'disabled',
        #         'id': 'staticEmail'
        #     }),
        # }
