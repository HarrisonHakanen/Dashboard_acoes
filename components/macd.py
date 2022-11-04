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
import os

import pdb
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO
import funcoes



layout = dbc.Col([

		dbc.Row([
			dbc.Col([
				html.H1("MACD", className="text-primary"),
			]),
		],style={"padding": "25px"}),


		dbc.Row([
			dbc.Col([
				
				html.H5("Período de análise"),

				dcc.DatePickerRange(
					id="periodo_analise_MACD",
					start_date_placeholder_text="Data inicial",
					end_date_placeholder_text="Data final",   
					calendar_orientation='vertical')
			]),

			dbc.Col([
				html.H5("Rápida MM (padrão 12)"),
				dcc.Input(id="rapida_mm", type="number",className="form-control form-control-lg"),
			]),

			dbc.Col([
				html.H5("Lenta MM (padrão 26)"),
				dcc.Input(id="lenta_mm", type="number",className="form-control form-control-lg"),
			]),
			dbc.Col([
				html.H5("Sinal (padrão 9)"),
				dcc.Input(id="sinal", type="number",className="form-control form-control-lg"),
			]),
		],style={"padding": "25px"}),


		dbc.Row([
			dbc.Col([
				dbc.Button("Carregar bollinger", color="error", id="carregar_macd", className="btn btn-success"),
			],width=4),

		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Col([
				
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_macd"))
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Col([
				
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_fechamento"))
				]),
			]),

		],style={"padding": "25px"}),

])


@app.callback(
	Output('grafico_macd','figure'),
	Output('grafico_fechamento','figure'),
	[Input("periodo_analise_MACD","start_date"),
	Input("periodo_analise_MACD","end_date"),
	Input("sinal","children"),
	Input("rapida_mm","children"),
	Input("lenta_mm","children"),
	Input("select_acao_selecionada","value"),
	Input("carregar_macd","n_clicks"),]


)

def popula_macd(data_inicial,data_final,sinal,rapida,lenta,acao_selecionada,btn_macd):

	if("carregar_macd"==ctx.triggered_id):

		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
				acao = acao_selecionada[0]

			else:
				acao = acao_selecionada


			if sinal == '' or sinal == None:
				sinal = 9

			if rapida == '' or rapida == None:
				rapida = 12

			if lenta == '' or lenta == None:
				lenta = 26


			if(data_inicial != '' or data_inicial != None) or (data_final != '' or data_final != None):

				fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


				if isinstance(acao_selecionada,list):
					df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

					
				else:
					df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]



				df.set_index("Date",inplace=True)


				df = pd.DataFrame(df[data_inicial:data_final]['Close'])


				#Calcula a média móvel exponencial rápida e lenta
				rapidaMME=df.Close.ewm(span=rapida).mean()

				lentaMME=df.Close.ewm(span=lenta).mean()

				MACD = rapidaMME - lentaMME

				#Calcula a média móvel exponencial do próprio MACD
				sinal = MACD.ewm(span=sinal).mean()


				fig = go.Figure()

				fig.add_trace(go.Scatter(x = df.index,y = MACD,name = "MACD", line_color = "blue"))

				fig.add_trace(go.Scatter(x = df.index,y = sinal,name = "Sinal", line_color = "yellow"))

				fig2 = go.Figure()

				fig2.add_trace(go.Scatter(x = df.index,y = df["Close"],name = "Fechamento",line_color = "blue"))


				arquivo = str(datetime.now().month) + str(datetime.now().day) + acao

				df["Close"].to_csv("Arquivos/Macd/"+arquivo+"close.csv")
				pd.DataFrame(MACD).to_csv("Arquivos/Macd/"+arquivo+"macd.csv")
				pd.DataFrame(sinal).to_csv("Arquivos/Macd/"+arquivo+"sinal.csv")



				return fig,fig2


	if len(acao_selecionada) > 0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada


		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker



		if(os.path.exists("Arquivos/Macd/"+arquivo+"macd.csv")):

			MACD = pd.read_csv("Arquivos/Macd/"+arquivo+"macd.csv")
			df = pd.read_csv("Arquivos/Macd/"+arquivo+"close.csv")
			sinal = pd.read_csv("Arquivos/Macd/"+arquivo+"sinal.csv")

			
			df.set_index("Date")

			fig = go.Figure()

			fig.add_trace(go.Scatter(x = df.index,y = MACD["Close"],name = "MACD", line_color = "blue"))

			fig.add_trace(go.Scatter(x = df.index,y = sinal["Close"],name = "Sinal", line_color = "yellow"))

			fig2 = go.Figure()

			fig2.add_trace(go.Scatter(x = df["Date"],y = df["Close"],name = "Fechamento",line_color = "blue"))


			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

			return fig,fig2

	return [{},{}]