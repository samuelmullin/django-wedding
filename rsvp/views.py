from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
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

        if party_form.is_valid() and guest_formset.is_valid():
            # party form Guest will be the contact for all other guests created here.
            guest_contact = party_form.save()
            for form in guest_formset:
                instance = form.instance
                instance.party = guest_contact
                instance.save()

            messages.add_message(request, messages.SUCCESS, 'Thank you for RSVPing {}.'.format(guest_contact.name))
            return redirect(reverse('thank-you'))

        context = {
            'party_form': party_form,
            'guest_formset': guest_formset,
        }
        return render(request, self.template_name, context)


class RSVPComplete(TemplateView):
    template_name = 'thank-you.html'

