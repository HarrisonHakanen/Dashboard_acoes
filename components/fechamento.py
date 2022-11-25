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

import os.path




layout = dbc.Col([

	dbc.Row([

		dbc.Col([

			html.H1("Fechamentos", className="text-primary"),
			
			html.H5("Dias anteriores (padrão 30)"),
			dcc.Input(id="dias_anteriores_fechamento",value=30, type="number",className="form-control form-control-lg"),
		
		],width=3)

	],style={"padding": "25px"}),


	dbc.Row([
			dbc.Col([
				html.Legend("Grafico de fechamentos", className="text-primary"),
				dbc.Card(dcc.Graph(id="grafico_fechamentos"))
			]),
	],style={"padding": "25px"}),

	dbc.Row([

			dbc.Col([
				html.Legend("Tabela de fechamentos", className="text-primary"),
	        	html.Div(id="tabela_fechamentos", className="dbc"),

			]),
	],style={"padding": "25px"}),



	dbc.Row([

		dbc.Row([

			html.Legend("Informativos", className="text-primary"),
		]),
		dbc.Row([
			dbc.Col([

				html.Legend("Inf. fechamento"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="fechamento_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="fechamento_desvio"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="fechamento_minima"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="fechamento_maxima")
						]),
					]),

				]),

			],width=3),


			dbc.Col([
				html.Legend("Inf. alta"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="alta_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="alta_desvio"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="alta_minima"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="alta_maxima")
						]),
					]),

				]),

			],width=3),


			dbc.Col([
				html.Legend("Inf. baixa"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="baixa_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="baixa_desvio"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="baixa_minima"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="baixa_maxima")
						]),
					]),

				]),

			],width=3),


			dbc.Col([
				html.Legend("Inf. alta - baixa"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="alta-baixa_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="alta-baixa_desvio"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="alta-baixa_minima"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="alta-baixa_maxima")
						]),
					]),

				]),

			],width=3),
		]),

	],style={"padding": "25px"}),

	dbc.Row([
		dbc.Row([
			dbc.Col([
				html.Legend("Previsões", className="text-primary"),
				'''São realizadas as previsões do próximo dia'''
			]),
		]),
		dbc.Row([
			dbc.Col([
				dbc.Card([
					html.H5("Previsão por LSTM", className="text-primary"),			
					html.Hr(),
					html.Table([
						html.Tr([
							html.Td([
								html.H5("Próxima alta")
							]),

							html.Td([
								html.H5(id="proxima_alta_LSTM")
							]),
						]),
						html.Tr([
							html.Td([
								html.H5("Próxima baixa")
							]),

							html.Td([
								html.H5(id="proxima_baixa_LSTM")
							]),
						]),

					]),
				]),
			]),
			dbc.Col([
				dbc.Card([
					html.H5("Previsão por média", className="text-primary"),			
					html.Hr(),
					html.Table([
						html.Tr([
							html.Td([
								html.H5("Próxima alta")
							]),

							html.Td([
								html.H5(id="proxima_alta_media")
							]),
						]),
						html.Tr([
							html.Td([
								html.H5("Próxima baixa")
							]),

							html.Td([
								html.H5(id="proxima_baixa_media")
							]),
						]),

					]),
				]),
			]),
		]),
		dbc.Row([
			dbc.Col([
				dbc.Button("Realizar previsões", color="error", id="previsoes_dia_seguinte", value="acoes", className="btn btn-success"),
			]),

		]),

	],style={"padding": "25px"})

])

@app.callback(
	Output("alta_media","children"),
	Output("alta_desvio","children"),
	Output("alta_minima","children"),
	Output("alta_maxima","children"),
	Input("dias_anteriores_fechamento","value"),
	Input("select_acao_selecionada","value")
)
def retorna_alta(dias_anteriores,acao_selecionada):
	
	if len(acao_selecionada)>0:


		if dias_anteriores != '' or dias_anteriores != None:
			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


			if isinstance(acao_selecionada,list):
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]
		
			else:
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


			
			df = df.tail(dias_anteriores)
			df.set_index("Date",inplace=True)

			df["Data"] = df.index

			return round(df["High"].mean(),2),round(df["High"].std(),2),round(df["High"].min(),2),round(df["High"].max(),2)

	return [],[],[],[]


@app.callback(
	Output("baixa_media","children"),
	Output("baixa_desvio","children"),
	Output("baixa_minima","children"),
	Output("baixa_maxima","children"),
	Input("dias_anteriores_fechamento","value"),
	Input("select_acao_selecionada","value")
)


def retorna_baixa(dias_anteriores,acao_selecionada):
	if len(acao_selecionada)>0:


		if dias_anteriores != '' or dias_anteriores != None:
			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


			if isinstance(acao_selecionada,list):
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]
		
			else:
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


			
			df = df.tail(dias_anteriores)
			df.set_index("Date",inplace=True)

			df["Data"] = df.index

			return round(df["Low"].mean(),2),round(df["Low"].std(),2),round(df["Low"].min(),2),round(df["Low"].max(),2)


	return [],[],[],[]	

@app.callback(
	Output("alta-baixa_media","children"),
	Output("alta-baixa_desvio","children"),
	Output("alta-baixa_minima","children"),
	Output("alta-baixa_maxima","children"),
	Input("dias_anteriores_fechamento","value"),
	Input("select_acao_selecionada","value")
)
def retorna_atla_baixa(dias_anteriores,acao_selecionada):

	if len(acao_selecionada)>0:


		if dias_anteriores != '' or dias_anteriores != None:
			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


			if isinstance(acao_selecionada,list):
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]
		
			else:
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


			
			df = df.tail(dias_anteriores)
			df.set_index("Date",inplace=True)

			df["Data"] = df.index

			return round(df["High-Low"].mean(),2),round(df["High-Low"].std(),2),round(df["High-Low"].min(),2),round(df["High-Low"].max(),2)


	return [],[],[],[]	

@app.callback(
	Output('grafico_fechamentos','figure'),
	Output('tabela_fechamentos','children'),
	Output('fechamento_media','children'),
	Output('fechamento_desvio','children'),
	Output('fechamento_minima','children'),
	Output('fechamento_maxima','children'),
	Input("dias_anteriores_fechamento","value"),
	Input("select_acao_selecionada","value")
)


def popula_grafico(dias_anteriores,acao_selecionada):
	
	if len(acao_selecionada)>0:


		if dias_anteriores != '' or dias_anteriores != None:
			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


			if isinstance(acao_selecionada,list):
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]
		
			else:
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


			
			df = df.tail(dias_anteriores)
			df.set_index("Date",inplace=True)

			df["Data"] = df.index

			df["Close"] = round(df["Close"],2)
			df["High"] = round(df["High"],2)
			df["Low"] = round(df["Low"],2)
			df["Diferenca"] = round(df["Diferenca"],2)
			df["Diferenca_percentual"] = round(df["Diferenca_percentual"],2)
			df["Fechamento_minima"] = round(df["Fechamento_minima"],2)
			df["High-Low"] = round(df["High-Low"],2)

			df = df[["Data","Close","Diferenca","Diferenca_percentual","High","Low","High-Low","Fechamento_minima"]]

			df = df.sort_index(ascending=False)

			fig = go.Figure()

			fig.add_trace(go.Scatter(name='Fechamento', x=df.index, y=df['Close'], mode='lines'))


			fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

			tabela = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=15,)

			return fig,tabela,round(df["Close"].mean(),2),round(df["Close"].std(),2),round(df["Close"].min(),2),round(df["Close"].max(),2)

	return {},[],[],[],[],[]


@app.callback(
	Output("proxima_alta_LSTM","children"),
	Output("proxima_baixa_LSTM","children"),
	Output("proxima_alta_media","children"),
	Output("proxima_baixa_media","children"),
	Input("previsoes_dia_seguinte","n_clicks"),
	Input("select_acao_selecionada","value"),
)

def realizar_proximas_previsoes(n1,acao_selecionada):

	if len(acao_selecionada) > 0:

		'''
		if isinstance(acao_selecionada,list):

			data_atual = datetime.now()

			dia_mes = str(data_atual.day)+str(data_atual.month)

			arquivo = "Arquivos/Previsoes/"+acao_selecionada[0]+dia_mes+"previsoesSeguintes.csv"	

		else:

			data_atual = datetime.now()

			dia_mes = str(data_atual.day)+str(data_atual.month)

			arquivo = "Arquivos/Previsoes/"+acao_selecionada+dia_mes+"previsoesSeguintes.csv"

		if os.path.exists(arquivo):

			df_previsoes = pd.read_csv(arquivo)
			
			return df_previsoes[0],df_previsoes[1],df_previsoes[2],df_previsoes[3]

		'''

	if("previsoes_dia_seguinte" == ctx.triggered_id):	

		if len(acao_selecionada) > 0:

			if isinstance(acao_selecionada,list):

				data_atual = datetime.now()

				dia_mes = str(data_atual.day)+str(data_atual.month)

				#arquivo = "Arquivos/Previsoes/"+acao_selecionada[0]+dia_mes+"previsoesSeguintes.csv"	

			else:

				data_atual = datetime.now()

				dia_mes = str(data_atual.day)+str(data_atual.month)

				#arquivo = "Arquivos/Previsoes/"+acao_selecionada+dia_mes+"previsoesSeguintes.csv"

			#if not os.path.exists(arquivo):


			Quantidade_dias_anteriores = 15


			df_fechamento = pd.read_csv("Arquivos/Info/fechamento.csv")	


			if isinstance(acao_selecionada,list):
				
				df_fechamento = df_fechamento.loc[df_fechamento["ticker"] == acao_selecionada[0]]

				data_atual = datetime.now()

				dia_mes = str(data_atual.day)+str(data_atual.month)

				arquivo = "Arquivos/Previsoes/"+acao_selecionada[0]+dia_mes+"previsoesSeguintes.csv"	

			else:
				
				df_fechamento = df_fechamento.loc[df_fechamento["ticker"] == acao_selecionada]
				
				data_atual = datetime.now()

				dia_mes = str(data_atual.day)+str(data_atual.month)

				arquivo = "Arquivos/Previsoes/"+acao_selecionada+dia_mes+"previsoesSeguintes.csv"	


			prev_alta_LSTM = funcoes.prever_valor_lstm(pd.DataFrame(df_fechamento["High"]),Quantidade_dias_anteriores,1,180)
			prev_baixa_LSTM = funcoes.prever_valor_lstm(pd.DataFrame(df_fechamento["Low"]),Quantidade_dias_anteriores,1,180)

			prev_alta_MM = funcoes.prever_valor_media(df_fechamento["High"],Quantidade_dias_anteriores)
			prev_baixa_MM = funcoes.prever_valor_media(df_fechamento["Low"],Quantidade_dias_anteriores)


			dicionario_previsões={
			"Alta LSTM":prev_alta_LSTM,
			"Baixa LSTM":prev_baixa_LSTM,
			"Alta MM":prev_alta_MM,
			"Baixa MM":prev_baixa_MM,
			}

			df_previsoes = pd.DataFrame(dicionario_previsões)


			df_previsoes.to_csv(arquivo)


			return prev_alta_LSTM,prev_baixa_LSTM,prev_alta_MM,prev_baixa_MM

	return [[],[],[],[]]
