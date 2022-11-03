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
import funcoes

import os.path

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
	Output("proxima_compra_param_MM","children"),

	Output("proxima_venda_param_LSTM","children"),
	Output("proxima_venda_param_MM","children"),

	Output("proxima_compra_mes_LSTM","children"),
	Output("proxima_compra_mes_MM","children"),

	Output("proxima_venda_mes_LSTM","children"),
	Output("proxima_venda_mes_MM","children"),

	Input("realizar_previsoes","n_clicks"),
	Input("select_acao_selecionada","value"),

)

def realizar_previsoes(btn_realizarPrevisoes,acao_selecionada):

	


	if len(acao_selecionada) > 0:


		if isinstance(acao_selecionada,list):

			data_atual = datetime.now()

			dia_mes = str(data_atual.day)+str(data_atual.month)

			arquivo = "Arquivos/Previsoes/"+acao_selecionada[0]+dia_mes+"previsoes.csv"	

		else:

			data_atual = datetime.now()

			dia_mes = str(data_atual.day)+str(data_atual.month)

			arquivo = "Arquivos/Previsoes/"+acao_selecionada+dia_mes+"previsoes.csv"

		if os.path.exists(arquivo):

			df_previsoes = pd.read_csv(arquivo)
			#Compra param LSTM,Compra param MM,Venda param LSTM,Venda param MM,Compra mes LSTM,Compra mes MM,Venda mes LSTM,Venda mes MM
			return df_previsoes["Compra param LSTM"][0],df_previsoes["Compra param MM"][0],df_previsoes["Venda param LSTM"][0],df_previsoes["Venda param MM"][0],df_previsoes["Compra mes LSTM"][0],	df_previsoes["Compra mes MM"][0],df_previsoes["Venda mes LSTM"][0],	df_previsoes["Venda mes MM"][0]




	if("realizar_previsoes" == ctx.triggered_id):	

		if len(acao_selecionada) > 0:

			if isinstance(acao_selecionada,list):

				data_atual = datetime.now()

				dia_mes = str(data_atual.day)+str(data_atual.month)

				arquivo = "Arquivos/Previsoes/"+acao_selecionada[0]+dia_mes+"previsoes.csv"	

			else:

				data_atual = datetime.now()

				dia_mes = str(data_atual.day)+str(data_atual.month)

				arquivo = "Arquivos/Previsoes/"+acao_selecionada+dia_mes+"previsoes.csv"



		
			#CONTINUAR A PARTIR DAQUI-----------------------------


			if not os.path.exists(arquivo):

				

				Quantidade_dias_anteriores = 7



				df_param = pd.read_csv("Arquivos/Info/negociacoes_param.csv")	

				df_mes = pd.read_csv("Arquivos/Info/negociacoes_mes.csv")


				if isinstance(acao_selecionada,list):
					
					df_param = df_param.loc[df_param["ticker"] == acao_selecionada[0]]
					df_mes = df_mes.loc[df_mes["ticker"] == acao_selecionada[0]]

					data_atual = datetime.now()

					dia_mes = str(data_atual.day)+str(data_atual.month)

					arquivo = "Arquivos/Previsoes/"+acao_selecionada[0]+dia_mes+"previsoes.csv"	

				else:
					
					df_param = df_param.loc[df_param["ticker"] == acao_selecionada]
					df_mes = df_mes.loc[df_mes["ticker"] == acao_selecionada]
					
					data_atual = datetime.now()

					dia_mes = str(data_atual.day)+str(data_atual.month)

					arquivo = "Arquivos/Previsoes/"+acao_selecionada+dia_mes+"previsoes.csv"	



				#Previsões por dados divididos pelo parâmetro
				prev_compra_param_LSTM = funcoes.prever_valor_lstm(pd.DataFrame(df_param["Valor compra"]),Quantidade_dias_anteriores,1,180)
				prev_compra_param_MM = funcoes.prever_valor_media(df_param["Valor compra"],Quantidade_dias_anteriores)


				prev_venda_param_LSTM = funcoes.prever_valor_lstm(pd.DataFrame(df_param["Valor venda"]),Quantidade_dias_anteriores,1,180)
				prev_venda_param_MM = funcoes.prever_valor_media(df_param["Valor venda"],Quantidade_dias_anteriores)


				#Previsões por dados divididos mensalmente
				prev_compra_mes_LSTM = funcoes.prever_valor_lstm(pd.DataFrame(df_mes["Valor compra"]),Quantidade_dias_anteriores,1,180)
				prev_compra_mes_MM = funcoes.prever_valor_media(df_mes["Valor compra"],Quantidade_dias_anteriores)
				

				prev_venda_mes_LSTM = funcoes.prever_valor_lstm(pd.DataFrame(df_mes["Valor venda"]),Quantidade_dias_anteriores,1,180)
				prev_venda_mes_MM = funcoes.prever_valor_media(df_mes["Valor venda"],Quantidade_dias_anteriores)

				dicionario_previsões={
				"Compra param LSTM":prev_compra_param_LSTM,
				"Compra param MM":prev_compra_param_MM,
				"Venda param LSTM":prev_venda_param_LSTM,
				"Venda param MM":prev_venda_param_MM,

				"Compra mes LSTM":prev_compra_mes_LSTM,
				"Compra mes MM":prev_compra_mes_MM,
				"Venda mes LSTM":prev_venda_mes_LSTM,
				"Venda mes MM":prev_venda_mes_MM
				}

				df_previsoes = pd.DataFrame(dicionario_previsões)


				df_previsoes.to_csv(arquivo)

				return prev_compra_param_LSTM, prev_compra_param_MM, prev_venda_param_LSTM, prev_venda_param_MM, prev_compra_mes_LSTM, prev_compra_mes_MM,prev_venda_mes_LSTM,prev_venda_mes_MM

			else:
				df_previsoes = pd.read_csv(arquivo)
				#Compra param LSTM,Compra param MM,Venda param LSTM,Venda param MM,Compra mes LSTM,Compra mes MM,Venda mes LSTM,Venda mes MM
				return df_previsoes["Compra param LSTM"],df_previsoes["Compra param MM"][0],df_previsoes["Venda param LSTM"][0],df_previsoes["Venda param MM"][0],df_previsoes["Compra mes LSTM"][0],df_previsoes["Compra mes MM"][0],df_previsoes["Venda mes LSTM"][0],df_previsoes["Venda mes MM"][0]

	return [[],[],[],[],[],[],[],[]]