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



    def __str__(self):
        return f"{self.series} -> {self.number}"


class Purchase(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.CharField(choices=Type_Purchase_Choices, max_length=100)
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)







