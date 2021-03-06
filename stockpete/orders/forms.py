from django import forms
from stocks.models import Stock
from .models import Order


class buySellForm(forms.Form):
    stocks_list = Stock.objects.filter()
    stock = forms.ModelChoiceField(stocks_list, widget=forms.Select(attrs={}))
    TYPES = [
        ("BUY", "buy"),
        ("SELL", "sell")
    ]
    type = forms.ChoiceField(choices=TYPES, widget=forms.Select(attrs={}))
    num = forms.DecimalField(decimal_places=0, max_digits=5, min_value=1)
