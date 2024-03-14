from src.api import api_request
from src.ui import show_menu, print_data, show_age_distribution_line_plot, show_age_distribution_violin_plot, show_municipality_distribution_pie_plot, show_contagion_type_distribution_pie_plot
from src.data_wrangling import data_wrangling

def main():

    df = api_request("RISARALDA", 10000)
    
    print("Describe before wrangling:\n", df.describe())
    
    data_wrangling(df)
    
    print("\nDescribe after wrangling:\n", df.describe())

    while True:
        show_menu()
        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            print_data(df)
        elif opcion == '2':
            show_age_distribution_line_plot(df)
        elif opcion == '3':
            show_age_distribution_violin_plot(df)
        elif opcion == '4':
            show_municipality_distribution_pie_plot(df)
        elif opcion == '5':
            show_contagion_type_distribution_pie_plot(df)
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

    

main()
