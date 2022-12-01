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
			dcc.RadioItems(id="radio_periodo",
			   options=[
			       {'label': 'Dia', 'value': 'Dia'},
			       {'label': 'Minuto', 'value': 'Minuto'},
			   ],value="Dia")
		]),

	],style={"padding": "25px"}),

	dbc.Row([

		dbc.Col([
			dbc.Button("Carregar ações", color="error", id="carregar_acoes", value="acoes", className="btn btn-success"),

		]),
	],style={"padding": "25px"}),

	html.Hr(),

	dbc.Row([

		html.H3("Ação selecionada"),
		
		dbc.Select(id="select_acao_selecionada"),

	],style={"padding": "25px"}),


	html.Hr(),

	dbc.Row([

		dbc.Col([
			dbc.Nav(
	        [
	        	dbc.NavLink("Fechamentos", href="/fechamento", active="exact"),
	            dbc.NavLink("Negociações", href="/dashboards", active="exact"),
	            #dbc.NavLink("Altas baixas", href="/altas_baixas", active="exact"),
	            dbc.NavLink("Previsões", href="/previsoes", active="exact"),
	            dbc.NavLink("Indicadores", href="/indicadores", active="exact"),
	        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}),
			
		]),

	],style={"padding": "25px"}),



	#MODAIS--------------------------------------
	dbc.Modal([
		dbc.ModalHeader(dbc.ModalTitle("Tipos de ações")),
		dbc.ModalBody([

			dbc.Row([

				dbc.Col([
					html.H5("Ações selecionadas", className="card-title"),
					html.Div(
			            dcc.Dropdown(
			            id="dropdown_acoes_selecionadas",
			            clearable=False,
			            style={"width": "100%"},
			            persistence=True,
			            persistence_type="session",
			            multi=True)                       
			        ),

				],width=4),

				dbc.Col([
					html.H5("Ações pesquisadas anteriormente", className="card-title"),
					html.Div(
		                dcc.Dropdown(
		                id="dropdown_acoes_anteriores",
		                clearable=False,
		                style={"width": "100%"},
		                persistence=True,
		                persistence_type="session",
		                multi=True)                       
		            ),

				],width=4),

				dbc.Col([
					html.H5("Ações Ibovespa", className="card-title"),
					html.Div(
		                dcc.Dropdown(
		                id="dropdown_acoes_ibov",
		                clearable=False,
		                style={"width": "100%"},
		                persistence=True,
		                persistence_type="session",
		                multi=True)                       
		            ),

				],width=4),

			]),


			html.Hr(),

			dbc.Row([
				dbc.Col([
					dcc.RadioItems(id="tipo_acoes",
					   options=[
					       {'label': 'Ações selecionadas', 'value': 'AcoesSelecionadas'},
					       {'label': 'Ações anteriores', 'value': 'AcoesAnteriores'},
					       {'label': 'Ações Ibovespa', 'value': 'AcoesIbovespa'}
					   ],value="AcoesSelecionadas")
				]),

			],style={"padding": "5px"}),

		]),
		dbc.ModalFooter([
			dbc.Button("Carregar",id="carregar_",color="success"),
		])
	],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_carregar_acoes",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True)
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
	Input("radio_periodo","value")

	])

def carregar_acoes(n,drop_data,neg_param,neg_mes,sazon_param,sazon_mes,periodo):
	
	
	#if("carregar_acoes_ibov"==ctx.triggered_id):
	#	data = pd.read_csv("Empresas_Ibovespa_19_11_2022.csv")

	#	return carregar_acoes_func(data["ações"].values.tolist())
	

	if("carregar_acoes"==ctx.triggered_id):

		return carregar_acoes_func(drop_data,periodo)

	return [[],[],neg_param,neg_mes,sazon_param,sazon_mes]


def carregar_acoes_func(data,periodo):
	
	informacoes = funcoes.PesquisarAcoes(data,periodo)

	value = [data[0]]
	
	options = [{'label':i,'value':i}for i in data]

	ultimos_dias = 30

	informacoes[0].to_csv("Arquivos/Info/negociacoes_param.csv")
	informacoes[1].to_csv("Arquivos/Info/negociacoes_mes.csv")
	informacoes[2].to_csv("Arquivos/Info/sazonalidade_param.csv")
	informacoes[3].to_csv("Arquivos/Info/sazonalidade_mes.csv")
	informacoes[4].to_csv("Arquivos/Info/fechamento.csv")

	return options,value,informacoes[0].to_dict(),informacoes[1].to_dict(),informacoes[2].to_dict(),informacoes[3].to_dict()		

'''
@app.callback(
    Output('modal_carregar_acoes','is_open'),
    Output("dropdown_acoes_selecionadas","options"),
    Output("dropdown_acoes_selecionadas","value"),
    Output("dropdown_acoes_anteriores","options"),
    Output("dropdown_acoes_anteriores","value"),
    Output("dropdown_acoes_ibov","options"),
    Output("dropdown_acoes_ibov","value"),
    Input('carregar_acoes_ibov','n_clicks'),
    State('modal_carregar_acoes','is_open'),
    Input("dropdown-acoes","value")
)

def modal_acoes(n1,is_open,drop_acoes):
	
	if "carregar_acoes_ibov"==ctx.triggered_id:
		
		fechamentos = pd.read_csv("Arquivos/Info/fechamento.csv")

		fechamentos = fechamentos["ticker"].unique()

		ibov = pd.read_csv("Empresas_Ibovespa_19_11_2022.csv")

		return [not is_open,drop_acoes,drop_acoes,fechamentos,fechamentos,ibov["ações"].values.tolist(),ibov["ações"].values.tolist()]

	return [is_open,[],[],[],[],[],[]]




@app.callback(
	Output("select_acao_selecionada","value"),
	Input("carregar_","n_clicks"),
	Input("tipo_acoes","value"),
	Input("dropdown_acoes_selecionadas","value"),
	Input("dropdown_acoes_anteriores","value"),
	Input("dropdown_acoes_ibov","value"),
	)

def carregar_definitivo(n,tipo_acoes,acoes_selecionadas,acoes_anteriores,acoes_ibov):
	if "carregar_"==ctx.triggered_id:
		

		if(tipo_acoes=="AcoesSelecionadas"):
			return carregar_acoes_func(acoes_selecionadas)

		
		elif(tipo_acoes=="AcoesAnteriores"):
			print(acoes_anteriores)

		
		else:
			return carregar_acoes_func(acoes_ibov)
			

	return []


	dbc.Row([

		dbc.Col([
			dbc.Button("Ações IBOVESPA", color="error", id="carregar_acoes_ibov", value="acoes", className="btn btn-warning"),

		]),
	],style={"padding": "25px"}),

'''