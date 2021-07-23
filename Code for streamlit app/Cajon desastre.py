
#Para leer archivos pfd

#From PyPDF2 import PdfFileReader

# pdfReader= PdfFileReader("Memoria Análisis ajustes 2018 -julio 2021.pdf")
# count = pdfReader.numPages
# all_page_text = ""
# for i in range(count)
# page = pdfReader.getPage(i)
# all_page_text = page.extractText()
# return all_page_text





#def comp(df_ajustes):

    #st.header("Composición de los ajustes para todos los sectores")

    #left_col, middle_col = st.beta_columns(2)

    #left_col.subheader("Aumentos")

    #comp_aum, comp_dism, todos_sort, todos_sort_dism = gr.comp(df_ajustes)

    #if left_col.button("Ver importes"):
        #tabla_aum = todos_sort[["Partidas", "Todos los sectores"]].set_index("Partidas")
        #st.dataframe(tabla_aum)

    #left_col.plotly_chart(comp_aum, use_container_width=True)