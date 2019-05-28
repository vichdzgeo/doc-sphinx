################
Balance hídrico
################

Este modelo simula el escurrimiento superficial de las 244 subcuencas altas
en la periferia de la Ciudad de México. Cada subcuenca se dividió hasta en seis
bandas de elevación para estimar el escurrimiento acumulativo generado por la
heterogeneidad de la precipitación, la evapotranspiración y la cobertura
vegetal. Este modelo funciona con base en la curva numérica (CN) del método
SCS-CN desarrollado por el Servicio de Conservación de Suelos de Estados Unidos.



********
Insumos
********
Zona de estudio
=================
- swat_master.shp archivo vectorial que contine 244 subcuencas hidrológicas
  de la zona de estudio E.Vivoni
- swat_area.shp archivo vectorial que contiene la región de estudio para todo el
  valle de México E.Vivoni
- Agebs de la ciudad de México  INEGI
- Uso de suelo y vegetación serie VI INEGI
- `Edafología INEGI`_


Datos históricos de precipitación, temperatura y evapotranspiración
======================================================================
- Prec precipitación diaria en formato raster para el intervalo de tiempo de 01 de
  enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015

- TA temperatura promedio diaria en formato raster para el intervalo de tiempo de 01 de
  enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015

- ETA evapotranspiración promedio diaria en formato raster para el intervalo de tiempo
  de 01 de enero de 1993 al 31 de diciembre del 2013 - Livneh et al 2015

Datos de escenarios de cambio climático
=========================================
-  he45Prec55 12 archivos raster (1 por mes) que expresan el promedio de la
   precipitación mensual total expresada en mm. RCP 4.5
-  he45Prec85 12 archivos raster (1 por mes) que expresan el promedio de la
   temperatura promedio mensual total expresada en mm. RCP 4.5
-  he85Prec55 12 archivos raster (1 por mes) que expresan el promedio de la
   temperatura promedio mensual total expresada en mm. RCP 8.5
-  he85Prec85 12 archivos raster (1 por mes) que expresan el promedio de la
   temperatura promedio mensual total expresada en mm. RCP 8.5

-  he45TA55 12 archivos raster (1 por mes) que expresan el promedio de la
   temperatura promedio mensual total expresada en mm. RCP 4.5
-  he45TA85 12 archivos raster (1 por mes) que expresan el promedio de la
   temperatura promedio mensual total expresada en mm. RCP 4.5
-  he85TA55 12 archivos raster (1 por mes) que expresan el promedio de la
   temperatura promedio mensual total expresada en mm. RCP 8.5
-  he85TA85 12 archivos raster (1 por mes) que expresan el promedio de la
   temperatura promedio mensual total expresada en mm. RCP 8.5


..  note::

  he HadGEM2-ES 2075-2099 Modelo climático del sistema terrestre

  RCP 4.5: Escenario de estabilización. El forzamiento radiativo se estabiliza un
  poco luego del 2100. La temperatura muy probablemente excede los 2ºC.

  RCP 8.5: Incremento de las emisiones de GEI a lo largo del tiempo.
  La temperatura probablemente no excede los 4ºC.





.. _`Edafología INEGI`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search;jsessionid=39BB001F56D9D69BECA317CC4EF400CC#/metadata/19e432ad-a94c-4cbd-add6-67822fa63dfe

swat_area. Polígono de la zona de estudio para el Valle de México



***************
Procedimiento
***************

================
Series de tiempo
================

Objetivo:

Extraer de los datos raster de Livneh de la serie de tiempo (1993-2013)
los promedios mensuales de las variables de precipitación acumulada mensual, temperatura y
evapotranspiración para la zona de estudio.

códigos:

- promedios_historico_ta.py
- promedios_historico_prec.py
- promedios_historico_pet.py


salida:

- prom_mens_93_13.csv



.. csv-table:: Promedios mensuales de Prec,TA,ETA (1993 - 2013)
    :file: ../../mod_escorrentia/precipitacion_historica/salida/prom_mens_93_13.csv
    :header-rows: 1

descarga el archivo  :download:`prom_mens_93_13.csv <../../mod_escorrentia/precipitacion_historica/salida/prom_mens_93_13.csv>`.

=======================
Delta de precipitación
=======================

De los raster de los escenarios de cambio climatico, se extrae el promedio
mensual de los pixeles para la zona de estudio


- he45Prec55
- he45Prec85
- he85Prec55
- he85Prec85


salida

.. csv-table:: Promedios mensuales de escenarios de cambio climático
    :file: ../../mod_escorrentia/deltas_cambio_climatico/salida/prom_prec_esc.csv
    :header-rows: 1

descarga el archivo  :download:`prom_prec_esc.csv <../../mod_escorrentia/deltas_cambio_climatico/salida/prom_prec_esc.csv>`.



**************
Precipitación
***************

=======================
Precipitación histórica
=======================


************
Escorrentía
************
