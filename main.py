from src.api import api_request
from src.ui import show_menu, print_data, show_age_distribution_plot, show_municipality_distribution, show_travel_country_distribution
from src.data_wrangling import data_wrangling

def main():

    df = api_request("RISARALDA", 10000)
    data_wrangling(df)

    while True:
        show_menu()
        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            print_data(df)
        elif opcion == '2':
            show_age_distribution_plot(df)
        elif opcion == '3':
            show_municipality_distribution(df)
        elif opcion == '4':
            show_travel_country_distribution(df)
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

    

main()
