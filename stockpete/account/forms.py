from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    ph_num = forms.CharField(max_length=10)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=20)
    state = forms.CharField(max_length=20)
    zip_code = forms.DecimalField(decimal_places=0, max_digits=6)

    card_no = forms.CharField(max_length=16)
    card_exp = forms.DateField()

    email = forms.CharField(max_length=50)
