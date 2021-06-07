from django.test import TestCase

from . import operacao

resultado = operacao.price_bitcoin

if resultado < 30000:
    print('ERRO')