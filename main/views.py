from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.utils.text import slugify

# libraries
import yfinance as yf
from stocksymbol import StockSymbol

def get_stocks():
    # api configuration
    api_key = 'b5db84e9-5263-4f11-a426-326033fd1751'
    ss = StockSymbol(api_key)

    # get all stocks of US market
    all_stocks = ss.get_symbol_list(market="US")

    # get first 10 stocks
    i = 0
    stocks = []
    while i < 10:
        stocks.append(all_stocks[i])
        i += 1

    # append am ID to each stock object
    i = 0
    for stock in stocks:
        stock['id'] = i
        stock['slug'] = slugify(stock['symbol'])
        i += 1

    return stocks

def index(request):

    # passing information into the view
    context = {
        'stocks' : get_stocks(),
    }

    return render(request, 'main/index.html', context)

def stock(request, stock_slug):
    
    detail_stock = None
    
    # get the requested stock trough the url
    for stock in get_stocks():
        if stock_slug == stock['slug']:
            detail_stock = stock

    # ticker get a specific stock by the symbol
    stock = yf.Ticker(detail_stock['symbol']).info

    #print(stock.keys())
    
    # passing data to the view
    context = {
        'stock' : stock
    }

    return render(request, 'main/show.html', context)