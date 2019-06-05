Escasez
#########

El modelo de escasez de agua simula las deficiencias en el abastecimiento de
agua en cada una de las AGEB de la Ciudad de México. La escasez de agua se
calcula a través de un índice que toma valores entre 0 y 1.

Insumos
********

- Densidad de población para el año 2017, CONAPO
- Zonas críticas por Alcaldía, SACMEX
- Número de cisternas por Alcaldía, Encuesta intercensal 2015
- Ingreso total por alcaldía, Encuesta intercensal 2015
- Días sin agua, SACMEX
- Antigüedad de la infraestructura, LANCIS
- Falta en la distribución, Censo 2010
- Presión hidráulica, LANCIS

Issues
********

Repositorio SHV
- Generar índice de grado de escasez # 100

- Generar la capa de presión hidráulica # 122

Código
*******

  **indice_escasez.Rmd**

Salidas
********
  **escasez_ant_pres.shp**
