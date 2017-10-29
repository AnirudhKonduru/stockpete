from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .forms import RegisterForm

from persons.models import Customer
from account.models import Account
# Create your views here.


def login(request):
    if not request.method == 'POST':
        return render(request, "account/login.html")

    user = authenticate(username=request.POST["username"],
                        password=request.POST["password"])
    if user is None:
        return render(request, "account/login.html", {'message': "Invalid Credentials"})

    account = Account.objects.get(username=request.POST["username"])
    request.session["account"] = account.pk
    request.session["customer"] = account.customer.pk
    request.session["username"] = user.username

    return render(request, "account/portfolio.html")


def register(request):
    if not request.method == 'POST':
        return render(request, "account/register.html", {'form': RegisterForm})
    else:
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "account/register.html", {'form': RegisterForm, 'message': form.errors})

        user = User.objects.create_user(username=form.cleaned_data["username"],
                                        email=form.cleaned_data["email"],
                                        password=form.cleaned_data["password"])
        user.save()
        customer = Customer.objects.create(first_name=form.cleaned_data["first_name"],
                                           last_name=form.cleaned_data["last_name"],
                                           ph_num=form.cleaned_data["ph_num"],
                                           address=form.cleaned_data["address"],
                                           city=form.cleaned_data["city"],
                                           state=form.cleaned_data["state"],
                                           zip_code=form.cleaned_data["zip_code"],
                                           email="anirudh@konduru.com",
                                           )
        customer.save()
        account = Account.objects.create(username=form.cleaned_data["username"],
                                         customer=customer,
                                         card_no=form.cleaned_data["card_no"],
                                         card_exp=form.cleaned_data["card_exp"],
                                         )
        account.save()

        request.session["account"] = account.pk
        request.session["customer"] = customer.pk
        request.session["username"] = user.username
        return render(request, "account/portfolio.html")
