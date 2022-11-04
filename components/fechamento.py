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

		dbc.Col([
			html.Legend("Informações taxa de retorno"),
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

	],style={"padding": "25px"}),

])


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

			df = df[["Data","Close","ticker"]]


			fig = go.Figure()

			fig.add_trace(go.Scatter(name='Fechamento', x=df.index, y=df['Close'], mode='lines'))




			tabela = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=7,)

			return fig,tabela,df["Close"].mean(),df["Close"].std(),df["Close"].min(),df["Close"].max()

	return {},[],[],[],[],[]