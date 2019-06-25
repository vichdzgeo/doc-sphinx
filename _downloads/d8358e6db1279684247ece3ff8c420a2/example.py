import os


def abc():
    '''
    **Objetivo**:  Este código estima a partir de la altura y la distancia a las
    entradas del sistema Cutzamala la presión hidráulica por AGEB.

    **Proyecto**:   MEGADAPT

    **Autor (es)**: Fidel Serrano y Víctor Hernández
    '''

x = range(1,101)
y = len(x)

def grafica():
    '''
    Esta funcion ....

    .. plot::

       import matplotlib.pyplot as plt
       import numpy as np
       x = np.random.randn(1000)
       plt.hist( x, 20)
       plt.grid()
       plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
       plt.show()

    '''

    a = 5
    b = 10
    y = a+b +a*b
