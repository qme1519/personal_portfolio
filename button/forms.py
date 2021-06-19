from django import forms
from button.static_choices import CHOICES

# define form that user will complete
class Form(forms.Form):
    # radio buttons for choices
    choice = forms.MultipleChoiceField(
            required=True,
            widget=forms.RadioSelect(attrs={'class': "custom-radio-list"}
            ),
            choices=CHOICES,
        )
