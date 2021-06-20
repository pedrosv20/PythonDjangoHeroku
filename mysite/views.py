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

    html = f'''
    <html>
        <head><title>Página 5</title></head>
        <body>
            <h1>Python no Heroku - SOCPS</h1>
            <h1> Data atual: {data_atual} </h1>
            <h2>Página 5</h2>
            <a href="../page2">page2</a><br>
            <a href="../page4">page4</a><br>
            <img src="https://acegif.com/wp-content/uploads/2020/b72nv6/partyparrt-21.gif" alt="pérrot">
        </body>
    </html>
    '''
    return HttpResponse(html)