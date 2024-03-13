from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
    
def show_menu():
    print("Seleccione una opción:")
    print("1. Imprimir datos")
    print("2. Mostrar distribución de edades (gráfico de lineas)")
    print("3. Mostrar distribución de edades (gráfico de violin)")
    print("4. Mostrar distribución por municipio")
    print("5. Mostrar distribución por país de viaje")
    print("0. Salir")
    
def print_data(df):
    print()
    print(tabulate(df, headers=df.columns.tolist(), tablefmt = "double_grid"))

def show_age_distribution_line_plot(df):
    
    # Este dataframe tiene como indice las edades y para cada una cuantas personas tienen esa edad
    edad_counts = df['Edad'].value_counts().sort_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(edad_counts.index, edad_counts.values, linestyle='-')
    
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Número de Personas')
    
    plt.grid(True)
    plt.show()
    
def show_age_distribution_violin_plot(df):
    
    plt.figure(figsize=(12, 6))
    sns.violinplot(x=df['Edad'], color='skyblue')
    
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Número de Personas')
    
    plt.grid(True)
    plt.show()

    
def show_municipality_distribution_bar_plot(df):

    municipio_counts = df['Municipio'].value_counts()

    plt.figure(figsize=(10, 6))
    municipio_counts.plot(kind='bar')

    plt.title('Distribución de Contagios por Municipio')
    plt.xlabel('Municipio')
    plt.ylabel('Número de Contagiados')
    
    plt.xticks(rotation=90) 
    plt.tight_layout()  
    plt.show()

def show_travel_country_distribution_bar_plot(df):

    pais_viaje_counts = df['Pais de viaje'].value_counts()
    
    plt.figure(figsize=(10, 6))
    pais_viaje_counts.plot(kind='bar')
    
    plt.title('Distribución de Contagios por País de Viaje')
    plt.xlabel('País de Viaje')
    plt.ylabel('Número de Contagiados')
    
    plt.xticks(rotation=90) 
    plt.tight_layout()  
    plt.show()
