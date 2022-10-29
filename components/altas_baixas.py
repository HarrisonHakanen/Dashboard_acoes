from dash import html, dcc
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




layout = dbc.Col([

	#Card altas e baixas por parametro--------------------------
	dbc.Card([

		#grafico de negociações por parametro
		dbc.Row([
			html.H1("Altas e baixas por parâmetro", className="text-primary"),
			html.Hr(),

			dbc.Col([
				html.Legend("Grafico de altas e baixas por parâmetro", className="text-primary"),
				dbc.Card(dcc.Graph(id="grafico_altas_baixas_param"))
			]),

		],style={"padding": "25px"}),

		#tabela de altas e baixas por parametro
		dbc.Row([
			dbc.Col([
				html.Legend("Tabela de altas e baixas por parâmetro", className="text-primary"),
	        	html.Div(id="tabela_altas_baixas_param", className="dbc"),
			]),
		],style={"padding": "25px"}),
		

		#informações de altas e baixas por parametro
		dbc.Row([

			
			#valor de compra
			dbc.Col([

				html.Legend("Informações compra"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_param_max")
						]),
					]),

				]),

			],width = 3),



			#valor de venda
			dbc.Col([
				html.Legend("Informações venda"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_param_max")
						]),
					]),

				]),


			],width = 3),


			#lucro
			dbc.Col([

				html.Legend("Informações lucro"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_param_max")
						]),
					]),

				]),



			],width=3),

			#taxa de retorno
			dbc.Col([
				html.Legend("Informações taxa de retorno"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_param_max")
						]),
					]),

				]),



			],width=3),

		],style={"padding": "25px"}),
			
	]),






	#Card altas e baixas por mês--------------------------
	dbc.Card([

		#grafico de negociações por mes
		dbc.Row([
			html.H1("Altas e baixas por mês", className="text-primary"),
			html.Hr(),

			dbc.Col([
				html.Legend("Grafico de altas e baixas por mes", className="text-primary"),
				dbc.Card(dcc.Graph(id="grafico_altas_baixas_mes"))
			]),

		],style={"padding": "25px"}),

		#tabela de altas e baixas por mes
		dbc.Row([
			dbc.Col([
				html.Legend("Tabela de altas e baixas por mes", className="text-primary"),
	        	html.Div(id="tabela_altas_baixas_mes", className="dbc"),
			]),
		],style={"padding": "25px"}),
		

		#informações de altas e baixas por mes
		dbc.Row([

			
			#valor de compra
			dbc.Col([

				html.Legend("Informações compra"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_compra_altas_baixas_mes_max")
						]),
					]),

				]),

			],width = 3),



			#valor de venda
			dbc.Col([
				html.Legend("Informações venda"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_venda_altas_baixas_mes_max")
						]),
					]),

				]),


			],width = 3),


			#lucro
			dbc.Col([

				html.Legend("Informações lucro"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_altas_baixas_mes_max")
						]),
					]),

				]),



			],width=3),

			#taxa de retorno
			dbc.Col([
				html.Legend("Informações taxa de retorno"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_altas_baixas_mes_max")
						]),
					]),

				]),



			],width=3),

		],style={"padding": "25px"}),
			
	]),


])