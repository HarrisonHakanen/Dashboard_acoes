from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# import from folders
from app import *
from components import dashboards

import funcoes
from app import *

from components import dashboards


Acoes_lista = funcoes.GetAcoes(["YDUQ3.SA"],0)
negociacoes_param = Acoes_lista[0].negociacoes_param.tail(30).to_dict()
negociavoes_mes = Acoes_lista[0].negociacoes_mes.tail(30).to_dict()

#print(info)

app.layout = dbc.Container(children=[

	dcc.Store(id='store-negociacoes-param', data=negociacoes_param),
	dcc.Store(id='store-negociacoes-mes', data=negociavoes_mes),



    dbc.Row([
        dbc.Col([
        	dcc.Location(id="url"),
            html.Div(id="page-content")


        ], md=12),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")



@app.callback(

	Output("page-content", "children"), 
	[Input("url", "pathname")])



def render_page_content(pathname):

	print(pathname)
	if pathname == "/" or pathname == "/dashboards":
	

		return dashboards.layout

   
if __name__ == '__main__':
    app.run_server(debug=True)