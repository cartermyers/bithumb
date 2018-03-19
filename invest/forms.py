from django import forms

from decimal import Decimal

class BitcoinToInGameCurrencyForm(forms.Form):
    bitcoin = forms.DecimalField(min_value=Decimal('0'), max_digits=15, decimal_places=8, \
                widget=forms.NumberInput(attrs={'name': 'price', 'id':'bitcoins', 'class':'form-control', \
                 'onkeyup': 'coinTOpts(this)', 'disabled placeholder': 'Bitcoins to spend'}))


class InGameCurrencyToBitcoinForm(forms.Form):
    in_game_currency = forms.DecimalField(min_value=Decimal('0'), max_digits=17, decimal_places=2, \
                widget=forms.NumberInput(attrs={'name': 'price', 'id':'scores', 'class':'form-control', \
                 'onkeyup': 'ptsTOcoin(this)', 'disabled placeholder': 'USD to spend'}))
