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

				html.Legend("Informações baixa"),
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

			],width = 6),



			#valor de venda
			dbc.Col([
				html.Legend("Informações alta"),
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


			],width = 6),
			
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

				html.Legend("Informações baixa"),
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

			],width = 6),



			#valor de venda
			dbc.Col([
				html.Legend("Informações alta"),
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


			],width = 6),


		],style={"padding": "25px"}),
			
	]),


])


@app.callback(

	Output("vlr_venda_altas_baixas_param_media","children"),
	Output("vlr_venda_altas_baixas_param_std","children"),
	Output("vlr_venda_altas_baixas_param_min","children"),
	Output("vlr_venda_altas_baixas_param_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_vendas_mes(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_param.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)




		return [round(df["Fechamento alta"].mean(),2),round(df["Fechamento alta"].std(),2),round(df["Fechamento alta"].min(),2),round(df["Fechamento alta"].max(),2)]

	return[[],[],[],[]]

@app.callback(

	Output("vlr_compra_altas_baixas_param_media","children"),
	Output("vlr_compra_altas_baixas_param_std","children"),
	Output("vlr_compra_altas_baixas_param_min","children"),
	Output("vlr_compra_altas_baixas_param_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_compra_mes(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_param.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		return [round(df["Fechamento baixa"].mean(),2),round(df["Fechamento baixa"].std(),2),round(df["Fechamento baixa"].min(),2),round(df["Fechamento baixa"].max(),2)]

	return[[],[],[],[]]



@app.callback(
    Output('tabela_altas_baixas_param', 'children'),
    [Input("select_acao_selecionada","value")]
)
def imprimir_tabela (acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_param.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)

		
		df = df.sort_index(ascending=False)

		
		df['Fechamento baixa'] = round(df['Fechamento baixa'],2)
		df['Fechamento alta'] = round(df['Fechamento alta'],2)
		
		tabela = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=7,)


		return tabela

	return []


@app.callback(
    Output('tabela_altas_baixas_mes', 'children'),
    [Input("select_acao_selecionada","value")]
)
def imprimir_tabela (acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_mes.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		df = df.sort_index(ascending=False)

		df['Fechamento baixa'] = round(df['Fechamento baixa'],2)
		df['Fechamento alta'] = round(df['Fechamento alta'],2)
		

		tabela = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=7,)


		return tabela

	return []

@app.callback(
	Output('grafico_altas_baixas_param','figure'),
	[Input("select_acao_selecionada","value")]
)

def popula_grafico_altas_baixas_param(acao_selecionada):


	if len(acao_selecionada)>0:

		df_compra = pd.DataFrame()
		df_venda = pd.DataFrame()

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_mes.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		df['Fechamento baixa'] = round(df['Fechamento baixa'])
		df['Fechamento alta'] = round(df['Fechamento alta'])

		df_compra["Data"] = df['Data baixa']
		df_compra["Valor"] = df['Fechamento baixa']
		df_compra["Output"] = 'Baixa'

		df_venda['Data'] = df['Data alta']
		df_venda['Valor'] = df['Fechamento alta']
		df_venda['Output'] = 'Alta'

		dfs = [df_venda, df_compra]

		df_final = pd.concat([df_compra,df_venda])

		fig = go.Figure()
		fig.add_trace(go.Scatter(name='Altas', x=df['Data alta'], y=df['Fechamento alta'], mode='lines'))
		fig.add_trace(go.Scatter(name='Baixas', x=df['Data baixa'], y=df['Fechamento baixa'], mode='lines'))
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return fig

	fig = go.Figure()
	return fig




#SAZONALIDADE POR MES------------------------------------------------------



#INFO DAS NEGOCIAÇÕES POR MÊS
@app.callback(

	Output("vlr_venda_altas_baixas_mes_media","children"),
	Output("vlr_venda_altas_baixas_mes_std","children"),
	Output("vlr_venda_altas_baixas_mes_min","children"),
	Output("vlr_venda_altas_baixas_mes_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_vendas_mes(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_mes.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)




		return [round(df["Fechamento alta"].mean(),2),round(df["Fechamento alta"].std(),2),round(df["Fechamento alta"].min(),2),round(df["Fechamento alta"].max(),2)]

	return[[],[],[],[]]


@app.callback(

	Output("vlr_compra_altas_baixas_mes_media","children"),
	Output("vlr_compra_altas_baixas_mes_std","children"),
	Output("vlr_compra_altas_baixas_mes_min","children"),
	Output("vlr_compra_altas_baixas_mes_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_compra_mes(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_mes.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		return [round(df["Fechamento baixa"].mean(),2),round(df["Fechamento baixa"].std(),2),round(df["Fechamento baixa"].min(),2),round(df["Fechamento baixa"].max(),2)]

	return[[],[],[],[]]

@app.callback(

	Output('grafico_altas_baixas_mes','figure'),
	[Input("select_acao_selecionada","value")]

)


def popula_grafico_altas_baixas_mes(acao_selecionada):

	if len(acao_selecionada)>0:

		df_compra = pd.DataFrame()
		df_venda = pd.DataFrame()


		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/sazonalidade_mes.csv")	


		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		
		df['Fechamento baixa'] = round(df['Fechamento baixa'])
		df['Fechamento alta'] = round(df['Fechamento alta'])

		df_compra["Data"] = df['Data baixa']
		df_compra["Valor"] = df['Fechamento baixa']
		df_compra["Output"] = 'Baixa'

		df_venda['Data'] = df['Data alta']
		df_venda['Valor'] = df['Fechamento alta']
		df_venda['Output'] = 'Alta'

		dfs = [df_venda, df_compra]

		df_final = pd.concat([df_compra,df_venda])

		fig = go.Figure()
		fig.add_trace(go.Scatter(name='Altas', x=df['Data alta'], y=df['Fechamento alta'], mode='lines'))
		fig.add_trace(go.Scatter(name='Baixas', x=df['Data baixa'], y=df['Fechamento baixa'], mode='lines'))
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return fig

	fig = go.Figure()
	return fig