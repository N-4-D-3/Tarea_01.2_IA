
import pandas as pd

df=pd.read_csv('calificaciones.csv')

print('----------------------------------')
print('Las primeras filas del dataset son: ')
print(df.head())

# Promedio de calificaciones por materia
promedio_calificaciones=df.groupby('Materia')['Calificación'].mean().sort_values(ascending=False)
print('----------------------------------')
print('El promedio de calificaciones por materia es: ')
print(promedio_calificaciones.reset_index())

# Estudiante con el promedio más alto
promedio_estudiante=df.groupby('Estudiante')['Calificación'].mean().sort_values(ascending=False)
print('----------------------------------')
print('El estudiante con el promedio más alto es: ')
print(promedio_estudiante.reset_index().head(1))

# Promedio de calificaciones por estudiante
promedio_calificaciones_estudiante=df.groupby('Estudiante')['Calificación'].mean().sort_values(ascending=False)
print('----------------------------------')
print('El promedio de calificaciones por estudiante es: ')
print(promedio_calificaciones_estudiante.reset_index())

# Estudiantes con promedio superior a 85
estudiantes_promedio_85 = (promedio_calificaciones_estudiante > 85).sum()
print('----------------------------------')
print('La cantidad de estudiantes con promedio superior a 85 es: ',estudiantes_promedio_85)

# Materia con la mayor cantidad de calificaciones registradas
materia_calificaciones = df['Materia'].value_counts().reset_index()
materia_calificaciones.columns = ['Materia', 'Materias Registradas']

print('----------------------------------')
print('La materia con la mayor cantidad de calificaciones registradas es:')
print(materia_calificaciones)

# 5 estudiantes con el promedio más bajo
promedio_calificaciones_estudiante_bajo=promedio_calificaciones_estudiante.sort_values(ascending=True)
print('----------------------------------')
print('Los 5 estudiantes con el promedio más bajo son: ')
print(promedio_calificaciones_estudiante_bajo.reset_index().head(5))