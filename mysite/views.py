from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):

    #data_atual = date.today()
    #return HttpResponse(data_atual)
    return render(request, "index.html")

def page2(request):

    return render(request, "page2.html")

def page3(request):

    html = '''
    <html>
        <head><title>Página 3</title></head>
        <body>
            <h1>Python no Heroku - SOCPS</h1>
            <!-- se quiser troca esse cara-->
            <h2>Página 3</h2>
            <a href="../">index</a><br>
            <a href="../page4">pagina4</a>
        </body>
    </html>
    '''
    return HttpResponse(html)

def page4(request):
    return render(request, "page4.html")

def page5(request):
    data_atual = datetime.date.today()
    data_hour = datetime.time.hour

    html = f'''
    <html>
        <head><title>Index</title></head>
        <body>
            <h1>Avaliação SOCPS II</h1><br>
            <h1>Estudante: Pedro Vargas</h1><br>
            <h1> Data atual: {data_atual, data_hour} </h1>
        </body>
    </html>
    '''
    return HttpResponse(html)