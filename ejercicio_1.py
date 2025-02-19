import pandas as pd

'''
. Cargue los datos en un DataFrame.

. Calcule la cantidad total de productos vendidos por categoría.

. Determine cuál es el producto con el mayor total de ventas.

. Encuentre el precio promedio de los productos vendidos.

'''
df=pd.read_csv('ventas.csv')

# Cantidad total de productos vendidos por categoría
cantidad_total=df.groupby('Producto')['Cantidad'].sum().sort_values(ascending=False)
print('----------------------------------')
print(cantidad_total.reset_index())

# Producto con el mayor total de ventas
cantidad_total_mayor=cantidad_total.idxmax()
print('----------------------------------')
print('El producto con mayor total de ventas es: ',cantidad_total_mayor)

# Precio promedio de los productos vendidos
precio_promedio=df.groupby('Producto')['Precio_Unitario'].mean().sort_values
print('----------------------------------')
print('El precio promedio de los productos vendidos es: ')
print(precio_promedio.reset_index())