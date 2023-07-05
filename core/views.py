import random
import string
from django.utils import timezone

from dateutil.relativedelta import relativedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView, DeleteView, UpdateView

from CARDCONTROL.settings import Type_Purchase_Choices
from .forms import AddCardForm
from .models import Card, Purchase


class ShowCardView(ListView):
    model = Card
    template_name = "index.html"
    paginate_by = 6


class CardAddView(FormView):
    form_class = AddCardForm
    template_name = "card_add.html"
    success_url = '/'


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
            Card.objects.create(
                series=series,
                number = get_random_card_number(),
                cvv = get_random_card_cvv(),
                release_date = timezone.now(),
                end_date = create_end_date,
                funds = random.randint(1, 100000000),
                status = "Active"
            )
            return redirect(request.META['HTTP_REFERER'])


class PurchaseView(ListView):
    model = Purchase
    template_name = "purchase.html"


    def post(self,request,*args, **kwargs):
        title = request.POST.get("title")
        price = float(request.POST.get("price"))
        pk = self.kwargs.get("pk")

        Purchase.objects.create(
            title=title,
            release_date = timezone.now(),
            price=price,
            card_id=pk,

        )
        return redirect(request.META['HTTP_REFERER'])