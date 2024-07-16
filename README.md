# Evaluación Final Módulo 3 
## Análisis exploratorio de los datos del programa de fidelización de una compañía aérea.
**Tania Graff** | Promo A Part Time

![imagen_portada_modulo](portada.png)

En esta evaluación se han explorado, limpiado y transformado dos archivos de datos (.csv) que contienen información sobre los clientes canadienses adscritos al programa de fidelización de una compañía aérea.

Se ha automatizado la primera fase del proceso de transformación y limpieza de datos para crear un archivo .csv combinado llamado 'customer_combined'.

Se han utilizado diferentes herramientas de visualización para responder a algunas cuestiones relacionadas con el comportamiento de los clientes y su distribución por sexo, estado civil o lugar de procedencia, entre otros.

Y se ha realizado una prueba de hipótesis para comprobar si existe o no una relación entre el número de vuelos reservados y el nivel de estudios de los clientes.

### Estructura de archivos
**Data**
- Archivos CSV de entrada:
    - Customer Flight Activity.csv
    - Customer Loyalty History.csv
- Archivo CSV de salida:
customer_combined.csv

**Scripts**
- main.py. Script principal que ejecuta la automatización del proceso ETL.
- soporte.py. Archivo de soporte donde se definen las funciones utilizadas en el proceso ETL.

**Jupyternotes**

- fase2. Jupyter Notebook con gráficos y visualizaciones de datos.

*NOTA* Las visualizaciones también se pueden consultar desde este dashboard creado con Tableau: [Dashboard Clientes](https://public.tableau.com/views/visualizacion_datos_clientes_compania_aerea/FlightActivityCanadianCustomers?:language=es-ES&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- fase 3. Jupyter Notebook con análisis exploratorios avanzados y A/B testing.

**MD**

Archivos markdown:
- Enunciados de los ejercicios de la evaluación.
- README.md (este archivo).

### Descripción de archivos DATA
Los archivos 'Customer Flight Activity.csv' y 'Customer Loyalty History.csv' se utilizan como entrada para el proceso de combinación y limpieza de datos. El archivo resultante, 'customer_combined.csv', contiene los datos combinados de los clientes que forman parte del programa de fidelización de la compañía de vuelos, listos para análisis posteriores.

### Ejecución
Para realizar el proceso ETL de la primera fase, ejecutar desde la línea de comandos: python soporte.py | python main.py

