from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
    
def show_menu():
    print("Seleccione una opción:")
    print("1. Imprimir datos")
    print("2. Mostrar distribución de edades (gráfico de líneas)")
    print("3. Mostrar distribución de edades (gráfico de violín)")
    print("4. Mostrar distribución por municipio")
    print("5. Mostrar distribución del tipo de contagio (gráfico de pastel)")
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

    
def show_municipality_distribution_pie_plot(df):
    municipio_counts = df['Municipio'].value_counts()
    total_contagios = municipio_counts.sum()

    porcentajes = municipio_counts / total_contagios * 100

    otros = porcentajes[porcentajes < 2]
    otros_total = otros.sum()

    porcentajes = porcentajes[porcentajes >= 2]
    porcentajes['Otros'] = otros_total

    plt.figure(figsize=(10, 6))
    porcentajes.plot(kind='pie', autopct='%1.1f%%', startangle=140)

    plt.title('Distribución de Contagios por Municipio')
    plt.axis('equal')
    plt.ylabel('')

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

def show_contagion_type_distribution_pie_plot(df):
    
    contagion_type_counts = df['Fuente de contagio'].value_counts()

    threshold = df.shape[0] * 0.05
    contagion_type_counts['Otros'] = contagion_type_counts[contagion_type_counts < threshold].sum()
    contagion_type_counts = contagion_type_counts[contagion_type_counts >= threshold]

    plt.figure(figsize=(8, 8))
    plt.pie(contagion_type_counts, labels=contagion_type_counts.index, autopct='%1.1f%%', startangle=140)

    plt.title('Distribución del Fuente de contagio')

    plt.axis('equal')
    plt.show()