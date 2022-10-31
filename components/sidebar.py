from dash import html, dcc,ctx
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app
from dash import dash_table

import pdb
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO
import funcoes



layout = dbc.Col([

	dbc.Row([
		dbc.Col([

			html.H3("Pesquisar ações", className="card-title"),
            html.Div(
                dcc.Dropdown(
                id="dropdown-acoes",
                clearable=False,
                style={"width": "100%"},
                persistence=True,
                persistence_type="session",
                multi=True)                       
            ),


		]),


	],style={"padding": "25px"}),

	dbc.Row([

		dbc.Col([
			dbc.Button("Carregar ações", color="error", id="carregar_acoes", value="acoes", className="btn btn-success"),

		]),
	],style={"padding": "25px"}),


		html.Hr(),
	dbc.Row([

		html.H3("Ações selecionadas"),
		
		dbc.Select(id="select_acao_selecionada"),

	],style={"padding": "25px"}),

	html.Hr(),

	dbc.Row([

		dbc.Col([
			dbc.Nav(
	        [
	            dbc.NavLink("Negociações", href="/dashboards", active="exact"),
	            dbc.NavLink("Altas baixas", href="/altas_baixas", active="exact"),
	            dbc.NavLink("Previsões", href="/previsoes", active="exact"),
	            dbc.NavLink("MACD", href="/macd", active="exact"),
	            dbc.NavLink("Bollinger", href="/bollinger", active="exact"),
	        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}),
			
		]),

	],style={"padding": "25px"}),

	



])




@app.callback(
	[Output("dropdown-acoes", "options"),
	Input("tickers","data")]
)

def popula_dropdown(data):

	df = pd.DataFrame(data)
	
	val = df.Acoes.unique().tolist()

	return [([{"label": x, "value": x} for x in df.Acoes.unique()])]


@app.callback(Output("select_acao_selecionada","options"),
	Output("select_acao_selecionada","value"),

	Output("store-negociacoes-param","data"),
	Output("store-negociacoes-mes","data"),

	Output("store-sazonalidade-param","data"),
	Output("store-sazonalidade-mes","data"),

	[
	
	Input("carregar_acoes","n_clicks"),
	Input("dropdown-acoes","value"),

	Input("store-negociacoes-param","data"),
	Input("store-negociacoes-mes","data"),

	Input("store-sazonalidade-param","data"),
	Input("store-sazonalidade-mes","data"),

	])

def carregar_acoes(n,drop_data,neg_param,neg_mes,sazon_param,sazon_mes):
	
	if("carregar_acoes"==ctx.triggered_id):
		
		data = drop_data

		informacoes = funcoes.PesquisarAcoes(data)


		value = [data[0]]
		options = [{'label':i,'value':i}for i in data]

		ultimos_dias = 30

		
		informacoes[0].to_csv("Arquivos/negociacoes_param.csv")
		informacoes[1].to_csv("Arquivos/negociacoes_mes.csv")
		informacoes[2].to_csv("Arquivos/sazonalidade_param.csv")
		informacoes[3].to_csv("Arquivos/sazonalidade_mes.csv")


		
		return options,value,informacoes[0].to_dict(),informacoes[1].to_dict(),informacoes[2].to_dict(),informacoes[3].to_dict()

	return [[],[],neg_param,neg_mes,sazon_param,sazon_mes]


		

	