import soporte

print('______________________FASE 1. EXPLORACIÓN INICIAL Y LIMPIEZA DE DATOS_______________________')

print('_______________APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME ACTIVIDAD CLIENTES____________')

#Llamo a la función de leer csv de la actividad de los clientes.
df_actividad_clientes = soporte.leer_csv('../data/input_data/Customer Flight Activity.csv')
print('Las 5 primeras filas del DataFrame de la ACTIVIDAD CLIENTES son:\n')
print(df_actividad_clientes.head())
print('.....................................................')

#Llamo a la función para ver la info del DF ACTIVIDAD CLIENTES.
print('La INFORMACIÓN del DataFrame de la ACTIVIDAD CLIENTES es:\n')
soporte.info_df(df_actividad_clientes)
print('.....................................................')

#Llamo a la función para ver los valores únicos del DF ACTIVIDAD CLIENTES.
soporte.valores_unicos(df_actividad_clientes)
print('.....................................................')

#Llamo a la función para cambiar el tipo de la columna Points Redeemed y que sea el mismo que Points Accumulated.
soporte.cambiar_tipo(df_actividad_clientes, 'Points Redeemed')

#Únicamente llamo a la función para ver los principales estadísticos de las columnas numéricas porque no tiene ninguna columna categórica.
print('Los principales estadísticos de las COLUMNAS NUMÉRICAS del DataFrame de la ACTIVIDAD CLIENTES son:\n')
estadisticos_numericos = soporte.estadisticos_numericos(df_actividad_clientes)
print(estadisticos_numericos)


print('_______________APERTURA CSV, EXPLORACIÓN Y LIMPIEZA DATAFRAME HISTORIAL CLIENTES____________')

#Repito los mismos pasos para leer el otro archivo csv y convertirlo en DF.
df_historial_clientes = soporte.leer_csv('../data/input_data/Customer Loyalty History.csv')
print('Las 5 primeras filas del DataFrame del HISTORIAL CLIENTES son:\n')
print(df_historial_clientes.head())
print('.....................................................')

#Llamo a la función para ver la info del DF HISTORIAL CLIENTES.
print('La INFORMACIÓN del DataFrame del HISTORIAL CLIENTES es:\n')
soporte.info_df(df_historial_clientes)
print('.....................................................')

#Llamo a la función para ver los valores únicos del DF HISTORIAL CLIENTES.
soporte.valores_unicos(df_historial_clientes)
print('.....................................................')

#Llamo a la función para eliminar la columna Country que tiene un único valor.
soporte.eliminar_columnas(df_historial_clientes, 'Country')

#Llamo a la función para ver los principales estadísticos de las columnas categóricas del DF HISTORIAL CLIENTES.
print('Los principales estadísticos de las COLUMNAS CATEGÓRICAS del DataFrame de la HISTORIAL CLIENTES son:\n')
estadisticos_categoricos = soporte.estadisticos_categoricos(df_historial_clientes)
print(estadisticos_categoricos)
print('.....................................................')

#Llamo a la función para ver los principales estadísticos de las columnas numéricas del DF HISTORIAL CLIENTES.
print('Los principales estadísticos de las COLUMNAS NUMÉRICAS del DataFrame de la HISTORIAL CLIENTES son:\n')
estadisticos_numericos = soporte.estadisticos_numericos(df_historial_clientes)
print(estadisticos_numericos)
print('.....................................................')

#Llamo a la función para buscar el porcentaje de nulos numéricos que tengo en el DF HISTORIAL CLIENTES.
print('El porcentaje de nulos numéricos por columna que hay en el DataFrame del HISTORIAL CLIENTES es:\n')
columnas_nulos_numericos = soporte.nulos_numericos(df_historial_clientes)
columnas_nulos_numericos
print('.....................................................')

#Llamo a la función para ver como se distribuyen los valores dentro de estas categórias, para ver si puedo imputar los nulos numéricos.
print('La distribución de los valores únicos en las COLUMNAS CON NULOS NUMÉRICOS es de:\n')
soporte.distribucion_valores(df_historial_clientes, columnas_nulos_numericos)
print('.....................................................')

#Llamo a la función para eliminar las dos columnas que tienen más de un 85% de nulos.
print('El DataFrame del HISTORIAL CLIENTES sin las columnas con más de un 85 por ciento de nulos queda así:\n')
soporte.eliminar_columnas_nulos(df_historial_clientes, columnas_nulos_numericos)
print(df_historial_clientes.columns)
print('.....................................................')

#Llamo a la función para cambiar el único valor negativo de la columna Salary, ya que al ser el único, entiendo que ha sido un error al imputar ese dato.
print('Los valores únicos de la columna SALARY tras corregir el valor negativo son:\n')
soporte.quitar_negativos(df_historial_clientes, 'Salary')
print(df_historial_clientes['Salary'].value_counts())
print('.....................................................')

#Llamo a la función para calcular la media y la mediana de la columna Salary y ver a qué valor imputo los nulos.
media_mediana_salary= soporte.media_mediana(df_historial_clientes, 'Salary')
print('.....................................................')

#Llamo a la función para imputar la mediana a la columna Salary.
soporte.imputar_mediana(df_historial_clientes, 'Salary')
print('Los nulos en el DataFrame de HISTORIAL CLIENTES son:')
print(df_historial_clientes.isnull().sum())


print('___________________UNIÓN DATAFRAMES_________________')

#Llamo a la función para unir los dos DF usando inner, así me quedaré con los registros de los clientes que tengan actividad registrada (que estén en las dos tablas).
df_clientes= soporte.unir_df(df_actividad_clientes, df_historial_clientes, on_column='Loyalty Number', how='inner')
print(df_clientes.head())
print('La forma del DataFrame CLIENTES es:\n')
soporte.forma_df(df_clientes)
print('.....................................................')
print('La info del DataFrame CLIENTES es:\n')
soporte.info_df(df_clientes)
print('.....................................................')
print('Los nulos del DataFrame CLIENTES son:')
print(soporte.nulos(df_clientes))
print('.....................................................')
print('Los duplicados del DataFrame CLIENTES son:')
soporte.duplicados(df_clientes)

#Llamo a la función para igualar nombres columnas.
soporte.igualar_columnas(df_clientes)
print(df_clientes.columns)

print('__________________________________OBSERVACIONES___________________________________')

print("""El DataFrame CLIENTES resultante contiene información de los clientes canadienses
que forman parte del programa de fidelidad de la compañía aérea, de los que se mantiene un
registro de sus vuelos, de los puntos que acumula con cada vuelo y de los puntos canjeados 
o no hasta el momento.

El DataFrame CLIENTES es un DataFrame que no contiene valores nulos, que presenta valores 
duplicados que se han considerado oportuno mantener (al trabajar con datos de transacciones
de clientes es normal que aparezcan este tipo de duplicados) y que tiene un total 
de 405624 registros y 22 columnas.""")

print('__________________________ALMACENAMIENTO DATAFRAME CLIENTES________________________')

#Llamo a la función para guardar el DF CLIENTES resultante en la carpeta output_data.
soporte.guardar_df(df_clientes, 'customer_combined')