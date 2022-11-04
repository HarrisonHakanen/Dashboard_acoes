from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from app import *
import funcoes
from app import *

from components import dashboards, altas_baixas,sidebar,previsoes,macd,bollinger,fechamento


ultimos_dias = 30

'''	
Acoes_lista = funcoes.GetAcoes(["YDUQ3.SA"],0)
negociacoes_param = Acoes_lista[0].negociacoes_param.tail(ultimos_dias).to_dict()
negociacoes_mes = Acoes_lista[0].negociacoes_mes.tail(ultimos_dias).to_dict()
sazonalidade_param = Acoes_lista[0].sazonalidade_param.tail(ultimos_dias).to_dict()
sazonalidade_mes = Acoes_lista[0].sazonalidade_mes.tail(ultimos_dias).to_dict()
'''

acoes_tickers = pd.read_csv("acoes_tickers.csv").to_dict()


app.layout = dbc.Container(children=[

	
	dcc.Store(id='store-negociacoes-param'),
	dcc.Store(id='store-negociacoes-mes'),
	dcc.Store(id='store-sazonalidade-param'),
	dcc.Store(id='store-sazonalidade-mes'),


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

	if pathname == "/macd":

		return macd.layout

	if pathname == "/bollinger":

		return bollinger.layout

	if pathname == "/fechamento":

		return fechamento.layout

  
if __name__ == '__main__':
    app.run_server(debug=True)




