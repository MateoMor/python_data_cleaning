import pandas as pd
from sodapy import Socrata


def api_request(departamento_nom, limite ):
    # Unauthenticated client only works with public data sets.
    client = Socrata("www.datos.gov.co", None)

    selected_data = "ciudad_municipio_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom"
    
    # The request is made
    results = client.get("gt2j-8ykr", limit=limite, departamento_nom=departamento_nom, select=selected_data)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return results_df