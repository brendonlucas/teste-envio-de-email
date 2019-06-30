from django.shortcuts import render, redirect
from django.core.mail import send_mail
from datetime import date

from gg.models import LinksRecuperacao
import random


def index(requests):
    return render(requests, 'index.html')


def rec(requests):
    return render(requests, 'recuperar.html')


def gerar_link():
    while True:
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'h']
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        link = ''
        for x in range(7):
            num_letra = random.randint(0, 10)
            link += letras[num_letra]

        for i in range(6):
            num_letra = random.randint(0, 9)
            link += str(numeros[num_letra])
        try:
            link_existe = LinksRecuperacao.objects.get(corpo_link=link)

        except LinksRecuperacao.DoesNotExist:
            LinksRecuperacao(corpo_link=link, status=1).save()
            break
    return link


def enviar(requests):
    link_gerado = gerar_link()
    # verificar se existe o email
    mensagem = 'Link para recuperar senha do connectedin \n' + 'http://127.0.0.1:8000/recuperacao/' + link_gerado
    send_mail('Email para recuperacao', mensagem, 'projectconnectedin@gmail.com',
              ['brendonplay007@gmail.com']
              , fail_silently=False)
    return redirect('index')


def recuperacao(requests, link):
    print(link)
    try:
        link_existe = LinksRecuperacao.objects.get(corpo_link=link)
        print('viu o link existe')
        data_atual = date.today()
        if link_existe is not None:
            print('viu o link existe 2')
            if link_existe.status == 1:
                print('viu o link existe 3')
                if data_atual == link_existe.data:
                    print('viu o link existe 4')



                    return render(requests, 'page_recuperar.html')
                else:
                    link_existe.status = 0
                    link_existe.save()
                    # desativar link
                    return render(requests, 'expirou.html')
            else:
                return render(requests, 'expirou.html')
        else:
            return render(requests, 'expirou.html')
    except LinksRecuperacao.DoesNotExist:
        return render(requests, 'expirou.html')
