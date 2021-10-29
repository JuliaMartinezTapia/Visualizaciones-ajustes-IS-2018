
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

    #Preparo los dataframe

    aum = df_ajustes[df_ajustes["Tipo"].isin(["Aumento"])][["Partidas", sector]].sort_values(sector, ascending=False)
    dism = df_ajustes[df_ajustes["Tipo"].isin(["Disminución"])][["Partidas", sector]].sort_values(sector, ascending=False)

    #Gráfica aumentos

    figA = px.bar(aum, x=sector, y="Partidas",
                  color='Partidas',
                  labels= {sector: "Importe (miles de euros)", "Partidas":"Ajuste fiscal"},
                  height=500,
                  template="plotly_white",    
                  hover_data= {sector : ":.", "Partidas" : False},
                  color_discrete_sequence=px.colors.sequential.Inferno)
              
    figA.update_layout(title_text=sector, font=dict(size=9),showlegend=False)

    # Gráfica disminuciones

    figB = px.bar(dism, x=sector, y="Partidas",
                  color='Partidas',
                  labels={sector: "Miles de euros", "Partidas": "Ajuste fiscal"},
                  height=500,
                  template="plotly_white",
                  color_discrete_sequence=px.colors.sequential.Inferno,
                  hover_data={sector: False, "Partidas": False})

    figB.update_layout(title_text=sector, font=dict(size=9),showlegend=False)


    return aum,dism,figA,figB


def tamano(df_size):

    fig_tam = px.bar(df_size,
                 x='Num. Compañías',
                 y='Tamaño',
                 template="plotly_white",
                 color = "Tamaño",
                 color_discrete_sequence=px.colors.sequential.Hot,
                 labels={  # replaces default labels by column name
                     "Tamaño": "Tipo de empresa", "Num. Compañías": "Número de empresas"})

    return fig_tam


def grafico_aumento(df_ajuste_graf):

    fig_1 = px.bar(df_ajuste_graf,
                   x=df_ajuste_graf.index,
                   y="Aumento",
                   color=df_ajuste_graf.index,
                   labels={"index": " ", "Aumento":"miles de euros"},
                   height=500,
                   template="plotly_white",
                    hover_data=["Aumento"],
                   color_discrete_sequence=px.colors.sequential.Inferno_r)
    
    fig_1.update_layout(showlegend=False)
    
    return fig_1

def grafico_disminucion(df_ajuste_graf):

    fig_2 = px.bar(df_ajuste_graf,
                 x=df_ajuste_graf.index,
                 y="Disminución",
                 color=df_ajuste_graf.index,
                labels={"index": " ", "Disminución": "miles de euros"},
                height=500,
                 template="plotly_white",
                 hover_data=["Disminución"],
                color_discrete_sequence=px.colors.sequential.Inferno_r)
    
    fig_2.update_layout(showlegend=False)

    return fig_2



