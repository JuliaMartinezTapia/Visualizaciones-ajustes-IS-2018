
#Para leer archivos pfd

#From PyPDF2 import PdfFileReader

# pdfReader= PdfFileReader("Memoria Análisis ajustes 2018 -julio 2021.pdf")
# count = pdfReader.numPages
# all_page_text = ""
# for i in range(count)
# page = pdfReader.getPage(i)
# all_page_text = page.extractText()
# return all_page_text


#código para incluir la opción de subir un archivo por el usuario:

#@st.cache
#def cargar_datos(csv_path_1,uploader_csv):

    #if uploader_csv is None:
        #df1 = pd.read_csv(csv_path_1,encoding = "Latin",sep = ";")

    #else:
        #df1 = pd.read_csv(uploader_csv,encoding = "Latin",sep = ";")

    #return df1


#def comp(df_ajustes):

    #st.header("Composición de los ajustes para todos los sectores")

    #left_col, middle_col = st.beta_columns(2)

    #left_col.subheader("Aumentos")

    #comp_aum, comp_dism, todos_sort, todos_sort_dism = gr.comp(df_ajustes)

    #if left_col.button("Ver importes"):
        #tabla_aum = todos_sort[["Partidas", "Todos los sectores"]].set_index("Partidas")
        #st.dataframe(tabla_aum)

    #left_col.plotly_chart(comp_aum, use_container_width=True)


#left, right = st.beta_columns(2)

#with left:
    #st.subheader("Empresas españolas por tamaño")

    #fig_tam = bt.tamano(df_size)

    #st.plotly_chart(fig_tam, use_container_width=True)

    #st.write(df_size)

#with right:
    #st.subheader("Grandes empresas por sector")

    #st.write(df_sector)

    #st.line_chart(df_sector)


if st.sidebar.button("Ver cifras para todos los ajustes"):
    st.dataframe(df_ajustes)