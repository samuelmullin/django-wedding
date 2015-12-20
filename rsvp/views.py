from django.shortcuts import render
from django.views.generic import TemplateView
from django.forms.formsets import formset_factory

from .forms import AdultForm, PartyForm
from rsvp.forms import KidForm


class RSVP(TemplateView):
    template_name = 'rsvp.html'

    def get(self, request, *args, **kwargs):
        defualt_adults = 1
        defualt_kids = 1
        max = 10

        party_form = PartyForm()

        AdultFormSet = formset_factory(AdultForm, extra=defualt_adults, max_num=max)
        adults_formset = AdultFormSet()

        KidsFormSet = formset_factory(KidForm, extra=defualt_kids, max_num=max)
        kids_formset = KidsFormSet()

        context = {
            'party_form': party_form,
            'adults_formset': adults_formset,
            'kids_formset': kids_formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        party_form = PartyForm(request.POST)
        AdultFormSet = formset_factory(AdultForm)
        adult_formset = AdultFormSet(request.POST)
        KidsFormSet = formset_factory(KidForm)
        kid_formset = KidsFormSet(request.POST)
        guest_contact = None
        if party_form.is_valid() and adult_formset.is_valid and kid_formset.is_valid():
            # party form Guest will be the contact for all other guests created here.
            pass

        context = {
            'party_form': party_form,
            'adults_formset': AdultFormSet,
            'kids_formset': KidsFormSet,
        }
        return render(request, self.template_name, context)
