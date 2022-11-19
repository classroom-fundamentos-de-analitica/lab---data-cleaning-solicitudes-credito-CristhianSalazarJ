"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime as dt
import re


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    df_copy = df.copy()

    # Eliminación de datos faltantes y duplicados
    df_copy.dropna(axis = 0, inplace = True)
    df_copy.drop_duplicates(inplace = True)

    cols = ['sexo','tipo_de_emprendimiento','idea_negocio','barrio','línea_credito']

    for col in cols:
        df_copy[col] = df_copy[col].str.lower()
        df_copy[col] = df_copy[col].str.replace('_',' ')
        df_copy[col] = df_copy[col].str.replace('-',' ')

    # COLUMNA FECHA DE BENEFICIO
    df_copy['fecha_de_beneficio'] = df_copy['fecha_de_beneficio'].apply(
        lambda x: dt.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else dt.strptime(x, "%d/%m/%Y"))


    # COLUMNA MONTO DEL CREDITO
    df_copy.monto_del_credito = df_copy.monto_del_credito.str.replace(',','')
    df_copy.monto_del_credito = df_copy.monto_del_credito.str.replace('\.00','')
    df_copy.monto_del_credito = df_copy.monto_del_credito.str.replace('\$[\s*]','')
    df_copy.monto_del_credito.astype(int)

    # COLUMNA COMUNA CIUDADANO
    df_copy['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    df_copy.drop_duplicates(inplace = True)

    return df_copy


