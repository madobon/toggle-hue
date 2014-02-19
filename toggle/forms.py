from django import forms
from toggle.models import Hueee

class HueeeForm(forms.ModelForm):
    class Meta:
        model = Hueee

    def __init__(self, *args, **kwargs):
        super(HueeeForm, self).__init__(*args, **kwargs)
        # something