import streamlit as st
import pandas as pd
from PIL import Image
import notebook as nt
import graficas as gr

def config_page():
    st.set_page_config(page_title = "Impuesto sobre Sociedades 2018",
    page_icon =":chart:",
    layout = "wide")

@st.cache
def cargar_datos(csv_path_1,uploader_csv):

    if uploader_csv is None:
        df1 = pd.read_csv(csv_path_1,encoding = "Latin",sep = ";")

    else:
        df1 = pd.read_csv(uploader_csv,encoding = "Latin",sep = ";")

    return df1

def home():
    st.title("Ajustes fiscales al Impuesto sobre Sociedades en España, 2018")

    st.header("Objetivo y origen de los datos")

    img = Image.open("C:\\Users\\julia\\Desktop\\PROYECTOS\\Análisis ajustes IS 2018\\Imagen de Hermann Traub en Pixabay .jpg")
    st.image(img,use_column_width="auto")
    st.write(
        "Análisis de los ajustes al resultado contable practicados por las sociedades no financieras en el periodo impositivo 2018")

    with st.beta_expander("¿De dónde salen los datos utilizados para este análisis?"):
        st.write(
            "Los datos utilizados para el análisis se han extraído de las estadísticas relativas al Impuesto sobre Sociedades elaboradas por el servicio de estudios tributarios y estadísticos de la Agencia Estatal de la Administración Tributaria (AEAT).En particular, se ha utilizado la estadística de cuentas anuales no consolidadas del Impuesto sobre Sociedades para el 2018, sección ajustes al resultado contable de sociedades no financieras (excluyendo aseguradoras, entidades de crédito y IIC), apartado relativo a las sociedades no financieras por Dimensión de empresa y Sector (excluyendo entidades transparentes, exentas y cooperativas).Para acceder a los datos utilizados en el presente estudio pincha aquí.")

def comp(df_ajustes):

    st.title("Composición de los ajustes para todos los sectores")

    st.header("Aumentos")

    comp_aum,comp_dism,todos_sort,todos_sort_dism = gr.comp(df_ajustes)

    st.plotly_chart(comp_aum, use_container_width=True)

    #st.button("Ver importes")

    if st.button("Ver importes"):
        tabla_aum = todos_sort[["Partidas","Todos los sectores"]].set_index("Partidas")
        st.dataframe(tabla_aum)

    st.header("Disminuciones")

    st.plotly_chart(comp_dism, use_container_width=True)
    if st.button("Ver importes "):
        tabla_dism = todos_sort_dism[["Partidas", "Todos los sectores"]].set_index("Partidas")
        st.dataframe(tabla_dism)

def analisis_sector(df_ajustes):

    sectores = df_ajustes.columns[2:]
    #tipo = df_ajustes["Tipo"].unique()[1:]
    tipo = ["Aumentos","Disminuciones"]

    st.title("Análisis por sector económico")
    sector = st.sidebar.selectbox("Selecciona el sector que te interese",sectores)
    tipo = st.selectbox("Escoge si quieres ver los aumentos  o las disminuciones a la base imponible",tipo)

    aum, dism, figA, figB = nt.ajustes_agregado(df_ajustes, sector, tipo)

    if tipo == "Aumentos":
        st.plotly_chart(figA,use_container_width=True)
        if st.button("Ver importes"):
            aum = aum.set_index("Partidas")
            st.dataframe(aum)

    elif tipo == "Disminuciones":
        st.plotly_chart(figB,use_container_width=True)
        if st.button("Ver importes"):
            dism = dism.set_index("Partidas")
            st.dataframe(dism)

#def analisis_ajuste(df_ajustes):


def otros_datos(df_size,df_sector,df_ajustes):

    st.write("Empresas españolas por tamaño")
    st.write(df_size)
    st.area_chart(df_size)

    st.write("Grandes empresas por sector")
    st.write(df_sector)
    st.line_chart(df_sector)

