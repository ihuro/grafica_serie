Grafica Series
==============

Es un graficador de series utilizado para visualizar ejemplos de los valores obtenidos de algoritmos
para acceso a disco en la cátedra Sistemas Operativos II en UCSE DAR

Es una aplicación Bottle. Indicándole una serie de datos separados por coma y configurando un conjunto de
parámetros, realiza el gráfico de la serie.

Está inicialmente pensada para graficar los accesos a disco según una lista de bloques, donde el orden de
la lista depende de un algoritmo de acceso específico.

El parámetro de tiempo/potencia es para graficar los valores de tiempo utilizados en lugar de los bloques
(tiempo de desplazamiento * nro de bloques).

Instalación
===========

Clonar el repositorio

    git clone git://github.com/ihuro/grafica_serie.git

Dependencias
------------

Con virtualenv
--------------

Para instalarlo en un virtualenv, es necesario tener algunas dependencias para la compilación de matplotlib.
Estas dependencias son libpng y libfreetype (ver http://matplotlib.org/users/installing.html#build-requirements)

En Debian/Ubuntu, se puede hacer mediante `apt-get`

    apt-get install libpng12-dev libfreetype6-dev libfreetype6

Sin virtualenv
--------------

Se debe instalar matplotlib en el sistema. En Debian/Ubuntu se puede hacer mediante `apt-get`

    apt-get install python-matplotlib

Instalar dependencias
---------------------

Con o sin virtualenv, se pueden instalar las dependencias mediante `pip`

    pip install -r requirements.txt

Si no se dispone de `pip`, se pueden instalar las dependencias mediante `easy_install` o manualmente.
Para eso, ver el contenido de `requirements.txt` e instalar esos paquetes.

Ejecución
=========

Ejecutar el archivo `app.py`

    python app.py
