from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django import template
from .forms import RegisterForm, LoginForm, AccountForm
from persons.models import Customer
from account.models import Account, Portfolio
from stocks.models import Stock
# Create your views here.


def index(request):
    return render(request, 'static/base.html')


def login_view(request):
    if not request.method == 'POST':
        return render(request, "account/login.html", {'form': LoginForm})

    user = authenticate(username=request.POST.get("username"),
                        password=request.POST.get("password"))
    if user is None or user.is_anonymous():
        return render(request, "account/login.html", {'form': LoginForm,
                                                      'error': ["Invalid Credentials"],
                                                      'info': ["Username \""+request.POST.get("username")
                                                               + "\" or the password is invalid"],
                                                      }
                      )

    login(request, user)

    account = Account.objects.get(user=request.user)
    request.session["account"] = account.pk
    request.session["customer"] = account.customer.pk
    request.session["username"] = user.username
    return HttpResponseRedirect("/portfolio")


def register_view(request):
    form = RegisterForm()
    if not request.method == 'POST':
        return render(request, "account/register.html", {'form': form})
    else:
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "account/register.html", {'form': form, 'error':form.errors})

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
        account = Account.objects.create(user=user,
                                         customer=customer,
                                         card_no=form.cleaned_data["card_no"],
                                         card_exp=form.cleaned_data["card_exp"],
                                         )
        account.save()

        request.session["account"] = account.pk
        request.session["customer"] = customer.pk
        request.session["username"] = user.username
        return HttpResponseRedirect("/login", {"message": "Registered Successfully. Login to continue"})


def account_view(request):
    user = request.user
    if user.is_anonymous or user is None:
        HttpResponseRedirect("/login")

    account = Account.objects.get(pk=request.session["account"])
    customer = account.customer

    form = AccountForm(data={
        **user.__dict__,
        **account.__dict__,
        **customer.__dict__,
        **{"username": user.username},
        **{"password": "--------"}
    })

    if not request.method == 'POST':
        return render(request, "account/account.html", {'form': form})
    else:
        form = AccountForm(request.POST)
        if not form.is_valid():
            return render(request, "account/account.html", {'form': form, 'error': list(form.errors)})
        user = request.user
        account = Account.objects.get(user=user)
        customer = Customer.objects.get(account=account)

        user.username = form.cleaned_data["username"]
        user.email = form.cleaned_data["email"]
        if form.cleaned_data["password"] is not None and form.cleaned_data["password"] != "":
            user.set_password(form.cleaned_data["password"])
        user.save()

        customer.first_name = form.cleaned_data["first_name"]
        customer.last_name = form.cleaned_data["last_name"]
        customer.ph_num = form.cleaned_data["ph_num"]
        customer.address = form.cleaned_data["address"]
        customer.city = form.cleaned_data["city"]
        customer.state = form.cleaned_data["state"]
        customer.zip_code = form.cleaned_data["zip_code"]
        customer.email = form.cleaned_data["email"]
        customer.save()

        account.user=user
        account.customer=customer
        account.card_no=form.cleaned_data["card_no"]
        account.card_exp=form.cleaned_data["card_exp"]
        account.save()

        request.session["account"] = account.pk
        request.session["customer"] = customer.pk
        request.session["username"] = user.username
        return HttpResponseRedirect("/portfolio", {"message": "Account Details modified successfully"})



regis = template.Library()


def mult(value, arg):
    """Multiplies the arg and the value"""
    return int(value) * int(arg)


regis.filter('mult', mult)


#@login_required(login_url="/login/")

def portfolio_view(request):
    if request.user.is_authenticated:
        #return render(request, "account/login.html", {"message": str(dict(request.session))+str(request.user)})
        account = Account.objects.get(pk=request.session["account"])
        try:
            own_portfolio = Portfolio.objects.filter(~Q(num=0), account=account)

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
