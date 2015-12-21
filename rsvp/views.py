from django.shortcuts import render
from django.views.generic import TemplateView
from django.forms.formsets import formset_factory

from .forms import PartyForm
from rsvp.forms import GuestForm


class RSVP(TemplateView):
    template_name = 'rsvp.html'

    def get(self, request, *args, **kwargs):
        defualt_guests = 1
        max = 10

        party_form = PartyForm()
        GuestFormset = formset_factory(GuestForm, extra=defualt_guests, max_num=max)
        guest_formset = GuestFormset()

        context = {
            'party_form': party_form,
            'guest_formset': guest_formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        party_form = PartyForm(request.POST)
        GuestFormset = formset_factory(GuestForm)
        guest_formset = GuestFormset(request.POST)
        guest_contact = None

        if party_form.is_valid() and guest_formset.is_valid:
            # party form Guest will be the contact for all other guests created here.
            pass

        context = {
            'party_form': party_form,
            'guest_formset': guest_formset,
        }
        return render(request, self.template_name, context)
