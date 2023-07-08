import random
import string
from django.utils import timezone

from dateutil.relativedelta import relativedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView, DeleteView, UpdateView

from CARDCONTROL.settings import Type_Purchase_Choices, StatusChoices
from .forms import AddCardForm, PurchaseForm
from .models import Card, Purchase


class ShowCardView(ListView):
    model = Card
    template_name = "index.html"
    paginate_by = 6


class CardAddView(FormView):
    form_class = AddCardForm
    template_name = "card_add.html"
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        context = self.get_context_data()
        form = self.get_form(form_class)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("/")

        return self.render_to_response(context)


class DetailCardView(DetailView):
    model = Card
    template_name = "detail_card.html"

    def post(self, request, pk):
        obj = Card.objects.get(id=pk)
        if obj.status.lower() == "active":
            obj.status = "Inactive"
        elif obj.status.lower() == "inactive":
            obj.status = "Active"

        obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CardDeleteView(DeleteView):
    model = Card
    template_name = 'card_delete.html'
    success_url = "/"


class CardEditView(UpdateView):
    model = Card
    template_name = 'edit_card.html'
    success_url = '/'
    fields = "__all__"


def get_random_card_number():
    number = ""
    for i in range(4):
        number += "".join(random.sample(string.digits, 4))

    return int(number)


def get_random_card_cvv():
    cvv = ""
    cvv += "".join(random.sample(string.digits, 3))
    return int(cvv)


class CardGenerationView(ListView):
    model = Card
    template_name = "generation.html"

    def post(self, request):
        series = request.POST.get("series")
        count = int(request.POST.get("count"))
        period = int(request.POST.get("period"))
        year_or_month = request.POST.get("rad")


        create_end_date = timezone.now() + relativedelta(months=1)

        if year_or_month.lower() == "month":
            create_end_date = timezone.now() + relativedelta(months=period)

        elif year_or_month.lower() == "year":
            create_end_date = timezone.now() + relativedelta(years=period)




        for iterator in range(count):
            print(count)
            Card.objects.create(
                series=series,
                number = get_random_card_number(),
                cvv = get_random_card_cvv(),
                release_date = timezone.now(),
                end_date = create_end_date,
                funds = random.randint(1, 10000),
                status = StatusChoices[0][0]
            )
            return redirect("/")


class PurchaseView(FormView):
    form_class = PurchaseForm
    template_name = "purchase.html"
    success_url = '/'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



