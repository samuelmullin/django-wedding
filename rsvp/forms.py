from django import forms
import datetime
from .models import Meal, Accommodation
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import StrictButton


class PartyForm(forms.Form):
    num_adults = forms.IntegerField(
        label="Number of Adults",
        widget=forms.NumberInput(
            attrs={
                "class": 'form-control',
                "placeholder": "12 and older",
            }))
    num_kids = forms.IntegerField(
        label="Number of Kids (under 12)",
        widget=forms.NumberInput(
            attrs={
                "class": 'form-control',
                "placeholder": "11 and younger",
            }))
    rsvp = forms.ChoiceField(
        label='Can you make it?',
        widget=forms.RadioSelect(
        attrs={
            "class": 'form-control radio-inline'
        }),
        choices=[
            (True, "We can make it"),
            (False, "We can't make it")
        ],
        )

    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'form-control col-sm-2 col-md-2 col-lg-2'
        self.helper.field_class = 'form-control col-sm-8 col-md-8 col-lg-8'
        self.helper.layout = Layout(
            'num_adults',
            'num_kids',
            'rsvp',
            Submit('submit', 'Next', css_class='btn-default'),
        )


class GuestForm(forms.Form):
    first_name = forms.CharField(
        label='First Name'
    )
    last_name = forms.CharField(
        label='Last Name'
    )
    email = forms.EmailField(
        label='Email'
    )
    phone = forms.CharField(
        label='Phone Number'
    )
    rsvp = forms.BooleanField(
        label='Can you Make it?',
        widget=forms.Select(
            choices=[
                (True, 'Yes'),
                (False, 'No')
            ],
            attrs={
                "class": 'form-control radio-inline'
            }))
    text = forms.CharField(
        label='Comments',
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": "Extra Details - Allergies, etc!"
            }))
    meal_choice = forms.ChoiceField(
        label='Meal Choice',
        choices=[],
        widget=forms.Select(
            attrs={
                "class": 'form-control',
            }))

    accom_choice = forms.ChoiceField(
        label='Accommodation Choice',
        choices=[],
        widget=forms.Select(
            attrs={
                "class": 'form-control',
            }))

    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        self.fields['meal_choice'].choices = [(value, value) for value in Meal.objects.all().order_by('name').values_list('name', flat=True)]
        self.fields['accom_choice'].choices = [(value, value) for value in Accommodation.objects.all().order_by('name').values_list('name', flat=True)]
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'form-control col-sm-2'
        self.helper.field_class = 'form-control col-sm-8'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            'phone',
            'rsvp',
            'meal_choice',
            'accom_choice',
            StrictButton('Submit', css_class='btn-default'),
        )
