from django import forms
from rsvp.models import Guest


class PartyForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')

    rsvp = forms.ChoiceField(
        label='Can you make it?',
        widget=forms.RadioSelect(attrs={}),
        choices=[
            (True, "We can make it"),
            (False, "We can't make it")
        ],
    )

    num_adults = forms.IntegerField(
        label="How many adults?",
        widget=forms.NumberInput(
            attrs={
                "class": 'form-control',
                "placeholder": "12 and older",
            }))

    num_kids = forms.IntegerField(
        label="How many Kids? (under 12)",
        widget=forms.NumberInput(
            attrs={
                "class": 'form-control',
                "placeholder": "11 and younger",
            }))

    class Meta:
        model = Guest
        fields = ['rsvp', 'name', 'email', 'meal_preference', 'accom_preference']


class AdultForm(forms.ModelForm):

    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number')

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

    text = forms.CharField(
        label='Comments',
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": "Extra Details - Allergies, etc!"
            }))

    class Meta:
        model = Guest
        fields = ['name', 'meal_choice',]


class KidForm(forms.Form):
    name = forms.CharField(label='Name')

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

    text = forms.CharField(
        label='Comments',
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": "Extra Details - Allergies, etc!"
            }))

    class Meta:
        model = Guest
        fields = ['name', 'meal_choice', 'accom_choice', 'text']
