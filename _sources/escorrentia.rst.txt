
Balance hídrico
################

Este modelo simula el escurrimiento superficial de las 244 subcuencas altas
en la periferia de la Ciudad de México. Cada subcuenca se dividió hasta en seis
bandas de elevación para estimar el escurrimiento acumulativo generado por la
heterogeneidad de la precipitación, la evapotranspiración y la cobertura
vegetal. Este modelo funciona con base en la curva numérica (CN) del método
SCS-CN desarrollado por el Servicio de Conservación de Suelos de Estados Unidos.

.. image:: /imagenes/diagrama.jpg
   :target: _images/diagrama.jpg
   :alt: alternate text

Insumos
********

Zona de estudio
=================
- `swat_master.shp archivo vectorial que contine 244 subcuencas hidrológicas de la zona de estudio E.Vivoni`_
- `swat_area.shp archivo vectorial que contiene la región de estudio para todo el valle de México`_
- `swat_EB_insct_diss.shp archivo que contiene las bandas de elevaciones separadas por poligonos para cada una de las cuencas.`_
- `Agebs de la ciudad de México  INEGI`_
- `Uso de suelo y vegetación serie VI INEGI`_
- `Edafología INEGI`_


Datos históricos de precipitación, temperatura y evapotranspiración
======================================================================
- `Prec precipitación diaria en formato raster para el intervalo de tiempo de 01 de enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015`_
- `TA temperatura promedio diaria en formato raster para el intervalo de tiempo de 01 de enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015`_
- `PET evapotranspiración promedio diaria en formato raster para el intervalo de tiempo de 01 de enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015`_

Datos de escenarios de cambio climático
=========================================
-  he45Prec55 12 archivos raster (1 por mes) que expresan el promedio de la precipitación mensual total expresada en mm. RCP 4.5
-  he45Prec85 12 archivos raster (1 por mes) que expresan el promedio de la precipitación mensual total expresada en mm. RCP 4.5
-  he85Prec55 12 archivos raster (1 por mes) que expresan el promedio de la precipitación mensual total expresada en mm. RCP 8.5
-  he85Prec85 12 archivos raster (1 por mes) que expresan el promedio de la precipitación mensual total expresada en mm. RCP 8.5

-  he45TA55 12 archivos raster (1 por mes) que expresan el promedio de la temperatura promedio mensual total expresada en °C. RCP 4.5
-  he45TA85 12 archivos raster (1 por mes) que expresan el promedio de la temperatura promedio mensual total expresada en °C. RCP 4.5
-  he85TA55 12 archivos raster (1 por mes) que expresan el promedio de la temperatura promedio mensual total expresada en °C. RCP 8.5
-  he85TA85 12 archivos raster (1 por mes) que expresan el promedio de la temperatura promedio mensual total expresada en °C. RCP 8.5


..  note::

  he HadGEM2-ES 2075-2099 Modelo climático del sistema terrestre

  RCP 4.5: Escenario de estabilización. El forzamiento radiativo se estabiliza un
  poco luego del 2100. La temperatura muy probablemente excede los 2ºC.

  RCP 8.5: Incremento de las emisiones de GEI a lo largo del tiempo.
  La temperatura probablemente no excede los 4ºC.




.. Metadatos de Zona de estudio

.. _swat_master.shp archivo vectorial que contine 244 subcuencas hidrológicas de la zona de estudio E.Vivoni: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/7b573714-a1a5-4737-92e6-3e213454b626
.. _swat_area.shp archivo vectorial que contiene la región de estudio para todo el valle de México : http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/21d847a8-ccf5-4097-928d-0d7619b8e5c1
.. _swat_EB_insct_diss.shp archivo que contiene las bandas de elevaciones separadas por poligonos para cada una de las cuencas.: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/facaf5cf-9f1e-4680-9aa3-cea5c74b2a13
.. _Agebs de la ciudad de México  INEGI: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/6207036e-a661-440f-aebb-0fac5325d210
.. _Uso de suelo y vegetación serie VI INEGI: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/4a984bc9-0486-4b97-ab4a-eb82b67bcb9e
.. _Edafología INEGI: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search;jsessionid=39BB001F56D9D69BECA317CC4EF400CC#/metadata/19e432ad-a94c-4cbd-add6-67822fa63dfe


.. Metadatos de Datos históricos de precipitación, temperatura y evapotranspiración

.. _Prec precipitación diaria en formato raster para el intervalo de tiempo de 01 de enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015 : http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/3ae6f733-5c3f-4252-a852-abd8fc8bea1f
.. _TA temperatura promedio diaria en formato raster para el intervalo de tiempo de 01 de enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/3927a1e3-615e-4555-b855-47daf6cfa1d1
.. _PET evapotranspiración promedio diaria en formato raster para el intervalo de tiempo de 01 de enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/2af95668-4c26-4359-900e-fb81b32e3c22

Issues
*******

`#26 calcular las escorrentias de cada escenario de precipitación y urbanización, para cada cuenca swat por año`_

`#27 implementar un algoritmo que recalcule el numero de curva dependiendo de el escenario urbano`_

`#28 entender la estructura de datos y el procedimiento que usaron Vivoni y sus coloboradores para calcular la curva numérica`_

`#29 calcular las escorrentías con los números de curva actuales para cada cuenca swat`_

`#55 Hacer un script para preparar las capas de urbanización para ser usadas en el recálculo del número de curva`_

`#57 calcular los números de curva para cada año de cada escenario de crecimiento urbano`_

`#59 Hacer un script para calcular la evapotranspiración potencial a partir de la temperatura`_

`#81 Generar una capa para el cálculo de curva númerica utilizando solo la serie VI de INEGI`_
`#82 Calcular número y áreas de las cuencas con urbanización para el escenario histórico, 2040 y 2060`_

`#86 Generar experimentos de simulación para calcular escurrimiento bajo los distintos escenarios de urbanización y de cambio climático`_

`#91 Generar un dataframe que contenga los datos de precipitación y escorrentia por ageb para el escenario 8.5_8.5`_

`#96 Generar para cada escenario de escorrentía un csv con precipitación anual por ageb y escorrentía anual por ageb`_


.. _`#29 calcular las escorrentías con los números de curva actuales para cada cuenca swat`: https://github.com/sostenibilidad-unam/SHV/issues/29
.. _`#26 calcular las escorrentias de cada escenario de precipitación y urbanización, para cada cuenca swat por año`: https://github.com/sostenibilidad-unam/SHV/issues/26
.. _`#27 implementar un algoritmo que recalcule el numero de curva dependiendo de el escenario urbano`: https://github.com/sostenibilidad-unam/SHV/issues/27
.. _`#28 entender la estructura de datos y el procedimiento que usaron Vivoni y sus coloboradores para calcular la curva numérica`: https://github.com/sostenibilidad-unam/SHV/issues/28
.. _`#55 Hacer un script para preparar las capas de urbanización para ser usadas en el recálculo del número de curva`: https://github.com/sostenibilidad-unam/SHV/issues/55
.. _`#57 calcular los números de curva para cada año de cada escenario de crecimiento urbano`: https://github.com/sostenibilidad-unam/SHV/issues/57
.. _`#59 Hacer un script para calcular la evapotranspiración potencial a partir de la temperatura`: https://github.com/sostenibilidad-unam/SHV/issues/59
.. _`#81 Generar una capa para el cálculo de curva númerica utilizando solo la serie VI de INEGI`: https://github.com/sostenibilidad-unam/SHV/issues/81
.. _`#82 Calcular número y áreas de las cuencas con urbanización para el escenario histórico, 2040 y 2060`: https://github.com/sostenibilidad-unam/SHV/issues/82
.. _`#86 Generar experimentos de simulación para calcular escurrimiento bajo los distintos escenarios de urbanización y de cambio climático`: https://github.com/sostenibilidad-unam/SHV/issues/86
.. _`#91 Generar un dataframe que contenga los datos de precipitación y escorrentia por ageb para el escenario 8.5_8.5`: https://github.com/sostenibilidad-unam/SHV/issues/91
.. _`#96 Generar para cada escenario de escorrentía un csv con precipitación anual por ageb y escorrentía anual por ageb`:  https://github.com/sostenibilidad-unam/SHV/issues/96


Códigos
*******

promedio_histororico_prec.py
promedios.py
calculo_datos.py
prec_vol_2.py

urb_a_curvan_v3.py

evapotranspiracion.v2

curva_numerica_usvsvi.py

script en R

build_dataframe_nf_ff_v2.py












Salidas
********



.. Procedimiento
.. ***************
..
..
.. Series de tiempo
.. ================
..
.. Objetivo:
..
.. Extraer de los datos raster de Livneh de la serie de tiempo (1993-2013)
.. los promedios mensuales de las variables de precipitación acumulada mensual, temperatura y
.. evapotranspiración para la zona de estudio.
..
.. códigos:
..
.. - promedios_historico_ta.py
.. - promedios_historico_prec.py
.. - promedios_historico_pet.py
..
..
.. salida:
..
.. - prom_mens_93_13.csv
..
..
..
.. .. csv-table:: Promedios mensuales de Prec,TA,ETA (1993 - 2013)
..     :file: ../../mod_escorrentia/precipitacion_historica/salida/prom_mens_93_13.csv
..     :header-rows: 1
..
.. descarga el archivo  :download:`prom_mens_93_13.csv <../../mod_escorrentia/precipitacion_historica/salida/prom_mens_93_13.csv>`.
..
..
.. Delta de precipitación
.. =======================
..
.. De los raster de los escenarios de cambio climatico, se extrae el promedio
.. mensual de los pixeles para la zona de estudio
..
..
.. - he45Prec55
.. - he45Prec85
.. - he85Prec55
.. - he85Prec85
..
..
.. salida
..
.. .. csv-table:: Promedios mensuales de escenarios de cambio climático
..     :file: ../../mod_escorrentia/deltas_cambio_climatico/salida/prom_prec_esc.csv
..     :header-rows: 1
..
.. descarga el archivo  :download:`prom_prec_esc.csv <../../mod_escorrentia/deltas_cambio_climatico/salida/prom_prec_esc.csv>`.
..
..
..
..
.. Precipitación
.. ***************
..
.. Precipitación histórica
.. =======================
..
.. Escorrentía
.. ************
