
import streamlit as st
import functions as ft
import pandas as pd
import barcharts as nt

#import pdfplumber


csv_path_1 = "datos/Distribucion sociedades por tamaño 2018.csv"
csv_path_2 = "datos/Grandes emp por sector para visualizacion.csv"
csv_path_3 = "datos/dataset ajustes IS 2018 CCAA.csv"

## Basic setup and app layout

ft.config_page()
st.sidebar.title("Panel de control")

#Importo los csv con los datos en formato dataframe

#Dataframe sociedades por tamaño
df_size = pd.read_csv(csv_path_1,sep=";",encoding = "Latin")
df_size = df_size.iloc[:3,:2]

##Dataframe grandes empresas por sector
df_sector = pd.read_csv(csv_path_2)

#Dataframe ajustes IS 2018
df_ajustes = pd.read_csv(csv_path_3,sep=";",encoding = "Latin")
df_ajustes.columns = ['Partidas',
                      'Tipo',
                      'Todos los sectores',
                      "Agricultura y ganadería",
                      "Industria extractiva",
                      "Industria manufacturera",
                      "Construcción y act.inmob",
                      "Comercio, reparaciones y transporte",
                      "Información y comunicaciones",
                      "Act. profesionales y científicas",
                      "Educación y act. sanitarias",
                      "Hostelería y ocio",
                      "Otras actividades financieras"]



menu = st.sidebar.selectbox("Elige una sección",("Contexto","A primera vista","Ajustes fiscales por sector","Análisis ajuste por ajuste"))

if menu == "Contexto":
    ft.home()

elif menu == "A primera vista":

    menu_2 = st.sidebar.selectbox("Elige una opción", ("Empresas españolas por tamaño y sector", "Ajustes fiscales de grandes empresas"))

    if menu_2 == "Empresas españolas por tamaño y sector":
        ft.otros_datos(df_size,df_sector)
    elif menu_2 == "Ajustes fiscales de grandes empresas":
        ft.comp(df_ajustes)

elif menu == "Ajustes fiscales por sector":
    ft.analisis_sector(df_ajustes)

#elif menu == "Análisis ajuste por ajuste":
    #ft.analisis_ajuste(df_ajustes)



#Código para subir un archivo:
#uploader_csv = st.sidebar.file_uploader("Sube tus datos",type=("csv"))
#para archivos: uploaded_file = st.file_uploader('Sube to archivo', type="pdf")
#st.write(uploader_csv)
#Primer dataframe. Creo una función con la opción de subirlo por el usuario.
#df_size = ft.cargar_datos(csv_path_1,uploader_csv)
#df_size = df_size.iloc[:3,:2]