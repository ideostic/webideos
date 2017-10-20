from django.shortcuts import render
from Test.services import CryptoGetter


def index(request):
    CryptoGetter.generateInfoLabel()
    context = {
        'CryptoCoins': CryptoGetter.generateInfoLabel(),
    }
    return render(request, 'Test/index.html', context)
