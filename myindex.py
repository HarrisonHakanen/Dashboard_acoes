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

from components import dashboards, altas_baixas,sidebar,previsoes


ultimos_dias = 30

Acoes_lista = funcoes.GetAcoes(["YDUQ3.SA"],0)
negociacoes_param = Acoes_lista[0].negociacoes_param.tail(ultimos_dias).to_dict()
negociacoes_mes = Acoes_lista[0].negociacoes_mes.tail(ultimos_dias).to_dict()


sazonalidade_param = Acoes_lista[0].sazonalidade_param.tail(ultimos_dias).to_dict()
sazonalidade_mes = Acoes_lista[0].sazonalidade_mes.tail(ultimos_dias).to_dict()


acoes_tickers = pd.read_csv("acoes_tickers.csv").to_dict()


#print(info)

app.layout = dbc.Container(children=[

	dcc.Store(id='store-negociacoes-param', data=negociacoes_param),
	dcc.Store(id='store-negociacoes-mes', data=negociacoes_mes),
	dcc.Store(id='store-sazonalidade-param', data=sazonalidade_param),
	dcc.Store(id='store-sazonalidade-mes', data=sazonalidade_mes),


	dcc.Store(id='tickers', data=acoes_tickers),




    dbc.Row([
    	dbc.Col([

			sidebar.layout

		],md=2),
        dbc.Col([
        	dcc.Location(id="url"),
            html.Div(id="page-content")


        ], md=10),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")



@app.callback(

	Output("page-content", "children"), 
	[Input("url", "pathname")])



def render_page_content(pathname):

	print(pathname)
	if pathname == "/" or pathname == "/dashboards":
	

		return dashboards.layout

	if pathname == "/altas_baixas":

		return altas_baixas.layout

	if pathname == "/previsoes":

		return previsoes.layout

   
if __name__ == '__main__':
    app.run_server(debug=True)




