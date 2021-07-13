import plotly.express as px
import pandas as pd


def comp(df_ajustes):#la función se puede simplificar pero la dejo así por ahora

    #AUMENTOS
    ajustes_aum = df_ajustes[df_ajustes["Tipo"].isin(["Aumento"])][["Partidas", "Tipo", "Todos los sectores"]]
    todos_sort = ajustes_aum.sort_values("Todos los sectores", ascending=False)
    # Guardo en un df los 5 ajustes más relevantes y agrupo el resto en la categoría "otros ajustes".
    # the top 5
    todos_pie = todos_sort[:5].copy()
    # others
    new_row = pd.DataFrame(data={
        "Partidas": ["Otros ajustes"],
        "Todos los sectores": [todos_sort["Todos los sectores"][5:].sum()]
    })
    # combining top 5 with others
    todos_pie_aum = pd.concat([todos_pie, new_row])

    # Gráfico de tarta con Plotly, aumentos a la base imponible
    comp_aum  = px.pie(todos_pie_aum,
                 values="Todos los sectores",
                 names='Partidas',
                 #title='Aumentos a la base imponible',
                 template="plotly_dark",
                 labels={'Todos los sectores': 'Importe en miles de euros', "Partidas": "Ajuste fiscal"},
                 color_discrete_sequence=px.colors.sequential.Turbo_r)

    comp_aum.update_traces(textposition='inside', textinfo='percent')

    #DISMINUCIONES
    ajustes_dism = df_ajustes[df_ajustes["Tipo"].isin(["Disminución"])][["Partidas", "Tipo", "Todos los sectores"]]
    todos_sort_dism = ajustes_dism.sort_values("Todos los sectores", ascending=False)
    #Guardo en un df los 5 ajustes más relevantes y agrupo el resto en la categoría "otros ajustes".
    # the top 5
    todos_pie = todos_sort_dism[:5].copy()
    # others
    new_row = pd.DataFrame(data={
        "Partidas": ["Otros ajustes"],
        "Todos los sectores": [todos_sort_dism["Todos los sectores"][5:].sum()]
    })
    # combining top 5 with others
    todos_pie_dism = pd.concat([todos_pie, new_row])

    # Gráfico de tarta con Plotly, disminuciones a la base imponible
    comp_dism = px.pie(todos_pie_dism,
                 values="Todos los sectores",
                 names='Partidas',
                 #title='Disminuciones a la base imponible',
                 template="plotly_dark",
                 labels={'Todos los sectores': 'Importe en miles de euros', "Partidas": "Ajuste fiscal"},
                 color_discrete_sequence=px.colors.sequential.thermal)

    comp_dism.update_traces(textposition='inside', textinfo='percent')

    return comp_aum,comp_dism,todos_sort,todos_sort_dism