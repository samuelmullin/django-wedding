from django import forms
from rsvp.models import Guest, Meals, Accoms


class PartyForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    meal_preference = forms.ChoiceField(label='Meal Choice', choices=Meals.choices)
    accom_preference = forms.ChoiceField(label='Accommodation Choice', choices=Accoms.choices)

    rsvp = forms.ChoiceField(
        label='Can you make it?',
        widget=forms.RadioSelect(attrs={}),
        choices=[
            (True, "We can make it"),
            (False, "We can't make it")
        ],
    )

    class Meta:
        model = Guest
        fields = ['rsvp', 'name', 'email', 'meal_preference', 'accom_preference']


class GuestForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    meal_preference = forms.ChoiceField(label='Meal Choice', choices=Meals.choices)
    accom_preference = forms.ChoiceField(label='Accommodation Choice', choices=Accoms.choices)
    kid = forms.BooleanField(widget=forms.CheckboxInput(), label="Kid (11 and younger)")

    class Meta:
        model = Guest
        fields = ['name', 'meal_preference', 'accom_preference', 'kid']
