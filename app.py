# -*- coding: utf-8 -*-

import cStringIO
import base64
import matplotlib.pyplot as plt
from bottle import route, run, response, static_file, post, request


@route('/css/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./css')


@route('/js/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./js')


@route('/img/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./img')


@route('/about')
def about():
    return "\n".join(open("about.html", "r").readlines())


@route('/')
def index():
    return "\n".join(open("index.html", "r").readlines())


@post('/graficar/')
def graficar():
    serie = request.forms.serie or "1,2"
    xlabel = request.forms.xlabel or "Eje X"
    ylabel = request.forms.ylabel or "Eje Y"
    titulo = request.forms.titulo or u"Título"
    power = request.forms.power or 2
    
    tcb = float(power) # Tiempos/Potencia relacionada

    # Datos de los bloques a leer
    datos = [int(n) for n in serie.split(',')]

    # Cálculo de los tiempos usados para cada movimiento
    tiempos = [0]
    for i in range(len(datos)-1):
        t = abs(datos[i + 1] - datos[i]) * tcb
        tiempos.append(tiempos[i] + t)

    # Grafico tiempos potenciados
    plt.clf()
    plt.plot(tiempos, datos, linewidth=2.0)
    plt.plot(tiempos, [d*tcb for d in datos], linewidth=1.0)

    # Agrego las etiquetas a los ejes
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(titulo)

    # Genero y retorno la imágen
    img = cStringIO.StringIO()
    plt.savefig(img, transparent=False)
    response.content_type = 'image/png'
    return base64.b64encode(img.getvalue())


run(host='localhost', port=8080, reloader=True)
