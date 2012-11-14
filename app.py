# -*- coding: utf-8 -*-

import base64
import cStringIO
import matplotlib.pyplot as plt
from bottle import route, run, response, static_file, post, request, view
from lib import configurar_grafico, accumulate


@route('/media/<filepath:path>')
def server_static(filepath):
    """Archivos estáticos"""
    return static_file(filepath, root='./media')


@route('/about')
@view('about')
def about():
    """Acerca de la apllicación"""
    return dict()


@route('/')
@view('index')
def index():
    """Formulario y página principal"""
    extra_css = """.shadow {box-shadow: 1px 1px 10px 5px #CDA;}"""
    extra_js = """<script>
        function graficar() {
            $.post('/graficar/', $('form').serialize(), function(data) {
                var img_tag="<img class='shadow' src='data:image/png;base64,";
                $("#imagen").html(img_tag + data + "' />");
            }).error(function(){
                $("#imagen").html("");
                alert("Error al generar la imágen, verifique los parámetros");
            });
        }
        $(document).ready(function() {
            $.ajaxSetup({cache: false});
            $("#btnVer").click(function(){
                $('form').submit();
            });
            $("form").submit(function(){
                graficar();
                return false;
            });
        });
    </script>
    """
    return dict(extra_js=extra_js, extra_css=extra_css)


@post('/graficar/')
def graficar():
    """Graficador y generador de imágen"""
    # Obtengo los valores o seteo los valroes por defecto
    serie = request.forms.serie or "1,2,3,4"
    xlabel = request.forms.xlabel or "Eje X"
    ylabel = request.forms.ylabel or "Eje Y"
    titulo = request.forms.titulo or u"Título"
    power = request.forms.power or 2

    tcb = float(power)  # Tiempos/Potencia relacionada

    # Datos de los bloques a leer
    datos = [int(n) for n in serie.split(',')]

    # Cálculo de los tiempos usados para cada movimiento
    tiempos = [0]
    for i in range(len(datos) - 1):
        t = abs(datos[i + 1] - datos[i]) * tcb
        tiempos.append(tiempos[i] + t)

    # Grafico tiempos potenciados
    plt.clf()
    plt.plot(tiempos, datos, linewidth=2.0, marker='o', linestyle='--',
             label="Bloques")
    plt.plot(tiempos, [d for d in accumulate(datos, tcb)], linewidth=1.0,
             marker='D', linestyle='--', label="Tiempos")

    # Agrego las etiquetas
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(titulo)
    plt.legend()

    # Configuro el gráfico
    plot = configurar_grafico(plt, datos, tiempos, tcb)

    # Genero y retorno la imágen
    img = cStringIO.StringIO()
    plot.savefig(img, transparent=False)
    response.content_type = 'image/png'
    return base64.b64encode(img.getvalue())


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
