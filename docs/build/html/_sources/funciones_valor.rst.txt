Funciones de valor
######################


Logística
**********
Para la construcción de la función de valor
los parámetros son

Saturación = 3

Centro = 7

.. math::

  elevacion\_exposicion = \frac{1}{1.0 + e^{- k \left(- \frac{100 center - 100 xmin}{xmax - xmin} + \frac{100 x - 100 xmin}{xmax - xmin}\right)}}
  \\
  \\
  \\
  \\x = elevacion
  \\xmin = -16
  \\xmax = 31
  \\center = 7
  \\k = 0.083499
  \\

concava creciente
********************
Para la construcción de la función de valor
los parámetros son

Saturación = 1

.. math::

  elevacion\_sensibilidad = \frac{e^{\frac{\gamma \left(100 x - 100 xmin\right)}{xmax - xmin}} - 1}{e^{100 \gamma} - 1}
  \\
  \\
  \\
  \\x = elevacion
  \\xmin = -16
  \\xmax = 31
  \\\gamma = 0.01975

concava decreciente
********************
Para la construcción de la función de valor
los parámetros son

Saturación = 3

.. math::

  elevacion\_resiliencia = \frac{e^{\gamma \left(- \frac{100.0 x - 100.0 xmin}{xmax - xmin} + 100.0\right)} - 1}{e^{100 \gamma} - 1}
  \\
  \\
  \\
  \\x = elevacion
  \\xmin = -16
  \\xmax = 31
  \\\gamma =0.0492499
