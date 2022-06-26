from django import forms
from button.static_choices import CHOICES

# define form that user will complete
class Form(forms.Form):
    # radio buttons for choices
    choice = forms.ChoiceField(
            required=True,
            widget=forms.RadioSelect(attrs={
                'class': "custom-radio-list",
                'onclick' : "ShowHideForms();",
            }
            ),
            choices=CHOICES,
        )
    other = forms.CharField(
        widget=forms.TextInput(attrs={
            'displaye': 'none',
        })
    )