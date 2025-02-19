import pandas as pd

'''
  Cargue el dataset y conviértelo en un DataFrame.
. Calcule la temperatura promedio de cada ciudad.
. Determine el registro con la temperatura más alta y el más bajo en el dataset.
. Identifique qué ciudad tuvo la temperatura más alta y cuál la más baja en todo el dataset.
. Encuentre cuántos registros tienen una temperatura mayor a 30°C.
. Cuenta cuántos días en total hay registrados por cada ciudad.
'''
df=pd.read_csv('clima.csv')

# Temperatura promedio de cada ciudad
temperatura_promedio=df.groupby('Ciudad')['Temperatura'].mean().sort_values(ascending=False)
print('----------------------------------')
print('La temperatura promedio de cada ciudad es: ')
print(temperatura_promedio.reset_index())

# Registro con la temperatura más alta y más baja con la ciudad
temperatura_maxima=df.loc[df['Temperatura'].idxmax()]
temperatura_minima=df.loc[df['Temperatura'].idxmin()]

print('----------------------------------')
print('El registro con la temperatura más alta es: ')
print(temperatura_maxima.to_frame().T)
print('----------------------------------')
print('El registro con la temperatura más baja es: ')
print(temperatura_minima.to_frame().T)

# Ciudad con la temperatura más alta y más baja
ciudad_temperatura_maxima=temperatura_maxima['Ciudad']
ciudad_temperatura_minima=temperatura_minima['Ciudad']

print('----------------------------------')
print('La ciudad con la temperatura más alta es: ',ciudad_temperatura_maxima)
print('La ciudad con la temperatura más baja es: ',ciudad_temperatura_minima)

# Registros con temperatura mayor a 30°C
temperatura_mayor_30 = (df['Temperatura'] > 30).sum()
print('----------------------------------')
print('La cantidad de registros con temperatura mayor a 30°C es: ',temperatura_mayor_30)

# Días registrados por ciudad
dias_registrados=df['Ciudad'].value_counts()
print('----------------------------------')
print('La cantidad de días registrados por ciudad es: ')
print(dias_registrados.reset_index().rename(columns={ 'count': 'Días Registrados'}))

