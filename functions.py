import streamlit as st
import pandas as pd
from PIL import Image
import barcharts as bt
import graficas_tarta as gr
import pdfplumber
import plotly.express as px

def config_page():
    st.set_page_config(page_title = "Impuesto sobre Sociedades 2018",
    page_icon =":chart:",
    layout = "wide")

def home():

    st.title("Ajustes fiscales al Impuesto sobre Sociedades en España, 2018")

    st.write(" ")

    #img = Image.open("datos/Imagen de Pexels en Pixabay.jpg")
    #st.image(img,use_column_width="auto")

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

    sentido = st.sidebar.radio("¿Que tipo de ajuste quieres ver?",
                     options=['Aumentos', 'Disminuciones'])

    comp_aum, comp_dism, todos_sort, todos_sort_dism = gr.comp(df_ajustes)

    if sentido == "Aumentos":

        st.header("Composición de los ajustes de las grandes empresas (todos los sectores)")

        st.subheader("Aumentos")

        if st.button("Ver importes (miles €)"):
            tabla_aum = todos_sort[["Partidas", "Todos los sectores"]].set_index("Partidas")
            st.dataframe(tabla_aum)

        st.plotly_chart(comp_aum, use_container_width=True)

    elif sentido == "Disminuciones":

        st.title("Composición de los ajustes de las grandes empresas (todos los sectores)")

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

    nota_pie = '<p style="font-family:Arial; color:Black; font-size: 11px;">Ten en cuenta que puedes ampliar el gráfico de barras haciendo click en las flechas que aparecen arriba a la derecha, cuando pasas el ratón sobre el gráfico</p>'
    st.sidebar.markdown(nota_pie, unsafe_allow_html=True)

    aum, dism, figA, figB = bt.ajustes_agregado(df_ajustes, sector, tipo)

    if tipo == "Aumentos":
        if st.button("Ver importes (miles de €)"):
            aum = aum.set_index("Partidas")
            st.dataframe(aum)
        st.plotly_chart(figA,use_container_width=True)

    elif tipo == "Disminuciones":
        if st.button("Ver importes (miles de €)"):
            dism = dism.set_index("Partidas")
            st.dataframe(dism)
        st.plotly_chart(figB,use_container_width=True)



def analisis_ajuste(df_ajustes):

    df_ajustes_rev = df_ajustes[df_ajustes["Tipo"].str.startswith("Aumento") | df_ajustes["Tipo"].str.startswith("Disminución")]

    lista_ajustes = df_ajustes_rev.set_index("Partidas").T

    lista_ajustes = lista_ajustes.columns

    nombre_ajuste = st.sidebar.selectbox("Escoge el ajuste que quieres visualizar", lista_ajustes)

    st.header(nombre_ajuste)

    df_ajuste_elegido = df_ajustes_rev[df_ajustes_rev["Partidas"].str.startswith(nombre_ajuste)].drop(columns=["Todos los sectores", "Otras actividades financieras"])

    df_ajuste_graf = df_ajuste_elegido.drop(columns=["Tipo"]).set_index("Partidas").T

    if df_ajuste_graf.columns.size == 2:

        df_ajuste_graf.columns = ['Aumento', 'Disminución']

        if st.button("Ver cifras (miles de euros) "):
            st.dataframe(df_ajuste_graf)

        st.write(" ")

        left_col, right_col = st.beta_columns(2)

        left_col.write(" Aumento")
        fig_1 = bt.grafico_aumento(df_ajuste_graf.sort_values('Aumento'))
        left_col.plotly_chart(fig_1, use_container_width=True)

        right_col.write("Disminución")
        fig_2 = bt.grafico_disminucion(df_ajuste_graf.sort_values('Disminución'))
        right_col.plotly_chart(fig_2, use_container_width=True)

    else:

        df_ajuste_graf.reset_index(inplace=True)
        
        df_ajuste_graf.columns = ["Partidas", "Ajuste"]

        if st.button(" Ver cifras (miles de euros)"):
            st.dataframe(df_ajuste_graf)

        st.write(" ")

        fig_3= px.bar(df_ajuste_graf.sort_values('Ajuste'),
                        x="Partidas",
                        y="Ajuste",
                        color="Partidas",                        
                        labels={"index": "Sector", "Ajuste": "Importe (miles de euros)", "Partidas" : "Sector"},
                        height=500,
                        template="plotly_white",
                        hover_data = {"Sector": False,"Partidas":":."},
                        color_discrete_sequence=px.colors.sequential.Inferno_r)
        
        fig_3.update_layout(showlegend=False)

        st.plotly_chart(fig_3, use_container_width=True)

def otros_datos(df_size,df_sector):

    menu_otros = st.radio("Escoge lo que te interese",
                     options=["Empresas españolas por tamaño", "Grandes empresas por sector"])

    if menu_otros == "Empresas españolas por tamaño":

        st.subheader("Empresas españolas por tamaño")

        if st.button("Ver cifras"):
            st.dataframe(df_size)

        fig_tam = bt.tamano(df_size)

        st.plotly_chart(fig_tam,use_container_width=True)


    elif menu_otros == "Grandes empresas por sector":

        st.subheader("Grandes empresas por sector")

        if st.button("Ver cifras"):
            st.dataframe(df_size)

        fig_emp_sector = gr.emp_sector(df_sector)

        st.plotly_chart(fig_emp_sector, use_container_width=True)
