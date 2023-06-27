## Modelo Predictivo Boletos Aéreos
El objetivo es la creación de un App web que permita predecir el precio de tiquetes aéreos, los datos son obtenidos de un repositorio de Github. Se pretende realizar un modelo basado en una red neuronal para la predicción.

## Necesidad:
La industria de las aerolíneas desde siempre ha sido un mercado inestable sumado a los problemas anteriores mencionados , este mercado sufre demasiadas fluctuaciones respecto a precios debido a varios factores externos , por ende surge un problema para los usuarios para la planificación eficiente de sus vuelos.

Por ende a través de técnicas de IA se pretende crear un modelo predictivo para los vuelos , para que de esta forma los usuarios puedan tener a la mano información acerca de las fechas , los trayectos y los precios, y poder generar información que ayude a la toma de decisiones por parte de una persona o empresa.

La predicción se basará provisionalmente en las siguientes características:

precios de vuelos anteriores.<br>
destino.<br>
partida.<br>
clase.<br>
aerolínea

#### ¿Quién se beneficia de construir este modelo/sistema?
Clientes de vuelos.

## Descripción de datos:
#### ¿Qué conjuntos de datos planea usar y cómo obtendrá los datos?

El conjunto de datos se creará extrayendo de un repositorio web https://github.com/MeshalAlamr/flight-price-prediction del usuario MeshalAlamr el cual extrae los datos de diferentes sitios web de viajes.

## Dataset
Esta carpeta contiene los datos extraidos de Kayak para el período del 01-02-2022 al 30-04-2022, incluidas las siguientes 12 rutas:

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


#### ¿Qué predecirá como su objetivo?
Precios de vuelos.

## Herramientas:

#### ¿Cómo pretende cumplir con los requisitos de herramientas del proyecto?
Uso de un dataset con datos realcionados con viajes.
Numpy y Pandas para realizar la manipulación de datos.
Matplotlib, Seaborn y Tableau para la visualización de datos.

#### ¿Está planeando con anticipación la necesidad o el uso de herramientas adicionales además de las requeridas?
Planeamos incorporar API de viajes para incluir datos en tiempo real.

### Arquitectura red neuronal

Usamos una red neuronal secuencial con la siguiente estructura:

La red mencionada es una red neuronal con una capa oculta de 16 unidades. La estructura de la red se define en el método __init__() de la clase RedPrecios, donde se crea una instancia de nn.Sequential llamada linear_relu_stack. Dentro de linear_relu_stack, se definen varias capas lineales y funciones de activación ReLU.

Las capas se definen de la siguiente manera:

nn.Linear(32, 16): Capa lineal con 32 unidades de entrada y 16 unidades de salida.

nn.ReLU(): Función de activación ReLU.

nn.Linear(16, 32): Capa lineal con 16 unidades de entrada y 32 unidades de salida.

nn.ReLU(): Función de activación ReLU.

nn.Linear(32, 1): Capa lineal con 32 unidades de entrada y 1 unidad de salida

En el método forward(), se aplica la operación de propagación hacia adelante de la red. La entrada x se pasa a través de linear_relu_stack y el resultado se asigna a y_pred. Finalmente, y_pred se devuelve como la salida de la red.



## Descripcion General del repositorio

El repositorio se compone de cuatro carpetas:


### Data:
    
    Esta carpeta contiene 14 archivos .csv de los cuales 12 son los datos extraídos del repositorio de MeshalAlamr. Los otros dos archivos son generados por la transformación y limpieza de los datos.


### Transformacion_Y_limpieza:
    Con tiene dos archivos .ipynb. donde el llamado join_Data.ipynb se realiza la concatenación de los 12 archivos generando el archivo Datos_completos.csv que contiene 55363 registros y 7 columnas.

    El archivo Transformacion.ipynb se encarga de analizar las variables y realizar cambios si es necesario
    analisis de tipos, de nulos, y de cambio de unidades.

### Analisis: 
    
    Contiene un archivo en el cual se realiza un analisis exploratorio y descriptivo de los datos.

### MODELO:

    Esta carpeta contiene Modelo2.ipynb en el cual se realiza todo el modelo la carga de los datos, la creacion de la red neuronal con pytorch y el entrenamiento y validacion.

    Tambien se cuenta con los archios .pt que son los modelos ya guardados y que pueden ser utilizados para las predicciones.
