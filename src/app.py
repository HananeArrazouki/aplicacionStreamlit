# Importar las librerias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Añade un título
st.title('EMPLEATRONIX')

# Muestra una breve descripción sobre la aplicación
st.write('Todos los datos sobre los empleados en una aplicación.')

# Leer el archivo CSV y cargar los datos en un DataFrame llamado 'employees'.
datos_empleados = pd.read_csv('csv/employees.csv')

# Muestra los datos de los empleados en forma de dataframe
st.dataframe(datos_empleados)

# Agrega una línea divisoria para mejorar la presentación
# st.divider()
st.markdown("")

# Divide el espacio en tres columnas para personalizar la visualización del gráfico
columna_color, columna_mostrar_nombres, columna_mostrar_salarios = st.columns(3)

# En la primera columna, permite al usuario elegir el color de las barras en el gráfico
with columna_color:
    color_barras = st.color_picker('Elige un color para las barras', '#3475B3')

# En la segunda columna, permite al usuario activar/desactivar la visualización de nombres en el gráfico
with columna_mostrar_nombres:
    mostrar_nombres = st.toggle('Mostrar el nombre')

# En la tercera columna, permite al usuario activar/desactivar la visualización de salarios en las barras del gráfico
with columna_mostrar_salarios:
    mostrar_salarios = st.toggle('Mostrar el sueldo en la barra')

# Extrae los nombres y salarios de los empleados para usar en el gráfico
nombres_empleados = datos_empleados['full name']
sueldos_empleados = datos_empleados['salary']

# Crea una figura y ejes para el gráfico
figura, ejes = plt.subplots()

# Si la opción de mostrar nombres está desactivada, oculta las etiquetas del eje y
if mostrar_nombres == False:
   ejes.set_yticks([])

# Si la opción de mostrar salarios está activada, crea barras horizontales con etiquetas de salario
if mostrar_salarios:
   barras = ejes.barh(nombres_empleados, sueldos_empleados, color=color_barras)
   # Agrega etiquetas de salario en cada barra
   for indice, barra in enumerate(barras):
      salario = sueldos_empleados[indice]
      ejes.annotate(f'{salario} €',
                     xy=(barra.get_width(), barra.get_y() + barra.get_height() / 2),
                     xytext=(5, 0),  # Ajusta la posición del texto
                     textcoords='offset points',
                     va='center', ha='left',
                     fontsize=10, color='black')

# Vuelve a crear las barras horizontales para asegurar que estén presentes en el gráfico
ejes.barh(nombres_empleados, sueldos_empleados, color=color_barras)

# Establece un límite en el eje x para mejorar la visualización del gráfico
plt.xlim(0,4500)

# Muestra el gráfico en la interfaz de Streamlit
st.pyplot(figura)

# Muestra un texto de la autora
st.write("© Hanane Arrazouki - CPIFP Alan Turing")