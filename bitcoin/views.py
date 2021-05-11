from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import HttpResponse, render

from . import operacao


def index(request):

    resultado = operacao.price_bitcoin

    return render(request, 'index.html', {'resultado': resultado})