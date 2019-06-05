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

- Vías de comunicación para la década de 1980
- Vías de comunicación para la década de 1990
- Vías de comunicación para la década del 2000
- Vías de comunicación para la década del 2015
- Crecimiento urbano para la década de 1980
- Crecimiento urbano para la década de 1990
- Crecimiento urbano para la década del 2000
- Crecimiento urbano para la década del 2015
- Pendiente del terreno
- Sombreado del terreno

Escenarios:
============

**e04_s6_flores_v2_noairport_no11**

- Exclusión

Esta capa tiene distintos grados exclusión que caracteriza el uso de suelo y
el grado de protección en áreas naturales

Está compuesta por la siguiente información:

Áreas verdes, 100% de exclusión
Zonas federales, 100% de exclusión
Cuerpos de agua, 100% de exclusión
Áreas Naturales Protegidas (municipales, estatales y federales), 50% de exclusión
Resto del área, 25% de exclusión
Semillas, 0% de exclusión

**e04_s6_flores_v2_noairport_no11_excl_0**

- Exclusión

Esta capa no tiene áreas de exclusión

**e04_s6_flores_v2_noairport_no11_excl_total**

- Exclusión

Esta capa tiene características de uso de suelo y de áreas naturales que presentan
el 100% de exclusión

Áreas verdes, 100% de exclusión
Zonas federales, 100% de exclusión
Cuerpos de agua, 100% de exclusión
Áreas Naturales Protegidas (municipales, estatales y federales), 100% de exclusión



Issues
*******
Repositorio Planeación colaborativa
- hacer un informe con descripción los resultados de SLEUTH # 837
- Reportar las corridas que se han hecho y que hacen falta de SLEUTH # 458
- Realizar pruebas estadísticas para evaluar calibraciones de SLEUTH # 852


Códigos
*******
sin códigos

Salidas
********

Son archivos para cada año tipo .tif apartir del año 2016 hasta el 2060:

-  urban_2016.tif
-  ...
-  ...
-  ...
-  urban_2060.tif
