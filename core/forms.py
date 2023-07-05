from django import forms

from .models import Card
class AddCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
        widgets = {
            "release_date": forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            "end_date": forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def clean_number(self):
        number1 = self.cleaned_data["number"]
        if len(str(number1)) != 16:
            raise forms.ValidationError("Not correct number")

        if Card.objects.all().filter(number = self.cleaned_data["number"], series = self.cleaned_data["series"]).exists():
            raise forms.ValidationError("Card is exists")

        return self.cleaned_data['number']



