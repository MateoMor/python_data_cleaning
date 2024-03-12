import pandas as pd
import matplotlib.pyplot as plt

from src.api import api_request

#df = api_request("RISARALDA", 1000 )

#print(df)

#print(df.shape[0])

#print("Column Names::",df.columns.values.tolist())

#print("Columns with Missing Values::",df.columns[df.isnull().any()].tolist())
#print("Number of rows with Missing Values:", df.isnull().any(axis=1).sum())
#print("Sample Indices with missing data::", df.index[df.isnull().any(axis=1)].tolist()[:5] ) 

#print("General Stats::")
#print(df.info())
#print("Summary Stats::" )
#print(df.describe())

def imput_data(df):
    if 'pais_viajo_1_nom' in df.columns:
        df['pais_viajo_1_nom'].fillna(value="No Registra", inplace=True)

def type_casting(df):
    df['edad'] = pd.to_numeric(df.edad)

def rename_headers(df):
    new_names = {"ciudad_municipio_nom": "Municipio",  "edad": "Edad", "fuente_tipo_contagio": "Fuente de contagio", "estado": "Estado", "pais_viajo_1_nom": "Pais de viaje"}
    df.rename(columns=new_names, inplace=True)

def data_wrangling(df):
    imput_data(df)
    type_casting(df)
    rename_headers(df)

