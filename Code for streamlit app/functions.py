import streamlit as st
import pandas as pd
from PIL import Image
import barcharts as bt
import graficas_tarta as gr
import pdfplumber

def config_page():
    st.set_page_config(page_title = "Impuesto sobre Sociedades 2018",
    page_icon =":chart:",
    layout = "wide")


def home():

    st.title("Ajustes fiscales al Impuesto sobre Sociedades en España, 2018")

    st.write(" ")

    img = Image.open("datos/Imagen de Pexels en Pixabay.jpg")
    st.image(img,use_column_width="auto")

    st.header("Objetivo")

    st.markdown("**Visualización de los ajustes al resultado contable practicados por las grandes empresas no financieras en el periodo impositivo 2018**")

    st.subheader("¿De dónde salen los datos?")

    st.markdown("Los datos utilizados para el análisis se han extraído de las estadísticas relativas al Impuesto sobre Sociedades elaboradas por el servicio de estudios tributarios y estadísticos de la Agencia Estatal de la Administración Tributaria (AEAT)\n"
                "\n En particular, se ha utilizado la estadística de cuentas anuales no consolidadas del Impuesto sobre Sociedades para el 2018, sección ajustes al resultado contable de sociedades no financieras (excluyendo aseguradoras, entidades de crédito y IIC), apartado relativo a las sociedades no financieras por dimensión de empresa y sector (excluyendo entidades transparentes, exentas y cooperativas)")


    with st.beta_expander("Información adicional sobre el proyecto"):
        with pdfplumber.open("Memoria Análisis ajustes 2018 -julio 2021.pdf") as pdf:
            pages_1 = pdf.pages[1]
            st.write(pages_1.extract_text())

    with st.sidebar.beta_expander("Datos"):
        st.markdown("Puedes acceder a los datos utilizados en el presente estudio en el siguiente "
        "[enlace](https://www.agenciatributaria.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/sociedadest2/2018/jrubikf93ce72b23694698d1488983ab0caa1f22b8d675.html)")

    with st.sidebar.beta_expander("Detalle de las agrupaciones sectoriales"):
        st.markdown("También puedes encontrar más información respecto de las agrupaciones sectoriales que utiliza la AEAT en el siguiente ""[enlace](https://www.agenciatributaria.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/sociedadest2/2018/docf15e3090a8e97d34e39533482da36a603374ebd1f.html)")



def comp(df_ajustes):

    st.header("Composición de los ajustes de las grandes empresas (todos los sectores)")

    st.subheader("Aumentos")

    comp_aum, comp_dism, todos_sort, todos_sort_dism = gr.comp(df_ajustes)

    if st.button("Ver importes (miles €)"):
        tabla_aum = todos_sort[["Partidas", "Todos los sectores"]].set_index("Partidas")
        st.dataframe(tabla_aum)

    st.plotly_chart(comp_aum, use_container_width=True)


    st.subheader("Disminuciones")

    if st.button("Ver importes (miles €) "):
        tabla_dism = todos_sort_dism[["Partidas", "Todos los sectores"]].set_index("Partidas")
        st.dataframe(tabla_dism)

    st.plotly_chart(comp_dism, use_container_width=True)

#Sección "Ajustes fiscales por sector"

def analisis_sector(df_ajustes):

    sectores = df_ajustes.columns[2:]
    tipo = ["Aumentos","Disminuciones"]

    st.header("Análisis por sector económico")
    sector = st.sidebar.selectbox("Selecciona el sector que te interese",sectores)
    tipo = st.selectbox("Escoge si quieres ver los aumentos  o las disminuciones a la base imponible",tipo)

    #Defino un formato para las notas al pie:

    nota_pie = '<p style="font-family:Arial; color:Black; font-size: 11px;">Recuerda que puedes ampliar el gráfico de barras cerando el panel de control, o bien haciendo click en las flechas que aparecen arriba a la derecha en el gráfico</p>'
    st.sidebar.markdown(nota_pie, unsafe_allow_html=True)

    aum, dism, figA, figB = bt.ajustes_agregado(df_ajustes, sector, tipo)

    if tipo == "Aumentos":
        st.plotly_chart(figA,use_container_width=True)
        if st.button("Ver importes (miles de €)"):
            aum = aum.set_index("Partidas")
            st.dataframe(aum)

    elif tipo == "Disminuciones":
        st.plotly_chart(figB,use_container_width=True)
        if st.button("Ver importes (miles de €)"):
            dism = dism.set_index("Partidas")
            st.dataframe(dism)


#def analisis_ajuste(df_ajustes):


def otros_datos(df_size,df_sector):

    st.write("Empresas españolas por tamaño")
    st.write(df_size)
    st.area_chart(df_size)

    st.write("Grandes empresas por sector")
    st.write(df_sector)
    st.line_chart(df_sector)



#código para incluir la opción de subir un archivo por el usuario:

#@st.cache
#def cargar_datos(csv_path_1,uploader_csv):

    #if uploader_csv is None:
        #df1 = pd.read_csv(csv_path_1,encoding = "Latin",sep = ";")


    #else:
        #df1 = pd.read_csv(uploader_csv,encoding = "Latin",sep = ";")

    #return df1