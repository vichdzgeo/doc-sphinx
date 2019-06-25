Abastecimiento de agua
#######################

El modelo de escasez de agua simula las deficiencias en el abastecimiento de
agua en cada una de las AGEB de la Ciudad de México. La escasez de agua se
calcula a través de un índice que toma valores entre 0 y 1.

Insumos
********

- Densidad de población para el año 2017, CONAPO
- `Zonas críticas por Alcaldía, SACMEX`_
- `Número de cisternas por Alcaldía, Encuesta intercensal 2015`_
- `Ingreso total por alcaldía, Encuesta intercensal 2015`_
- `Días sin agua, SACMEX`_
- `Antigüedad de la infraestructura, LANCIS`_
- `Falta en la distribución, Censo 2010`_
- `Presión hidráulica, LANCIS`_


.. links Insumos

.. _`Densidad de población para el año 2017, CONAPO`:
.. _`Zonas críticas por Alcaldía, SACMEX`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/a00f0839-bf90-4fb0-b819-74f5963109c0
.. _`Número de cisternas por Alcaldía, Encuesta intercensal 2015`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/60563b81-ad76-48ab-a2aa-8a06018d73f5
.. _`Ingreso total por alcaldía, Encuesta intercensal 2015`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/04ee8daf-6f86-44f4-9edd-461dd646be22
.. _`Días sin agua, SACMEX`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/79d0fc39-8903-4433-9610-f801e54ffa12
.. _`Antigüedad de la infraestructura, LANCIS`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/f2fa0db3-cbec-4989-ac1d-0ebb63e5e8a7
.. _`Falta en la distribución, Censo 2010`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/5c463557-2178-4ecc-97cb-3bebc296c8a6
.. _`Presión hidráulica, LANCIS`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/0687d057-144e-4586-a01d-5ee9c75c6e34





Issues
********

#. `#100 Generar índice de grado de escasez`_

#. `#122 Generar la capa de presión hidráulica`_


.. issues

.. _`#100 Generar índice de grado de escasez`: https://github.com/sostenibilidad-unam/SHV/issues/100
.. _`#122 Generar la capa de presión hidráulica`: https://github.com/sostenibilidad-unam/SHV/issues/122

Código
*******

  **indice_escasez.Rmd**

Salidas
********
  `escasez_ant_pres.shp`_


.. link salidas

.. _`escasez_ant_pres.shp`: http://magrat.mine.nu:8088/geonetwork/srv/spa/catalog.search#/metadata/f164a7ea-5a19-4bf4-af66-77640b7cea07
