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
import dateutil.relativedelta
from datetime import datetime


import pdb
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO
import funcoes




layout = dbc.Col([

		dbc.Row([
			dbc.Col([
				html.H1("Gráficos", className="text-primary"),
			]),
		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Col([
				html.H5("MACD"),
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_macd_info"))
				]),
			]),

		],style={"padding": "25px"}),
		dbc.Row([

			dbc.Col([
				html.H5("Bollinger"),
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_boolinger_info"))
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Col([
				html.H5("RSI"),
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_rsi_info"))
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Col([
				html.H5("Candlestick"),
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_candlestick_info"))
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Col([
				html.H5("Fechamentos"),
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_fechamento_info"))
				]),
			]),

		],style={"padding": "25px"}),

])


@app.callback(
	Output('grafico_candlestick_info','figure'),
	[Input("select_acao_selecionada","value")]


)

def popula_candlestick(acao_selecionada):


	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada


		#Atributos--------------------------------
		data_final = datetime.now()

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-6)

		#-----------------------------------------

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)


		df = pd.DataFrame(df[str(data_inicial):str(data_final)])

		fig = go.Figure()
		fig.add_trace(go.Candlestick(
		    name='Fechamento', 
		    x=df.index, 
		    open=df["Open"], 
		    high=df["High"],
		    low=df["Low"],
		    close=df["Close"]))

		return fig


	return {}

@app.callback(
	Output('grafico_boolinger_info','figure'),
	[Input("select_acao_selecionada","value")]


)


def popula_boolinger(acao_selecionada):

	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada

		

		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker
		if(os.path.exists("Arquivos/Bollinger/"+arquivo+"inf_band.csv")):

			Banda_inferior = pd.read_csv("Arquivos/Bollinger/"+arquivo+"inf_band.csv")
			Banda_superior = pd.read_csv("Arquivos/Bollinger/"+arquivo+"sup_band.csv")

			Compras_ = pd.read_csv("Arquivos/Bollinger/"+arquivo+"compras.csv")
			Vendas_ = pd.read_csv("Arquivos/Bollinger/"+arquivo+"vendas.csv")

			Medias_moveis = pd.read_csv("Arquivos/Bollinger/"+arquivo+"mm.csv")
			Desvio_padrao = pd.read_csv("Arquivos/Bollinger/"+arquivo+"std.csv")

			Bandas = pd.read_csv("Arquivos/Bollinger/"+arquivo+"bandas_bollinger.csv")

			Fechamento = pd.read_csv("Arquivos/Bollinger/"+arquivo+"fechamentos.csv")

			
			print(Compras_)
			

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
			print(fig)
			return fig

		else:

			if isinstance(acao_selecionada,list):
				acao = acao_selecionada[0]

			else:
				acao = acao_selecionada



			#Atributos--------------------------------
			data_final = datetime.now()

			data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-4)

			dias_anteriores = 10

			mm_superior = 1.5

			mm_inferior = 1.5
			#-----------------------------------------


			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


			if isinstance(acao_selecionada,list):
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

				
			else:
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


			df.set_index("Date",inplace=True)


			df = pd.DataFrame(df[str(data_inicial):str(data_final)]['Close'])



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

			print("Std")
			print(len(std))
			print(std)

			arquivo = str(datetime.now().month) + str(datetime.now().day) + acao



			sup_band.to_csv("Arquivos/Bollinger/"+arquivo+"sup_band.csv")
			inf_band.to_csv("Arquivos/Bollinger/"+arquivo+"inf_band.csv")
			mm.to_csv("Arquivos/Bollinger/"+arquivo+"mm.csv")
			std.to_csv("Arquivos/Bollinger/"+arquivo+"std.csv")
			compras.to_csv("Arquivos/Bollinger/"+arquivo+"compras.csv")
			vendas.to_csv("Arquivos/Bollinger/"+arquivo+"vendas.csv")
			bandas_bollinger.to_csv("Arquivos/Bollinger/"+arquivo+"bandas_bollinger.csv")
			df.to_csv("Arquivos/Bollinger/"+arquivo+"fechamentos.csv")
		
			'''
			print("banda inferior\n")
			print(inf_band.head(10))
			print("banda superior\n")
			print(sup_band.head(10))
			print("compras\n")
			print(compras.head(10))
			print("vendas\n")
			print(vendas.head(10))
			print("medias moveis\n")
			print(mm.head(10))
			print("desvio padrão\n")
			print(std.head(10))
			print("bandas\n")
			print(bandas_bollinger.head(10))
			print("fechamento\n")
			print(df.head(10))
			'''

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
			
	return {}

@app.callback(
	Output('grafico_macd_info','figure'),
	Output('grafico_fechamento_info','figure'),
	Input("select_acao_selecionada","value"),
	
)

def popula_macd(acao_selecionada):



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

		else:

			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")



			#ATRIBUTOS---------------------------
			data_final = datetime.now()

			data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-4)

			rapida = 12
			lenta = 26
			sinal = 9
			#------------------------------------



			if isinstance(acao_selecionada,list):
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

				
			else:
				df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


			df.set_index("Date",inplace=True)

			
			df = pd.DataFrame(df[str(data_inicial):str(data_final)]['Close'])
			

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


			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

			df["Close"].to_csv("Arquivos/Macd/"+arquivo+"close.csv")
			pd.DataFrame(MACD).to_csv("Arquivos/Macd/"+arquivo+"macd.csv")
			pd.DataFrame(sinal).to_csv("Arquivos/Macd/"+arquivo+"sinal.csv")


			return fig,fig2

	return [{},{}]



@app.callback(
	Output('grafico_rsi_info','figure'),
	Input("select_acao_selecionada","value"),
	
)

def popula_rsi(acao_selecionada):


	if len(acao_selecionada) > 0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada


		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")



		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		

		#ATRIBUTOS---------------------------
		data_final = datetime.now()

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-4)

		superior = 0.7
		inferior = 0.3
		dias_anteriores = 14


		#------------------------------------


		df.set_index("Date",inplace=True)
		
		df = pd.DataFrame(df[str(data_inicial):str(data_final)]['Close'])


		df = df[df.index > str(data_inicial)]

		change = df["Close"].diff()
		change.dropna(inplace=True)


		change_up = change.copy()
		change_down = change.copy()
		 
		change_up[change_up<0] = 0
		change_down[change_down>0] = 0


		change.equals(change_up+change_down)

		# Calculate the rolling average of average up and average down
		avg_up = change_up.rolling(dias_anteriores).mean()
		avg_down = change_down.rolling(dias_anteriores).mean().abs()

		rsi = 100 * avg_up / (avg_up + avg_down)

		rsi =pd.DataFrame(rsi)
		rsi["Date"] = rsi.index
		rsi.to_csv("rsi"+ticker+".csv")

		fig = px.line(rsi, x=rsi["Date"], y=rsi["Close"])
		fig.add_hline(y=rsi["Close"].max()*inferior,line_color="blue")
		fig.add_hline(y=rsi["Close"].max()*superior,line_color="red")

		return fig

	return {}