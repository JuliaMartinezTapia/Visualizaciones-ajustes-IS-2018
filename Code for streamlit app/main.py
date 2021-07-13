
import streamlit as st
import functions as ft
import pandas as pd
import notebook as nt


csv_path_1 = "C:\\Users\\julia\\Desktop\\PROYECTOS\\Análisis ajustes IS 2018\\Distribucion sociedades por tamaño 2018.csv"
csv_path_2 = "C:\\Users\\julia\\Desktop\\PROYECTOS\\Análisis ajustes IS 2018\\Grandes emp por sector para visualizacion.csv"
csv_path_3 = "C:\\Users\\julia\\Desktop\\PROYECTOS\\Análisis ajustes IS 2018\\dataset ajustes IS 2018 CCAA.csv"

ft.config_page()

uploader_csv = st.sidebar.file_uploader("Sube tus datos",type=("csv"))
#st.write(uploader_csv)

#Primer dataframe. Creo una función con la opción de subirlo por el usuario.
df_size = ft.cargar_datos(csv_path_1,uploader_csv)
df_size = df_size.iloc[:3,:2]

#segundo dataframe
df_sector = pd.read_csv(csv_path_2)

#tercer dataframe
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


menu = st.sidebar.selectbox("Opciones:",("Objetivo","Composición","Análisis por sector","Análisis por ajuste","Otros datos"))

if menu == "Objetivo":
    ft.home()

elif menu == "Composición":
    ft.comp(df_ajustes)

elif menu == "Análisis por sector":
    ft.analisis_sector(df_ajustes)

#elif menu == "Análisis por ajuste":
    #ft.analisis_ajuste(df_ajustes)

elif menu == "Otros datos":
    ft.otros_datos(df_size,df_sector,df_ajustes)


