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
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
from   sklearn.metrics import r2_score
import statsmodels.api as sm



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
				html.H5("Regressão linear"),
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_regressao_info"))
				]),
			]),

		],style={"padding": "25px"}),


		
		dbc.Row([

			dbc.Col([
				html.H5("SAR"),
				html.Hr(),

				dbc.Col([
					dbc.Card(dcc.Graph(id="grafico_sar_info"))
				]),
			]),

		],style={"padding": "25px"}),

])


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
		

		

		if isinstance(acao_selecionada,list):
			acao = acao_selecionada[0]

		else:
			acao = acao_selecionada



		#Atributos--------------------------------
		data_final = datetime.now()

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-24)

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

		fig.update_layout(xaxis_rangeslider_visible=True)

		return fig
			
	return {}

@app.callback(
	Output('grafico_macd_info','figure'),
	Input("select_acao_selecionada","value"),
	
)

def popula_macd(acao_selecionada):

	if len(acao_selecionada) > 0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada


		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")



		#ATRIBUTOS---------------------------
		data_final = datetime.now()

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-24)

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

		fig.add_trace(go.Scatter(x = df.index,y = MACD,name = "MACD", line_color = "green"))

		fig.add_trace(go.Scatter(x = df.index,y = sinal,name = "Sinal", line_color = "yellow"))

		

		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

		df["Close"].to_csv("Arquivos/Macd/"+arquivo+"close.csv")
		pd.DataFrame(MACD).to_csv("Arquivos/Macd/"+arquivo+"macd.csv")
		pd.DataFrame(sinal).to_csv("Arquivos/Macd/"+arquivo+"sinal.csv")

		fig.update_layout(xaxis_rangeslider_visible=True)
		

		return fig

	return {}







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

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-24)

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

		fig.update_layout(xaxis_rangeslider_visible=True)

		return fig

	return {}


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

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-24)

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

		fig.update_layout(height=700)


		return fig


	return {}





'''
@app.callback(
	Output('grafico_candlestick_bollinger_info','figure'),
	[Input("select_acao_selecionada","value")]
)

def popula_can_bollinger(acao_selecionada):


	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada


		#Atributos--------------------------------
		data_final = datetime.now()

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-24)

		dias_anteriores = 10

		mm_superior = 1.5

		mm_inferior = 1.5

		#-----------------------------------------

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]



		df_bollinger = pd.DataFrame()

		df_bollinger["Close"] = df["Close"]
		df_bollinger["Date"] = df["Date"]

		

		df.set_index("Date",inplace=True)
		df = pd.DataFrame(df[str(data_inicial):str(data_final)])

		df_bollinger.set_index("Date",inplace=True)
		df_bollinger = pd.DataFrame(df_bollinger[str(data_inicial):str(data_final)])
		
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


		bandas_bollinger = pd.DataFrame()
		bandas_bollinger["Close"] = df_bollinger["Close"]
		bandas_bollinger["Superior"] = sup_band["Superior"]
		bandas_bollinger["Inferior"] = inf_band["Inferior"]

		bandas_bollinger.dropna(inplace=True)

		compras = bandas_bollinger[bandas_bollinger["Close"]<=bandas_bollinger["Inferior"]]
		vendas = bandas_bollinger[bandas_bollinger["Close"]>=bandas_bollinger["Superior"]]

		compras = compras.rename(columns={"Close":"Compras"})
		vendas = vendas.rename(columns={"Close":"Vendas"})
		



		fig = go.Figure()
		fig.add_trace(go.Candlestick(
		    name='Fechamento', 
		    x=df.index, 
		    open=df["Open"], 
		    high=df["High"],
		    low=df["Low"],
		    close=df["Close"]))

		
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
		
		fig.update_layout(height=700)


		return fig


	return {}

'''


@app.callback(
	Output('grafico_regressao_info','figure'),
	Input("select_acao_selecionada","value"),
)


def popula_regressao(acao_selecionada):

	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada

		

		#Atributos--------------------------------
		data_final = datetime.now()

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-4)

		#-----------------------------------------

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)


		df = pd.DataFrame(df[str(data_inicial):str(data_final)])


		df.reset_index(inplace=True)

		X = df.index.values.reshape(-1,1)
		y = df['Close'].values.reshape(-1,1)


		reg = LinearRegression()
		reg.fit(X, y)


		f_previsoes = reg.predict(X)



		previsoes_lista = list()
		i = 0

		while i < len(f_previsoes):
		    
		    previsoes_lista.append(f_previsoes[i][0])
		    
		    i+=1


		fig = go.Figure()

		fig.add_trace(
		    go.Scatter(
		        name="Fechamento",
		        x=df["Date"],
		        y=df["Close"],
		        line=dict(color='blue', width=1))
		)

		fig.add_trace(
		    go.Scatter(
		        name="Regressão",
		        x=df["Date"],
		        y=previsoes_lista,
		        line=dict(color='red', width=1))
		)

		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return fig


	return {}


@app.callback(
	Output('grafico_sar_info','figure'),
	[Input("select_acao_selecionada","value")]
)


def popula_sar(acao_selecionada):
	
	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada

		

		#Atributos--------------------------------
		data_final = datetime.now()

		data_inicial = data_final + dateutil.relativedelta.relativedelta(months=-4)

		iaf = 0.2

		maxaf = 0.2

		#-----------------------------------------

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)

		df["Date"] = df.index

		df = pd.DataFrame(df[str(data_inicial):str(data_final)])

		SAR = funcoes.psar(df,iaf,maxaf)

		SAR_df = pd.DataFrame(SAR)

		fig = go.Figure()

		fig.add_trace(
		    go.Scatter(
		        name="Fechamento",
		        x=SAR_df["dates"],
		        y=SAR_df["close"],
		        line=dict(color='blue', width=2))
		)

		fig.add_trace(
		    go.Scatter(
		        name="SAR bear",
		        x=SAR_df["dates"],
		        y=SAR_df["psarbear"],
		        line=dict(color='red', width=1))
		)

		fig.add_trace(
		    go.Scatter(
		        name="SAR bull",
		        x=SAR_df["dates"],
		        y=SAR_df["psarbull"],
		        line=dict(color='blue', width=1))
		)

		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return fig

	return {}