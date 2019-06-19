import qgis
import codecs
import processing
from qgis.core import *
from qgis.analysis import *
from os.path import join
from PyQt4.QtCore import *
from osgeo import gdal, ogr,osr
import math
import os 
import apc
'''
Script para calcular la evapotranspiracion potencial utilizando las formulas descritas en el codigo
ComputeLivnehPixelAverages.m ubicado en:

MEGADAPT/mega_carpetas_trabajo/Kristen/Matlab/
La variable Dl expresa en horas el tiempo de luz solar. para esta variable se extrae de la siguiente
página un valor para cada mes (dia 16) para la latitud de 20 grados N
https://www.orchidculture.com/COD/daylength.html#20N

'''
path_sig="C:/Dropbox (LANCIS)/SIG/desarrollo/sig_megadapt/procesamiento/evapotranspiracion/"
area_estudio=path_sig+"insumos/swat_area.shp"

L=2.453e6 #Latent heat of vaporization = 2.453e6 (J/kg)
Rv=461 #Gas constat dor moist air = 461 (J/KG)
#Se crea una lista con los directorios y archivos en la ruta especificada
directorios =os.listdir(path_sig+"prom_temp/")

# recorre cada elemento de la lista de direcctorio
for carpeta in directorios:
    #solo si es carpeta realizar lo siguiente
    if os.path.isdir(path_sig+"prom_temp/"+carpeta):
        print carpeta
        #nombre de la carpeta
        nombre_carpeta=carpeta
        path_vector=path_sig+"prom_temp/"+carpeta+"/"
        lista=[]
        for root, dirs, files in os.walk(path_vector):
            for name in files:
                extension = os.path.splitext(name)
                if extension[1] == '.shp':
                    lista.append(name)
        for archivo in lista:
            nombre_a= archivo.split(".")[0][5:13].lower()
            path_salida=path_sig+"salida/"+"et_"+nombre_a+".shp"
            apc.vcopia(area_estudio,path_salida)
            capa_et=QgsVectorLayer(path_salida,"","ogr")
            capa=QgsVectorLayer(path_vector+archivo,"","ogr")

            datos=[field.name() for field in capa.fields()][1:]
            
            dl=[10.91,11.34,11.86,12.46,12.95,13.20,13.10,12.68,12.11,11.53,11.03,10.8]
          

            capa_et.startEditing()
            for elemento in capa.getFeatures():
                mes=0
                
                for campo in datos:
                    mes+=1
                    pet=0
                    #apc.crear_campo(path_salida,"etc_"+str(mes),"Double")
                    temp_corr=1/(elemento[campo]+273.15)
                    esat=6.11*math.exp((L/Rv)*((1/273.15)-temp_corr))
                    pet=29.8*(esat/(elemento[campo]+273.2))

                    for correccion in dl:
                        pet_1=pet*correccion

                    for zona in capa_et.getFeatures():
                        zona["etc_"+str(mes)]=pet_1
                    print campo,"   ",elemento[campo],"...",mes,zona["etc_"+str(mes)]
                    capa_et.updateFeature(zona)
                        

            capa_et.commitChanges()
            print (path_salida)
