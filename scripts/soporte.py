
#Importo librerías
import pandas as pd
import numpy as np

import os
import sys
sys.path.append("../")

import warnings
warnings.filterwarnings("ignore")

"""Creo función para abrir los csv y convertir en DF.
"""
def leer_csv(ruta_csv):
    df= pd.read_csv(ruta_csv)
    pd.set_option('display.max_columns', None)
    return df

"""Creo función para ver la info de los DF.
"""
def info_df(df):
    return df.info()

"""Creo función para ver forma de los DF.
"""
def forma_df(df):
    print(f"El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.")

"""Creo función para ver los valores únicos de cada columna en el dF.
"""
def valores_unicos(df):
    for columna in df.columns:
        print(f"La distribución de las categorías para la columna {columna.upper()}:")
        print(df[columna].value_counts())


"""Creo función para ver los principales estadísticos de las columnas numéricas.
"""
def estadisticos_numericos(df):
   return df.describe().T

"""Creo función para ver los principales estadísticos de las columnas categóricas.
"""
def estadisticos_categoricos(df):
    return df.describe(include='O').T

"""Creo función para ver si hay valores duplicados y si los hay comprobar que tengan sentido.
"""
def duplicados(df):
    for columna in df.columns:
        duplicados_en_columna = df[columna].duplicated().sum()
        print(f"Duplicados en la columna '{columna.upper()}': {duplicados_en_columna}")

"""Creo función para ver los valores nulos.
"""
def nulos(df):
    return df.isnull().sum()

"""Creo función para buscar el porcentaje de nulos numéricos que tengo en las columnas porque en ninguno 
de los dos csv hay nulos categóricos.
"""
def nulos_numericos(df):
    columnas_con_nulos = df.columns[df.isnull().any()].tolist()
    print("Porcentaje de nulos numéricos por columna:")
    print(df[columnas_con_nulos].isnull().sum() / df.shape[0] * 100)    
    return columnas_con_nulos

"""Creo función para ver cómo se distribuyen los valores únicos en esas columnas.
"""
def distribucion_valores (df, columnas):
    for columna in columnas:
        print(f"La distribución de las categorías para la columna {columna.upper()}")
        print(df[columna].value_counts() / df.shape[0])

"""Creo función para eliminar columna 'Country' que solo tiene un valor.'
"""
def eliminar_columnas(df, columna):
    df.drop(columna, axis=1, inplace=True)


"""Creo función para eliminar las columnas Cancellation Year y Cancellation Month ya que tienen un 88% de nulos.
"""
def eliminar_columnas_nulos(df, columnas):
    for columna in columnas:
        if columna in df.columns:
            porcentaje_nulos = df[columna].isnull().mean() * 100
            if porcentaje_nulos > 85:
                df.drop(columna, axis=1, inplace=True)
                print(f"La columna '{columna.upper()}' se ha eliminado porque el porcentaje de nulos ({porcentaje_nulos:.2f}%) supera el {85}%.")
            else:
                print(f"La columna '{columna.upper()}' no se eliminó porque el porcentaje de nulos ({porcentaje_nulos:.2f}%) no supera el {85}%.")
        else:
            print(f"La columna '{columna.upper()}' no existe en el DataFrame.")

    return df

"""Creo función para que no haya números negativos en la columna Salary.
"""
def quitar_negativos(df, columna):
    df.loc[df[columna] < 0, columna] = df[columna].abs()
    return df


"""Creo función para calcular la media y la mediana a la columna Salary.
"""
def media_mediana (df, columna):
    print(f'La MEDIA de la columna {columna.upper()} es:')
    media = df[columna].mean()
    print(media)
    print(f'La MEDIANA de la columna {columna.upper()} es:')
    mediana = df[columna].median()
    print(mediana)


"""Creo función para imputar la mediana a la columna Salary.
"""
def imputar_mediana(df, columna):
    mediana = df[columna].median()
    df[columna].fillna(mediana, inplace=True)
    return df

"""Creo función para unir los dos DF usando merge_inner.
"""
def unir_df(df1, df2, on_column=None, how='inner'):
    df_merged_inner = pd.merge(df1, df2, on=on_column, how='inner')
    return df_merged_inner

"""Creo función para igualar nombres columnas con un guión bajo.
"""
def igualar_columnas(df):
    df.columns = df.columns.str.replace(' ', '_')
    return df

"""Creo función para cambiar el tipo de la columna Points Redeemed y que sea float.
"""
def cambiar_tipo(df, columna):
    df[columna]=df[columna].astype(float)
    return df


"""Creo función para guardar el DF resultante en la carpeta output_data.
"""
def guardar_df(df, nombre_archivo):
    ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'data', 'output_data', nombre_archivo + '.csv')
    df.to_csv(ruta_archivo, index=False)
    print(f"El DataFrame se ha guardado en {ruta_archivo}")

