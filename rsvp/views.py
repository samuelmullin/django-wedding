from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import GuestForm, PartyForm
from django.forms.formsets import formset_factory


class RSVP(TemplateView):
    GuestFormSet = None
    partyform = PartyForm()
    template_name = 'rsvp.html'
    num_adults = 0
    num_kids = 0

    def dispatch(self, request, *args, **kwargs):
        return super(RSVP, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.GuestFormSet = formset_factory(GuestForm, extra=int(self.num_adults))
        context = {
            'partyform': self.partyform,
            'guestformset': self.GuestFormSet,
            'num_adults': self.num_adults,
            'num_kids': self.num_kids,
        }
        print context
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.party_form = PartyForm(request.POST)
        if self.party_form.is_valid():
            self.num_adults = int(self.party_form.data['num_adults']) if self.party_form.data['num_adults'] else 0
            self.num_kids = int(self.party_form.data['num_kids']) if self.party_form.data['num_kids'] else 0
            self.GuestFormSet = formset_factory(GuestForm, extra=int(self.num_adults))

        context = {
            'num_adults': self.num_adults,
            'num_kids': self.num_kids,
            'partyform': self.party_form,
            'guestformset': self.GuestFormSet
        }
        print context

        return render(request, self.template_name, context)
