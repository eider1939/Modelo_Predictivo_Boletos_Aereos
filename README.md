## Modelo_Predictivo_Boletos_Aereos
 Creacion de un App que permita predecir el precio de ticketes aereos, los datos son obtenidos de un repositorio web de Github. Se pretendi realizar un modelo basado en un red neuronal.

## Necesidad:
#### Que necesidad se plantea resolver o pregunta a responder 

Planeamos predecir los precios de los boletos para los próximos vuelos para ayudar a los clientes a seleccionar el momento óptimo para viajar y el vuelo más barato al destino deseado.

A lo largo de este proyecto, se aplicará un modelo de un red neuronal para pronosticar los boletos de avión más baratos a un destino específico en función de los datos extraídos de una variedad de sitios web de viajes como Momondo, Kayak y Expedia.

La predicción se basará provisionalmente en las siguientes características:

precios de vuelos anteriores
destino
partida
clase
aerolínea

#### ¿Quién se beneficia de construir este modelo/sistema?
Clientes de vuelos.

## Descripción de datos:
#### ¿Qué conjuntos de datos planea usar y cómo obtendrá los datos?

El conjunto de datos se creará extrayendo de un repositori web https://github.com/MeshalAlamr/flight-price-prediction del usuario MeshalAlamr el cual extrae los datos de diferentes sitios web de viajes.

## Dataset
Esta carpeta contiene los datos raspados de Kayak para el período del 01-02-2022 al 30-04-2022, incluidas las siguientes 12 rutas:

* NYC = NUEVA YORK
* PAR = PARIS
* RUH = RIAD ARABIA SAUDI
* SVO = MOSCU

RUTAS:

- RUH => NYC
- RUH => SVO
- RUH => PAR
- NYC => RUH
- NYC => SVO
- NYC => PAR
- SVO => PAR
- SVO => RUH
- SVO => NYC
- PAR => NYC
- PAR => RUH
- PAR => SVO 


#### ¿qué predecirá como su objetivo?
Precios de vuelos.

## Herramientas:
#### ¿Cómo pretende cumplir con los requisitos de herramientas del proyecto?
Uso de un dataset con datos realcionados con viajes.
Numpy y Pandas para realizar la manipulación de datos.
Matplotlib, Seaborn y Tableau para la visualización de datos.
#### ¿Está planeando con anticipación la necesidad o el uso de herramientas adicionales además de las requeridas?
Planeamos incorporar API de viajes para incluir datos en tiempo real.