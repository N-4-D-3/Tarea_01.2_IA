import pandas as pd

df=pd.read_csv('ventas.csv')

# Cantidad total de productos vendidos por categoría
cantidad_total=df.groupby('Producto')['Cantidad'].sum().sort_values(ascending=False)
print('----------------------------------')
print(cantidad_total.reset_index())

# Producto con el mayor total de ventas
df['Total_Ventas']=df['Cantidad']*df['Precio_Unitario']
producto_mayor_ventas=df.groupby('Producto')['Total_Ventas'].sum().idxmax()
print('----------------------------------')
print('El producto con mayor total de ventas es:',producto_mayor_ventas)

# Precio promedio de los productos vendidos
precio_promedio=df.groupby('Producto')['Precio_Unitario'].mean().sort_values(ascending=False)
print('----------------------------------')
print('El precio promedio de los productos vendidos es: ')
print(precio_promedio.reset_index())