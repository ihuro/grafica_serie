Grafica Series
==============

Es un graficador de series utilizado para visualizar ejemplos de los valores obtenidos de algoritmos
para acceso a disco en la c�tedra Sistemas Operativos II en UCSE DAR

Es una aplicaci�n Bottle. Indic�ndole una serie de datos separados por coma y configurando un conjunto de
par�metros, realiza el gr�fico de la serie.

Est� inicialmente pensada para graficar los accesos a disco seg�n una lista de bloques, donde el orden de
la lista depende de un algoritmo de acceso espec�fico.

El par�metro de tiempo/potencia es para graficar los valores de tiempo utilizados en lugar de los bloques
(tiempo de desplazamiento * nro de bloques).

Instalaci�n
===========

Clonar el repositorio

    git clone git://github.com/ihuro/grafica_serie.git

Dependencias
------------

Con virtualenv
--------------

Para instalarlo en un virtualenv, es necesario tener algunas dependencias para la compilaci�n de matplotlib.
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

Ejecuci�n
=========

Ejecutar el archivo `app.py`

    python app.py
