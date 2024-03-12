from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
    
def show_menu():
    print("Seleccione una opción:")
    print("1. Imprimir datos")
    print("2. Mostrar distribución de edades")
    print("3. Mostrar distribución por municipio")
    print("4. Mostrar distribución por país de viaje")
    print("0. Salir")
    
def print_data(df):
    
    print()
    print(tabulate(df, headers=df.columns.tolist(), tablefmt = "double_grid"))

def show_age_distribution_plot(df):
    # Se agrupan las edad en intervalos de 10 años
    df['intervalo_edad'] = pd.cut(df['Edad'], bins=range(0, 111, 10), right=False)

    # Se cuenta el número de edades en cada intervalo
    distribucion_edades = df['intervalo_edad'].value_counts().sort_index()

    #print(df)

    plt.figure(figsize=(12, 6))
    plt.bar(distribucion_edades.index.astype(str), distribucion_edades.values)

    plt.title('Distribución de Contagiados por Edad')
    plt.xlabel('Intervalo de Edad')
    plt.ylabel('Cantidad de Personas')

    plt.show()
    
def show_municipality_distribution(df):
    # Contar el número de contagiados por municipio
    municipio_counts = df['Municipio'].value_counts()

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    municipio_counts.plot(kind='bar')
    
    # Configurar el título y las etiquetas
    plt.title('Distribución de Contagios por Municipio')
    plt.xlabel('Municipio')
    plt.ylabel('Número de Contagiados')
    
    # Mostrar el gráfico
    plt.xticks(rotation=90) 
    plt.tight_layout()  
    plt.show()

def show_travel_country_distribution(df):
    # Contar el número de contagiados por país de viaje
    pais_viaje_counts = df['Pais de viaje'].value_counts()

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    pais_viaje_counts.plot(kind='bar')
    
    # Configurar el título y las etiquetas
    plt.title('Distribución de Contagios por País de Viaje')
    plt.xlabel('País de Viaje')
    plt.ylabel('Número de Contagiados')
    
    # Mostrar el gráfico
    plt.xticks(rotation=90) 
    plt.tight_layout()  
    plt.show()
