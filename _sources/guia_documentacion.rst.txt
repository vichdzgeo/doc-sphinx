Guía para documentar con Sphinx
###############################


Párrafos
**********
El párrafo es el bloque más básico en un documento rst, los párrafos son
simplemente trozos de texto separados por uno o más líneas en blanco. La
sangría es significativa en rst, por lo que todas las líneas del mismo
párrafo deben alinearse a la izquierda con el mismo nivel de sangría.


Marcadores de línea
*********************

El marcado estándar en línea rst es bastante simple de usar
 - un asterisco  \*texto\* para énfasis (cursíva)
 - dos asteriscos  \*\*text\*\* para énfasis fuerte (negrita)
 - dos comillas inversas  \`\`texto\`\` para ejemplos de código

Ejemplo:

*esto es un texto en cursivas*

**esto es un texto en negritas**

``esto es un bloque de código``



Listas
**********
Para la generación de listas vasta con colocar un asterisco al pricipio de la
línea, para lístas numéricas bien puede colocar \1. el número explicitamente
o puede colocar \#. al principio de la línea y se enumerarán de forma automática.



Código fuente
****************
Los bloques de código litera se introducen al terminar un párrafo con el marcador
especial **\:\:** El bloque literal debe estar sangrado ( y, como todos los Párrafos
, separados delos que lo rodean con líneas en blanco.)

Este es un párrafo de texto normal. El siguiente párrafo es un ejemplo de código::

  Puede abarcar

  diferentes líneas

Este es un párrafo de texto normal de nuevo.


Tablas
***************

Las tablas simples deben contener más de una fila y la primera columan no puede
contener varias líneas::

  =====  =====  =======
  A      B      A and B
  =====  =====  =======
  False  False  False
  True   False  False
  False  True   False
  True   True   True
  =====  =====  =======



=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======


Hipervinculos
*****************

Para colocar hipervinculos a una palabra y redireccione al sitio web solcitado
se tiene que colocar un guión bajo al finalizar la palabra. posteriormente
se tiene que declarar e indicar el link.
Ejemplo en rst: ::

  Conozca la página de Python_ para más información.

  .. _Python: http://www.python.org

Como se visualizaría en la página:

Conozca la página de Python_ para más información.

.. _Python: http://www.python.org

Descargas
============

Para agregar una liga donde el usuario pueda descargar algún tipo de archivo
se usa la referencia *download*
Ejemplo en rst : ::

  descarga el código de ejemplo :download:`codigo de ejemplo </../../example.py>`.

Como se visualizaría en la página.

descarga el código de ejemplo :download:`codigo de ejemplo </../../example.py>`.

Secciones
**********
 Los encabezados de sección se crean subrayando ( y opcionalmente, delinieando)
 el título de la sección con un carácter de puntuación, al menos tan largo como
 el texto.

 Normalmente, no hay niveles asignados a ciertos caracteresm ya que la estructura
 se determian a partir de la sucesión de encabezados. Sin embargo se propone
 la siguiente convención que es usada en la guía de estilo para código en Python


* #, Encabezados
* \*, Capítulos
* =, Secciones
* -, Subsecciones
* ^, Subsubsecciones

Imágenes
**********

Sphinx soporta una directiva de imagen que es utilidada asi ::

  .. imagen :: /imagenes/imagen.jpg

Cuando se usa dentro de Sphinx, el nombre de archivo dado debe ser relativo al
archivo de origen.

Archivos separados por comas (CSV)
***********************************
El lenguaje restructurado usado en Sphinx tiene la capacidad de leer un
arhivo separado por comas, la directiva que se ocupa es la siguiente ::

  .. csv-table:: Tabla de prueba
      :file: ./csv/ejemplo.csv
      :header-rows: 1

Mostrandose de la siguiente forma:

.. csv-table:: Tabla de prueba
    :file: ./csv/ejemplo.csv
    :header-rows: 1

Ecuaciones
*************
reStructuredText en conjunto con LaTeX permiten la inserción de ecuaciones
matemáticas de tal manera que su visualización sea elegante y lo más parecida
a la connotacion matemática convencional.

Por ejemplo:

Combinación lineal ponderada


..  \frac{ \sum_{t=0}^{N}f(t,k) }{N}


.. math::
  S_j = \sum_{i}^{I}w_i x_{ij}



| S =  Agregación del modelo multicriterio
| w =  peso  del  criterio
| x =  valor  del  criterio  (Se  obtiene  de  la  función  de  valor  discreta  o  continua)
| i =  criterios  de  decisión
| j =  alternativas



Códigos
********


.. automodule:: example
    :members:
    :private-members:

https://build-me-the-docs-please.readthedocs.io/en/latest/Using_Sphinx/ShowingCodeExamplesInSphinx.html


.. code-block:: r

  Fibonacci_12<-numeric(12)
  Fibonacci_12[1]<-Fibonacci_12[2]<-1
  for(i in 3:12){Fibonacci_12[i]<-Fibonacci_12[i-2]+Fibonacci_12[i-1]}
  Fibonacci_12


The literal blocks are now highlighted as HTML, until a new directive is found.

.. code-block:: html

   <html><head></head>
   <body>This is a text.</body>
   </html>


.. code-block:: python

  for i in range(1,101):
    print(i)


Notas a pie de página
**********************
Para colocar notas a pie de página seguir el siguiente ejemplo: ::

  Énfasis [#f1]   "A dos hombres que viven el mismo número de años,
  el mundo les proporciona siempre la misma cantidad de experiencias.
  A nosotros nos corresponde tener conciencia de ellas.
  Sentir la propia vida, su rebelión, su libertad, y lo más posible,
  es vivir lo más posible." [#f2]_

  .. rubric:: Notas

  .. [#f1] Fuerza de la articulación o en la entonación con la que se quiere destacar
   un aspecto de lo que se dice
  .. [#f2] "El mito del Sísifo" (1942) - Albert Camus

La manera de visualización en la página es la siguiente:


Énfasis [#f1]_   ... "A dos hombres que viven el mismo número de años,
el mundo les proporciona siempre la misma cantidad de experiencias.
A nosotros nos corresponde tener conciencia de ellas.
Sentir la propia vida, su rebelión, su libertad, y lo más posible,
es vivir lo más posible." [#f2]_

.. rubric:: Notas

.. [#f1] Fuerza de la articulación o en la entonación con la que se quiere destacar
 un aspecto de lo que se dice
.. [#f2] "El mito del Sísifo" (1942) - Albert Camus
