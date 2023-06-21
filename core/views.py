from django.shortcuts import render
from django.views.generic import ListView

from core.models import Card


class ShowCardView(ListView):
    model = Card
    template_name = "index.html"
    paginate_by = 6


