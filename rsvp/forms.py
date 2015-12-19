from django import forms
import datetime
from .models import Meal


class PartyForm(forms.Form):
    num_adults = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": 'form-control',
                "placeholder": "12 and older",
            }))
    num_kids = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": 'form-control',
                "placeholder": "11 and younger",
            }))
    rsvp = forms.BooleanField(
        label='Can you make it?',
        widget=forms.RadioSelect(
            choices=[
                (True, "We can make it"),
                (False, "We can't make it")
            ],
            attrs={
                "class": 'radio-inline'
            }))


class GuestForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    rsvp = forms.BooleanField(
        widget=forms.Select(
            choices=[
                (True, 'Yes'),
                (False, 'No')
            ],
            attrs={
                "class": 'form-control radio-inline'
            }))
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": "Extra Details - Allergies, etc!"
    }))
    meal_choice = forms.ChoiceField(
        choices=[],
        widget=forms.Select(
            attrs={
                "class": 'form-control',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['meal_choice'].choices = [(value, value) for value in Meal.objects.all().order_by('name').values_list('name', flat=True)]
