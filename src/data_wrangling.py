import pandas as pd

def imput_data(df):
    if 'pais_viajo_1_nom' in df.columns:
        df['pais_viajo_1_nom'] = df['pais_viajo_1_nom'].fillna(value="No Registra")

def type_casting(df):
    df['edad'] = pd.to_numeric(df.edad)

def rename_headers(df):
    new_names = {"ciudad_municipio_nom": "Municipio",  "edad": "Edad", "fuente_tipo_contagio": "Fuente de contagio", "estado": "Estado", "pais_viajo_1_nom": "Pais de viaje"}
    df.rename(columns=new_names, inplace=True)

def data_wrangling(df):
    imput_data(df)
    type_casting(df)
    rename_headers(df)

