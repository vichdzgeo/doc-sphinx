Crecimiento Urbano
####################


Este modelo simula el crecimiento urbano de la Zona Metropolitana de la
Ciudad de México, a través de la implementación de SLEUTH, un software de
libre distribución basado en autómatas celulares y desarrollado en el National
Center for Geographic Information and Analysis para simular cambios de uso
de suelo.


Insumos
*******

Capas utilizadas para los tres escenarios:

- Restricciones de crecimiento
- Pendiente del terreno
- Vías de comunicación para la década de 1980
- Vías de comunicación para la década de 1990
- Vías de comunicación para la década del 2000
- Vías de comunicación para la década del 2015
- Zona urbana para la década de 1980
- Zona urbana para la década de 1990
- Zona urbana para la década de 2000


Escenarios:
============

**e04_s6_flores_v2_noairport_no11**

- Restricciones de crecimiento

Esta capa tiene distintos grados de exclusión que caracteriza el uso de suelo y
el grado de protección en áreas naturales

Está compuesta por la siguiente información:

Áreas verdes, 100% de exclusión
Zonas federales, 100% de exclusión
Cuerpos de agua, 100% de exclusión
Áreas Naturales Protegidas (municipales, estatales y federales), 50% de exclusión
Resto del área, 25% de exclusión
Semillas, 0% de exclusión

**e04_s6_flores_v2_noairport_no11_excl_0**

- Restricciones de crecimiento

Esta capa no tiene áreas de exclusión

**e04_s6_flores_v2_noairport_no11_excl_total**

- Restricciones de crecimiento

Esta capa tiene características de uso de suelo y de áreas naturales que presentan
el 100% de exclusión

Áreas verdes, 100% de exclusión
Zonas federales, 100% de exclusión
Cuerpos de agua, 100% de exclusión
Áreas Naturales Protegidas (municipales, estatales y federales), 100% de exclusión



Issues
*******

#. `# 837 hacer un informe con descripción los resultados de SLEUTH`_
#. `# 458 Reportar las corridas que se han hecho y que hacen falta de SLEUTH`_
#. `# 852 Realizar pruebas estadísticas para evaluar calibraciones de SLEUTH`_


Códigos
*******
sin códigos

Salidas
********

Son archivos para cada año de tipo .tif apartir del año 2016 hasta el 2060:

-  urban_2016.tif
-  ...
-  ...
-  ...
-  urban_2060.tif
