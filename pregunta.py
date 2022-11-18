"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    df_copy = df.copy()

    # Eliminación de datos faltantes y duplicados
    df_copy.dropna(axis = 0, inplace = True)
    df_copy.drop_duplicates(inplace = True)

    # COLUMNA SEXO
    df_copy['sexo'] = df_copy.sexo.str.lower()
    
    # COLUMNA TIPO EMPRENDIMIENTO
    df_copy['tipo_de_emprendimiento'] = df_copy.tipo_de_emprendimiento.str.lower()

    # COLUMNA IDEA DE NEGOCIO
    df_copy['idea_negocio'] = df_copy.idea_negocio.str.strip()
    df_copy['idea_negocio'] = df_copy.idea_negocio.str.strip('-')
    df_copy['idea_negocio'] = df_copy.idea_negocio.str.strip('_')
    df_copy['idea_negocio'] = df_copy.idea_negocio.str.replace(' ','_')
    df_copy['idea_negocio'] = df_copy.idea_negocio.str.replace('-','_')
    df_copy['idea_negocio'] = df_copy.idea_negocio.str.lower()
    
    # COLUMNA BARRIO
    df_copy['barrio'] = df_copy.barrio.str.strip()
    df_copy['barrio'] = df_copy.barrio.str.replace('.',' ')
    df_copy['barrio'] = df_copy.barrio.str.replace('  ',' ')
    df_copy['barrio'] = df_copy.barrio.str.strip('-')
    df_copy['barrio'] = df_copy.barrio.str.strip('_')
    df_copy['barrio'] = df_copy.barrio.str.replace(' ','_')
    df_copy['barrio'] = df_copy.barrio.str.replace('-','_')
    df_copy['barrio'] = df_copy.barrio.str.replace('__','_')
    df_copy['barrio'] = df_copy.barrio.str.replace('.','_')
    df_copy['barrio'] = df_copy.barrio.str.lower()
    df_copy.barrio = df_copy.barrio.str.replace('bel¿n','belen')
    df_copy.barrio = df_copy.barrio.str.replace('antonio_nari¿o','antonio_nariño')

    # COLUMNA FECHA DE BENEFICIO
    df_copy.fecha_de_beneficio = pd.to_datetime(df_copy.fecha_de_beneficio, infer_datetime_format=True, errors='coerce')
    df_copy.fecha_de_beneficio = df_copy.fecha_de_beneficio.dt.strftime("%d-%m-%Y")

    # COLUMNA LINEA DE CREDITO
    df_copy['línea_credito'] = df_copy.línea_credito.str.strip()
    df_copy['línea_credito'] = df_copy.línea_credito.str.strip('-')
    df_copy['línea_credito'] = df_copy.línea_credito.str.strip('_')
    df_copy['línea_credito'] = df_copy.línea_credito.str.strip('.')
    df_copy['línea_credito'] = df_copy.línea_credito.str.replace(' ','_')
    df_copy['línea_credito'] = df_copy.línea_credito.str.replace('.','_')
    df_copy['línea_credito'] = df_copy.línea_credito.str.replace('-','_')
    df_copy['línea_credito'] = df_copy.línea_credito.str.lower()
    df_copy.línea_credito = df_copy.línea_credito.str.replace('soli_diaria','solidaria')

    # COLUMNA MONTO DEL CREDITO
    df_copy.monto_del_credito = df_copy.monto_del_credito.str.replace(',','')
    df_copy.monto_del_credito = df_copy.monto_del_credito.str.replace('\.00','')
    df_copy.monto_del_credito = df_copy.monto_del_credito.str.replace('$','')
    df_copy.monto_del_credito.astype(int)

    # Corregir tipo de dato de la columna comuna_ciudadano
    df_copy['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    df_copy.drop_duplicates(inplace = True)

    return df_copy

