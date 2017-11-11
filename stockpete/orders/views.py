from django.shortcuts import render, HttpResponseRedirect
from .forms import buySellForm
from stocks.models import Stock
from account.models import Account
from account.models import Portfolio
from .models import Order


# Create your views here.
def order_view(request):
    if request.method == "GET":
        form = buySellForm()
        return render(request, "orders/order.html", {"form": form})

    if request.method == "POST":
        num = int(request.POST["num"])
        type = request.POST["type"]
        stock = Stock.objects.get(pk=request.POST["stock"])
        user = request.user
        account = Account.objects.get(username=user.username)
        if type == 'BUY':
            try:
                p = Portfolio.objects.get(account=account, stock=stock)
            except Portfolio.DoesNotExist:
                p = Portfolio(account=account, stock=stock, num=0)
            p.num = p.num+num
            p.save()
            Order(stock=stock, account=account, type=type, num=num).save()
        if type == 'SELL':
            try:
                p = Portfolio.objects.get(account=account, stock=stock)
            except Portfolio.DoesNotExist:
                p = Portfolio(account=account, stock=stock, num=0)
                p.save()
            if p.num < num:
                return render(request, "orders/order.html", {"form": buySellForm(), "error": ["Insufficient stocks!"]})
            p.num = p.num-num;
            p.save()
            Order(stock=stock, account=account, type=type, num=num).save()
            if p.num == 0:
                p.delete()
        return HttpResponseRedirect('/portfolio')
