# -*- coding: utf-8 -*-

import math
import operator
from matplotlib.ticker import MultipleLocator


def accumulate(iterable, power=1, func=operator.add):
    """Return running totals
    Copy from Python 3 docs

    >>> [ d for d in accumulate([1,2,3,4,5])]
    [1,3,6,10,15]
    >>> accumulate([1,2,3,4,5], operator.mul)
    [1,2,6,24,120]
    """
    it = iter(iterable)
    last = next(it)
    total = last * power
    print 0, last, power, total
    yield total
    for element in it:
        total = func(total, abs(element - last) * power)
        print last, element, power, total
        last = element
        yield total


def configurar_grafico(plot, datos, tiempos, potencia, pextra=1.3):
    """Configura los ejes y la grilla de fonde del gráfico"""

    t_acumulado = [d for d in accumulate(datos, potencia)]

    # Ajusto las longitudes de los ejes
    max_y = max(t_acumulado)  # Valor máximo a graficar en el eje Y
    top_y = max_y * pextra  # Valor máximo para el eje Y
    max_x = max(tiempos)  # Valor máximo a graficar en el eje X
    top_x = int(max_x * pextra)  # Valor máximo para el eje X
    plot.axis([max_x - top_x, top_x, max_y - top_y, top_y])

    # Agusto los ticks para la grilla
    ax = plot.subplot(111)
    x_min_locator = MultipleLocator(abs(math.ceil(top_x / 10.0) / 2.0))
    x_max_locator = MultipleLocator(abs(math.ceil(top_x / 10.0)))
    y_min_locator = MultipleLocator(abs(math.ceil(top_y / 10.0) / 2.0))
    y_max_locator = MultipleLocator(abs(math.ceil(top_y / 10.0)))
    ax.xaxis.set_minor_locator(x_min_locator)
    ax.xaxis.set_major_locator(x_max_locator)
    ax.yaxis.set_minor_locator(y_min_locator)
    ax.yaxis.set_major_locator(y_max_locator)

    # Activo la grilla de fondo
    plot.grid()

    return plot