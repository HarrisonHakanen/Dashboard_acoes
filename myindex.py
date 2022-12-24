from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from app import *
import funcoes
from app import *
from components import dashboards, altas_baixas,sidebar,previsoes,macd,bollinger,fechamento,indicadores,configuracoes

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

	dcc.Store(id='Macd_store',data=[12,26,9]),
	dcc.Store(id='Bollinger_store',data=[10,1.5,1.5]),
	dcc.Store(id='Rsi_store',data=[0.3,0.7,14]),
	dcc.Store(id='CandleStick_store',data=[0,0]),
	dcc.Store(id='Sar_store',data=[0.2,0.2]),
	dcc.Store(id='ForceIndex_store',data=[21]),
	dcc.Store(id='Aroon_store',data=[25]),
	dcc.Store(id='Adx_store',data=[14]),
	dcc.Store(id='Stc_store',data=[50,23,10,3,3]),

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
	if pathname == "/negociacoes":
	
		return dashboards.layout


	if pathname == "/previsoes":

		return previsoes.layout


	if pathname == "/fechamento":

		return fechamento.layout


	if pathname == "/" or pathname == "/indicadores":

		return indicadores.layout


	if pathname == "/configuracoes":

		return configuracoes.layout

  
if __name__ == '__main__':
    app.run_server(debug=True)