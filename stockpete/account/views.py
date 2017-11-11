from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django import template
from .forms import RegisterForm, LoginForm

from persons.models import Customer
from account.models import Account, Portfolio
from stocks.models import Stock
# Create your views here.


def index(request):
    return render(request, 'static/auth_base.html')


def login_view(request):
    if not request.method == 'POST':
        return render(request, "account/login.html", {'form': LoginForm})

    user = authenticate(username=request.POST.get("username"),
                        password=request.POST.get("password"))
    if user is None:
        return render(request, "account/login.html", {'form': LoginForm,
                                                      'message': "Invalid Credentials"
                                                                 + request.POST.get("username")
                                                                 + request.POST.get("password")
                                                      }
                      )

    account = Account.objects.get(username=request.POST["username"])
    request.session["account"] = account.pk
    request.session["customer"] = account.customer.pk
    request.session["username"] = user.username
    login(request, user)
    return HttpResponseRedirect("/portfolio")


def register_view(request):
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
        login(request, user)
        customer = Customer.objects.create(first_name=form.cleaned_data["first_name"],
                                           last_name=form.cleaned_data["last_name"],
                                           ph_num=form.cleaned_data["ph_num"],
                                           address=form.cleaned_data["address"],
                                           city=form.cleaned_data["city"],
                                           state=form.cleaned_data["state"],
                                           zip_code=form.cleaned_data["zip_code"],
                                           email=form.cleaned_data["email"],
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
        return HttpResponseRedirect("/login", {"message": "Registered Successfully. Login to continue"})


regis = template.Library()


def mult(value, arg):
    """Multiplies the arg and the value"""
    return int(value) * int(arg)


regis.filter('mult', mult)


#@login_required(login_url="/login/")

def portfolio_view(request):
    if request.user.is_authenticated:
        #return render(request, "account/login.html", {"message": str(dict(request.session).for )+str(request.user)})
        account = Account.objects.get(pk=request.session["account"])
        try:
            own_portfolio = Portfolio.objects.filter(account=account)
        except Portfolio.DoesNotExist:
            own_portfolio = []
        try:
            stocks = Stock.objects.filter()
        except Stock.DoesNotExist:
            stocks = []
        return render(request, "account/portfolio.html", {"portfolio": own_portfolio, "stocks": stocks})
    else:
        return HttpResponseRedirect("/login", {"message": "Not logged in. Please Login to Continue"})


def thankView(request):
    return render(request, "account/Thanks.html")
