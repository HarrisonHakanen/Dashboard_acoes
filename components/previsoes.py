from dash import html, dcc, ctx
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


	dbc.Row([

		dbc.Col([
			dbc.Button("Realizar previsões", color="error", id="realizar_previsoes", value="acoes", className="btn btn-warning"),

		],width=6),

	],style={"padding": "25px"}),
])


@app.callback(
	Output("proxima_compra_param_LSTM","children"),
	Output("proxima_venda_param_LSTM","children"),

	Output("proxima_compra_param_MM","children"),
	Output("proxima_venda_param_MM","children"),

	Output("proxima_compra_mes_LSTM","children"),
	Output("proxima_venda_mes_LSTM","children"),

	Output("proxima_compra_mes_MM","children"),
	Output("proxima_venda_mes_MM","children"),

	Input("realizar_previsoes","n_clicks"),
	Input("select_acao_selecionada","value"),

)

def realizar_previsoes(btn_realizarPrevisoes,acao_selecionada):

	if("realizar_previsoes"==ctx.triggered_id):
		
		if len(acao_selecionada) > 0:

			Quantidade_dias_anteriores = 30

			df_param = pd.read_csv("Arquivos/negociacoes_param.csv")	

			df_mes = pd.read_csv("Arquivos/negociacoes_mes.csv")


			if isinstance(acao_selecionada,list):
				
				df_param = df_param.loc[df_param["ticker"] == acao_selecionada[0]]
				df_mes = df_sazon.loc[df_sazon["ticker"] == acao_selecionada[0]]

			else:
				
				df_param = df_param.loc[df_param["ticker"] == acao_selecionada]
				df_mes = df_sazon.loc[df_sazon["ticker"] == acao_selecionada]



			#Previsões por dados divididos pelo parâmetro
			prev_compra_param_LSTM = prever_valor_lstm(df_param["Valor compra"],Quantidade_dias_anteriores,1,180)
			prev_compra_param_MM = prever_valor_media(df_param["Valor compra"],Quantidade_dias_anteriores)

			prev_venda_param_LSTM = prever_valor_lstm(df_param["Valor venda"],Quantidade_dias_anteriores,1,180)
			prev_venda_param_MM = prever_valor_media(df_param["Valor venda"],Quantidade_dias_anteriores)


			#Previsões por dados divididos mensalmente
			prev_compra_mes_LSTM = prever_valor_lstm(df_mes["Valor compra"],Quantidade_dias_anteriores,1,180)
			prev_compra_mes_MM = prever_valor_media(df_mes["Valor compra"],Quantidade_dias_anteriores)

			prev_venda_mes_LSTM = prever_valor_lstm(df_mes["Valor venda"],Quantidade_dias_anteriores,1,180)
			prev_venda_mes_MM = prever_valor_media(df_mes["Valor venda"],Quantidade_dias_anteriores)



	return [[],[],[],[],[],[],[],[]]