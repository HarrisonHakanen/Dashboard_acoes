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
			html.H1("Bollinger", className="text-primary"),
		]),
	],style={"padding": "25px"}),


	dbc.Row([
		dbc.Col([
			
			html.H5("Período de análise"),

			dcc.DatePickerRange(
				id="periodo_analise",
				start_date_placeholder_text="Data inicial",
				end_date_placeholder_text="Data final",   
				calendar_orientation='vertical')
		]),

		dbc.Col([
			html.H5("Dias anteriores"),
			dcc.Input(id="dias_anteriores", type="number",className="form-control form-control-lg"),
		]),

		dbc.Col([
			html.H5("Quantidade de desvio padrão superior"),
			dcc.Input(id="mm_superior", type="number",className="form-control form-control-lg"),
		]),
		dbc.Col([
			html.H5("Quantidade de desvio padrão inferior"),
			dcc.Input(id="mm_inferior", type="number",className="form-control form-control-lg"),
		]),
	],style={"padding": "25px"}),


	dbc.Row([
		dbc.Col([
			dbc.Button("Carregar bollinger", color="error", id="carregar_bollinger", className="btn btn-success"),
		],width=4),

	],style={"padding": "25px"}),


	dbc.Row([

		dbc.Col([
			
			html.Hr(),

			dbc.Col([
				dbc.Card(dcc.Graph(id="grafico_boolinger"))
			]),
		]),

	],style={"padding": "25px"}),

])

@app.callback(
	Output('grafico_boolinger','figure'),
	[Input("periodo_analise","start_date"),
	Input("periodo_analise","end_date"),
	Input("dias_anteriores","children"),
	Input("mm_inferior","value"),
	Input("mm_superior","value"),
	Input("select_acao_selecionada","value"),
	Input("carregar_bollinger","n_clicks"),]


)

def popula_boolinger(data_inicial,data_final,dias_anteriores,mm_inferior,mm_superior,acao_selecionada,btn_carregar_bollinger):

	'''
	if isinstance(acao_selecionada,list):
		df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

	else:
		df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]

	'''

	if("carregar_bollinger"==ctx.triggered_id):
		
		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
				acao = acao_selecionada[0]

			else:
				acao = acao_selecionada



			if dias_anteriores == '' or dias_anteriores == None:
				dias_anteriores = 10

			if mm_superior == '' or mm_superior == None:
				mm_superior = 1.5

			if mm_inferior == '' or mm_inferior == None:
				mm_inferior = 1.5



			if(data_inicial != '' or data_inicial != None) or (data_final != '' or data_final != None):

				

				fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


				if isinstance(acao_selecionada,list):
					df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

					
				else:
					df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]

				
				df.set_index("Date",inplace=True)


				df = pd.DataFrame(df[data_inicial:data_final]['Close'])


				

				#Médias móveis de 20 em 20 dias
				mm = df.rolling(10).mean()

				#Desvio padrão de 20 em 20 dias
				std = df.rolling(10).std()

				sup_band = mm + mm_superior * std
				inf_band = mm - mm_inferior * std

				sup_band = sup_band.rename(columns={"Close":"Superior"})
				inf_band = inf_band.rename(columns={"Close":"Inferior"})
				mm = mm.rename(columns={"Close":"Medias"})
				std = std.rename(columns={"Close":"Desvio padrao"})



				bandas_bollinger = df.join(sup_band).join(inf_band)

				bandas_bollinger.dropna(inplace=True)

				compras = bandas_bollinger[bandas_bollinger["Close"]<=bandas_bollinger["Inferior"]]
				vendas = bandas_bollinger[bandas_bollinger["Close"]>=bandas_bollinger["Superior"]]

				compras = compras.rename(columns={"Close":"Compras"})
				vendas = vendas.rename(columns={"Close":"Vendas"})


				sup_band["ticker"] = acao
				inf_band["ticker"] = acao
				mm["ticker"] = acao
				std["ticker"] = acao
				compras["ticker"] = acao
				vendas["ticker"] = acao
				bandas_bollinger["ticker"] = acao
				df["ticker"] = acao

				arquivo = str(datetime.now().month) + str(datetime.now().day) + acao



				sup_band.to_csv("Arquivos/Bollinger/"+arquivo+"sup_band.csv")
				inf_band.to_csv("Arquivos/Bollinger/"+arquivo+"inf_band.csv")
				mm.to_csv("Arquivos/Bollinger/"+arquivo+"mm.csv")
				std.to_csv("Arquivos/Bollinger/"+arquivo+"std.csv")
				compras.to_csv("Arquivos/Bollinger/"+arquivo+"compras.csv")
				vendas.to_csv("Arquivos/Bollinger/"+arquivo+"vendas.csv")
				bandas_bollinger.to_csv("Arquivos/Bollinger/"+arquivo+"bandas_bollinger.csv")
				df.to_csv("Arquivos/Bollinger/"+arquivo+"fechamentos.csv")



				fig = go.Figure()

				fig.add_trace(go.Scatter(
				    x = inf_band.index,
				    y = inf_band['Inferior'],
				    name = "Banda inferior",
				    line_color = "rgba(173,204,255,0.2)"
				))

				fig.add_trace(go.Scatter(
				    x = sup_band.index,
				    y = sup_band["Superior"],
				    name = "Banda superior",
				    fill="tonexty",
				    line_color = "rgba(173,204,255,0.2)"
				))

				fig.add_trace(go.Scatter(
				    x = df.index,
				    y = df["Close"],
				    name = "Preço de fechamento",
				    line_color = "#636EFA"
				))

				fig.add_trace(go.Scatter(
				    x = mm.index,
				    y = mm["Medias"],
				    name = "Média móvel",
				    line_color = "#FECB52"
				))

				fig.add_trace(go.Scatter(
				    x = compras.index,
				    y = compras["Compras"],
				    name = "Compra",
				    mode = "markers",
				    marker = dict(color="#00CC96",size=8)
				))

				fig.add_trace(go.Scatter(
				    x = vendas.index,
				    y = vendas["Vendas"],
				    name = "Venda",
				    mode = "markers",
				    marker = dict(color="#EF553B",size = 8)
				))

			return fig





	
	if len(acao_selecionada) > 0:


		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada


		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

		

		if(os.path.exists("Arquivos/Bollinger/"+arquivo+"inf_band.csv")):
				

			Banda_inferior_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"inf_band.csv")
			Banda_superior_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"sup_band.csv")

			Compras_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"compras.csv")
			Vendas_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"vendas.csv")

			Medias_moveis_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"mm.csv")
			Desvio_padrao_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"std.csv")

			Bandas_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"bandas_bollinger.csv")

			Fechamento_original = pd.read_csv("Arquivos/Bollinger/"+arquivo+"fechamentos.csv")

			

			#Split no tiker correto________________________________________________
			
			Banda_inferior = Banda_inferior_original.loc[Banda_inferior_original["ticker"] == ticker]
			Banda_superior = Banda_superior_original.loc[Banda_superior_original["ticker"] == ticker]

			Compras_ = Compras_original.loc[Compras_original["ticker"] == ticker]
			Vendas_ = Vendas_original.loc[Vendas_original["ticker"] == ticker]

			Medias_moveis = Medias_moveis_original.loc[Medias_moveis_original["ticker"] == ticker]
			Desvio_padrao = Desvio_padrao_original.loc[Desvio_padrao_original["ticker"] == ticker]

			Bandas = Bandas_original.loc[Bandas_original["ticker"] == ticker]

			Fechamento = Fechamento_original.loc[Fechamento_original["ticker"] == ticker]


			fig = go.Figure()

			fig.add_trace(go.Scatter(
			    x = Banda_inferior["Date"],
			    y = Banda_inferior['Inferior'],
			    name = "Banda inferior",
			    line_color = "rgba(173,204,255,0.2)"
			))

			fig.add_trace(go.Scatter(
			    x = Banda_superior["Date"],
			    y = Banda_superior["Superior"],
			    name = "Banda superior",
			    fill="tonexty",
			    line_color = "rgba(173,204,255,0.2)"
			))

			fig.add_trace(go.Scatter(
			    x = Fechamento["Date"],
			    y = Fechamento["Close"],
			    name = "Preço de fechamento",
			    line_color = "#636EFA"
			))

			fig.add_trace(go.Scatter(
			    x = Medias_moveis["Date"],
			    y = Medias_moveis["Medias"],
			    name = "Média móvel",
			    line_color = "#FECB52"
			))

			fig.add_trace(go.Scatter(
			    x = Compras_["Date"],
			    y = Compras_["Compras"],
			    name = "Compra",
			    mode = "markers",
			    marker = dict(color="#00CC96",size=8)
			))

			fig.add_trace(go.Scatter(
			    x = Vendas_["Date"],
			    y = Vendas_["Vendas"],
			    name = "Venda",
			    mode = "markers",
			    marker = dict(color="#EF553B",size = 8)
			))

			return fig


	return {}