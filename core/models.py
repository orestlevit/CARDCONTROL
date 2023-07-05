from django.db import models

from CARDCONTROL.settings import StatusChoices, Type_Purchase_Choices


class Card(models.Model):
    series = models.CharField(max_length=100)
    number = models.PositiveBigIntegerField()
    release_date = models.DateTimeField()
    end_date = models.DateTimeField()
    cvv = models.IntegerField()
    funds = models.IntegerField()
    status = models.CharField( choices=StatusChoices, blank=True, max_length=20)


class Purchase(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    price = models.FloatField()
    card = models.ForeignKey("Card", on_delete=models.CASCADE)







