###################### Función para cargar un archivo como un dataframe################################

def cargar_dataset(archivo):  #La entrada es un archivo
    import pandas as pd
    import os
    #Si se desea agregar un input se coloca:
#   archivo=input("Por favor, ingresa el nombre del archivo: ")
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df= pd.read_excel(archivo)
        return (df)
    elif extension == '.json':
        df= pd.read_json(archivo)
        return (df)
    elif extension == '.html':
        df= pd.read_html(archivo)
        return (df)
    else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")


#######################Función_Nulos_Promedio_Dataframe########################################
def nulos_prom_df(df):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas= df.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(round(cuantitativas.mean(), 1))
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    df = pd.concat([cuantitativas, cualitativas], axis=1)
    return(df)