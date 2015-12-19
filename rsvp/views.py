from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import GuestForm, PartyForm
from django.forms.formsets import formset_factory


class RSVP(TemplateView):
    GuestFormSet = None
    party_form = PartyForm()
    template_name = 'rsvp.html'
    num_adults = 0
    num_kids = 0

    def dispatch(self, request, *args, **kwargs):
        return super(RSVP, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        GuestFormSet = formset_factory(GuestForm, extra=int(self.num_adults))
        form = PartyForm()
        GuestFormSet = formset_factory(GuestForm, extra=int(self.num_adults))
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        party_form = PartyForm(request.POST)
        self.num_adults = int(party_form.data['num_adults']) if party_form.data['num_adults'] else 0
        num_kids = int(party_form.data['num_kids']) if party_form.data['num_kids'] else 0
        GuestFormSet = formset_factory(GuestForm, extra=int(self.num_adults))

        context = {
            'num_adults': self.num_adults,
            'num_kids': self.num_kids,
            'form': party_form,
            'guestformset': GuestFormSet
        }

        return render(request, self.template_name, context)
