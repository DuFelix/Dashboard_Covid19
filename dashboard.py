from black import read_cache

import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

from pyparsing import col

# df = pd.read_csv("HIST_PAINEL_COVIDBR_13mai2021.csv", sep=";")
# df_states = df[(~df["estado"].isna()) & (df["codmun"].isna())]
# df_states
# df_brasil = df[df["regiao"] == "Brasil"]
# df_brasil
# df_states.to_csv("df_states.csv")
# df_brasil.to_csv("df_brasil.csv")

df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

df_states_ = df_states[df_states["data"] == "2020-05-13"]

brazil_states = json.load(open("geojson/brazil_geo.json", "r"))
brazil_states

app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

fig = px.choropleth_mapbox(df_states_, locations="estado", color="casosNovos", 
center={"lat": -16.95, "lon": -47.78}, 
geojson=brazil_states, color_continuous_scale="redor", opacity=0.4, 
hover_data={"casosAcumulado": True, "casosNovos": True, "ObitosNovos": True, "Estado": True})

# =========================================== 
# Layout

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="choropleth-map", figure=fig)

        ])
    ])
)

if __name__ =="__main__":
    app.run_server(debug=True) 