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
	html.H1("Previsões", className="text-primary"),

	dbc.Row([
		dbc.Card([
			
			dbc.Row([
				html.Legend("Previsões de negociação por parametro", className="text-primary"),			
				dbc.Col([
					

					dbc.Card([
						html.H5("Previsão por LSTM", className="text-primary"),			
						html.Hr(),
						html.Table([
							html.Tr([
								html.Td([
									html.H5("Próxima compra")
								]),

								html.Td([
									html.H5(id="proxima_compra_param_LSTM")
								]),
							]),
							html.Tr([
								html.Td([
									html.H5("Próxima venda")
								]),

								html.Td([
									html.H5(id="proxima_venda_param_LSTM")
								]),
							]),

						]),
						],style={"padding": "25px"}),
				],width=6),



				dbc.Col([
					

					dbc.Card([
						html.H5("Previsão por médias móveis", className="text-primary"),			
						html.Hr(),
						html.Table([
							html.Tr([
								html.Td([
									html.H5("Próxima compra")
								]),

								html.Td([
									html.H5(id="proxima_compra_param_MM")
								]),
							]),
							html.Tr([
								html.Td([
									html.H5("Próxima venda")
								]),

								html.Td([
									html.H5(id="proxima_venda_param_MM")
								]),
							]),

						]),
						],style={"padding": "25px"}),
				],width=6),
			])

		]),

	],style={"padding": "25px"}),



	dbc.Row([
		dbc.Card([
			
			dbc.Row([
				html.Legend("Previsões de negociação por mês", className="text-primary"),			
				dbc.Col([
					

					dbc.Card([
						html.H5("Previsão por LSTM", className="text-primary"),			
						html.Hr(),
						html.Table([
							html.Tr([
								html.Td([
									html.H5("Próxima compra")
								]),

								html.Td([
									html.H5(id="proxima_compra_mes_LSTM")
								]),
							]),
							html.Tr([
								html.Td([
									html.H5("Próxima venda")
								]),

								html.Td([
									html.H5(id="proxima_venda_mes_LSTM")
								]),
							]),

						]),
						],style={"padding": "25px"}),
				],width=6),



				dbc.Col([
					

					dbc.Card([
						html.H5("Previsão por médias móveis", className="text-primary"),			
						html.Hr(),
						html.Table([
							html.Tr([
								html.Td([
									html.H5("Próxima compra")
								]),

								html.Td([
									html.H5(id="proxima_compra_mes_MM")
								]),
							]),
							html.Tr([
								html.Td([
									html.H5("Próxima venda")
								]),

								html.Td([
									html.H5(id="proxima_venda_mes_MM")
								]),
							]),

						]),
						],style={"padding": "25px"}),
				],width=6),
			])

		]),

	],style={"padding": "25px"}),


])