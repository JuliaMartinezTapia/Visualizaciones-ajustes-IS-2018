
import plotly.express as px
import pandas as pd

def ajustes_agregado(df_ajustes,sector,tipo):
    """
    Funcion que pinta dos gráficas de barras que muestran los principales ajustes fiscales (aumentos y disminuciones)
    al Impuesto sobre Sociedades ejercicio 2018 para cada sector económico.

    En primer lugar la función aplica una máscara que filtra el dataset según el tipo del ajuste sea aumento o disminución.

    Despues ordena los valores de los ajustes tipo aumento y genera su gráfica.

    Por último, ordena los valores de los ajustes tipo disminución y genera la gráfica.
    """

    aum = df_ajustes[df_ajustes["Tipo"].isin(["Aumento"])][["Partidas", sector]].sort_values(sector, ascending=False)
    dism = df_ajustes[df_ajustes["Tipo"].isin(["Disminución"])][["Partidas", sector]].sort_values(sector, ascending=False)

    aum[sector] = aum[sector]
    dism[sector] = dism[sector]

    figA = px.bar(aum, x=sector, y="Partidas",
                  color='Partidas',
                  labels={sector: 'Importe en miles de euros', "Partidas": " "}, height=500,
                  template="plotly_dark",
                  hover_name="Partidas",
                 color_discrete_sequence=px.colors.sequential.Turbo_r)


    figA.update_layout(title_text=sector, font=dict(size=9))

    #figA.show()

    figB = px.bar(dism, x=sector, y="Partidas",
                  color='Partidas',
                  labels={sector: 'Importe en miles de euros', "Partidas": ""}, height=500,
                  template="plotly_dark",
                  hover_name="Partidas",
                  color_discrete_sequence=px.colors.sequential.Turbo_r)

    figB.update_layout(title_text=sector, font=dict(size=9))

    #figB.show()

    return aum,dism,figA,figB
