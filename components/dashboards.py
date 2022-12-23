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
	
	#Card negociacoes por parametro--------------------------
	dbc.Card([

		#grafico de negociações por parametro
		dbc.Row([
			html.H1("Negociações por parâmetro", className="text-primary"),
			html.Hr(),

			dbc.Col([
				html.Legend("Grafico de negociações por parâmetro", className="text-primary"),
				dbc.Card(dcc.Graph(id="grafico_negociacoes_param"))
			]),

		],style={"padding": "25px"}),

		#tabela de negociações por parametro
		dbc.Row([
			dbc.Col([
				html.Legend("Tabela de negociações por parâmetro", className="text-primary"),
	        	html.Div(id="tabela_negociacoes_param", className="dbc"),
			]),
		],style={"padding": "25px"}),
		

		#informações de negociações por parametro
		dbc.Row([

			
			#valor de compra
			dbc.Col([

				html.Legend("Informações compra"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_param_max")
						]),
					]),
					

				]),

			],width = 3),



			#valor de venda
			dbc.Col([
				html.Legend("Informações venda"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_param_max")
						]),
					]),

				]),


			],width = 3),


			#lucro
			dbc.Col([

				html.Legend("Informações lucro"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_param_max")
						]),
					]),

				]),



			],width=3),

			#taxa de retorno
			dbc.Col([
				html.Legend("Informações taxa de retorno"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_param_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_param_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_param_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_param_max")
						]),
					]),

				]),



			],width=3),

		],style={"padding": "25px"}),
			
	]),
	


	#Card negociacoes por mês--------------------------
	dbc.Card([

		dbc.Row([
			html.H1("Negociações por mês", className="text-primary"),
			html.Hr(),

			dbc.Col([
				html.Legend("Grafico de negociações por mês", className="text-primary"),
				dbc.Card(dcc.Graph(id="grafico_negociacoes_mes"))
			]),
		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Col([
				html.Legend("Tabela de negociações por mês", className="text-primary"),
	        	html.Div(id="tabela_negociacoes_mes", className="dbc"),

			]),
		],style={"padding": "25px"}),


		#informações de negociações por mês
		dbc.Row([

			
			#valor de compra
			dbc.Col([

				html.Legend("Informações compra"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_compra_neg_mes_max")
						]),
					]),

				]),

			],width = 3),



			#valor de venda
			dbc.Col([
				html.Legend("Informações venda"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_venda_neg_mes_max")
						]),
					]),

				]),


			],width = 3),


			#lucro
			dbc.Col([

				html.Legend("Informações lucro"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_lucro_neg_mes_max")
						]),
					]),

				]),



			],width=3),

			#taxa de retorno
			dbc.Col([
				html.Legend("Informações taxa de retorno"),
				html.Table([
					html.Tr([
						html.Td([
							html.H5("Média")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_mes_media"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Desvio padrão")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_mes_std"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Mínima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_mes_min"),
						]),
					]),
					html.Tr([
						html.Td([
							html.H5("Máxima")
						]),
						html.Td([
							html.H5(id="vlr_retorno_neg_mes_max")
						]),
					]),

				]),



			],width=3),

		],style={"padding": "25px"}),

	])




],width=12)



#INFO DAS NEGOCIAÇÕES POR PARAMETRO
@app.callback(

	Output("vlr_venda_neg_param_media","children"),
	Output("vlr_venda_neg_param_std","children"),
	Output("vlr_venda_neg_param_min","children"),
	Output("vlr_venda_neg_param_max","children"),
	[Input("select_acao_selecionada","value")
	]

)

def info_vendas_param(acao_selecionada):


	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_param.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		return [round(df["Valor venda"].mean(),2),round(df["Valor venda"].std(),2),round(df["Valor venda"].min(),2),round(df["Valor venda"].max(),2)]

	return[[],[],[],[]]

@app.callback(

	Output("vlr_compra_neg_param_media","children"),
	Output("vlr_compra_neg_param_std","children"),
	Output("vlr_compra_neg_param_min","children"),
	Output("vlr_compra_neg_param_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_compra_param(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_param.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)

		return [round(df["Valor compra"].mean(),2),round(df["Valor compra"].std(),2),round(df["Valor compra"].min(),2),round(df["Valor compra"].max(),2)]

	return[[],[],[],[]]

@app.callback(

	Output("vlr_lucro_neg_param_media","children"),
	Output("vlr_lucro_neg_param_std","children"),
	Output("vlr_lucro_neg_param_min","children"),
	Output("vlr_lucro_neg_param_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_lucro_param(acao_selecionada):


	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_param.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)

		return [round(df["Lucro"].mean(),2),round(df["Lucro"].std(),2),round(df["Lucro"].min(),2),round(df["Lucro"].max(),2)]

	return[[],[],[],[]]



@app.callback(

	Output("vlr_retorno_neg_param_media","children"),
	Output("vlr_retorno_neg_param_std","children"),
	Output("vlr_retorno_neg_param_min","children"),
	Output("vlr_retorno_neg_param_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_taxa_retorno_param(acao_selecionada):


	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_param.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)

		return [round(df["Taxa retorno"].mean(),2),round(df["Taxa retorno"].std(),2),round(df["Taxa retorno"].min(),2),round(df["Taxa retorno"].max(),2)]

	return[[],[],[],[]]





#INFO DAS NEGOCIAÇÕES POR MÊS
@app.callback(

	Output("vlr_venda_neg_mes_media","children"),
	Output("vlr_venda_neg_mes_std","children"),
	Output("vlr_venda_neg_mes_min","children"),
	Output("vlr_venda_neg_mes_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_vendas_mes(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_mes.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		return [round(df["Valor venda"].mean(),2),round(df["Valor venda"].std(),2),round(df["Valor venda"].min(),2),round(df["Valor venda"].max(),2)]

	return[[],[],[],[]]

@app.callback(

	Output("vlr_compra_neg_mes_media","children"),
	Output("vlr_compra_neg_mes_std","children"),
	Output("vlr_compra_neg_mes_min","children"),
	Output("vlr_compra_neg_mes_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_compra_mes(acao_selecionada):


	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_mes.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		return [round(df["Valor compra"].mean(),2),round(df["Valor compra"].std(),2),round(df["Valor compra"].min(),2),round(df["Valor compra"].max(),2)]


	return[[],[],[],[]]

@app.callback(

	Output("vlr_lucro_neg_mes_media","children"),
	Output("vlr_lucro_neg_mes_std","children"),
	Output("vlr_lucro_neg_mes_min","children"),
	Output("vlr_lucro_neg_mes_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_lucro_mes(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_mes.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)

		

		return [round(df["Lucro"].mean(),2),round(df["Lucro"].std(),2),round(df["Lucro"].min(),2),round(df["Lucro"].max(),2)]

	return[[],[],[],[]]

@app.callback(

	Output("vlr_retorno_neg_mes_media","children"),
	Output("vlr_retorno_neg_mes_std","children"),
	Output("vlr_retorno_neg_mes_min","children"),
	Output("vlr_retorno_neg_mes_max","children"),
	[Input("select_acao_selecionada","value")]

)

def info_taxa_retorno_mes(acao_selecionada):


	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_mes.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		return [round(df["Taxa retorno"].mean(),2),round(df["Taxa retorno"].std(),2),round(df["Taxa retorno"].min(),2),round(df["Taxa retorno"].max(),2)]

	return[[],[],[],[]]


@app.callback(
    Output('tabela_negociacoes_param', 'children'),
    Input("select_acao_selecionada","value"),
)
def imprimir_tabela_negociacoes_param (acao_selecionada):



	if len(acao_selecionada) >0:


		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_param.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		
		df.reset_index(inplace=False)

		df = df.sort_index(ascending=False)

		df['Valor compra'] = round(df['Valor compra'],2)
		df['Valor venda'] = round(df['Valor venda'],2)
		df['Lucro'] = round(df['Lucro'],2)
		df['Taxa retorno'] = round(df['Taxa retorno'],2)

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
    Output('tabela_negociacoes_mes', 'children'),
    [Input("select_acao_selecionada","value")]
)
def imprimir_tabela_negociacoes_mes (acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_original = pd.read_csv("Arquivos/Info/negociacoes_mes.csv")	

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)


		df.reset_index(inplace=False)

		df = df.sort_index(ascending=False)

		
		df['Valor compra'] = round(df['Valor compra'],2)
		df['Valor venda'] = round(df['Valor venda'],2)
		df['Lucro'] = round(df['Lucro'],2)
		df['Taxa retorno'] = round(df['Taxa retorno'],2)
		

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
	Output('grafico_negociacoes_param','figure'),
	[Input("select_acao_selecionada","value")]
)

def popula_grafico_negocios_param(acao_selecionada):

	if len(acao_selecionada)>0:

		Quantidade_dias_anteriores = 30

		df_compra = pd.DataFrame()
		df_venda = pd.DataFrame()


		df_original = pd.read_csv("Arquivos/Info/negociacoes_param.csv")		
		
		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]


		df = df.tail(Quantidade_dias_anteriores)

		df['Valor compra'] = round(df['Valor compra'])
		df['Valor venda'] = round(df['Valor venda'])

		
		
		fig = go.Figure()
		fig.add_trace(go.Scatter(name='Altas', x=df['Data venda'], y=df['Valor venda'], mode='lines'))
		fig.add_trace(go.Scatter(name='Baixas', x=df['Data compra'], y=df['Valor compra'], mode='lines'))
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')


		return fig


	fig = go.Figure()
	return fig


@app.callback(
	Output('grafico_negociacoes_mes','figure'),
	[Input("select_acao_selecionada","value")]
)

def popula_grafico_negocios_mes(acao_selecionada):

	Quantidade_dias_anteriores = 30

	if len(acao_selecionada)>0:

		df_compra = pd.DataFrame()
		df_venda = pd.DataFrame()

		df_original = pd.read_csv("Arquivos/Info/negociacoes_mes.csv")		

		if isinstance(acao_selecionada,list):
			df = df_original.loc[df_original["ticker"] == acao_selecionada[0]]

		else:
			df = df_original.loc[df_original["ticker"] == acao_selecionada]

		df = df.tail(Quantidade_dias_anteriores)

		df['Valor compra'] = round(df['Valor compra'])
		df['Valor venda'] = round(df['Valor venda'])


		fig = go.Figure()
		fig.add_trace(go.Scatter(name='Altas', x=df['Data venda'], y=df['Valor venda'], mode='lines'))
		fig.add_trace(go.Scatter(name='Baixas', x=df['Data compra'], y=df['Valor compra'], mode='lines'))
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return fig

	fig = go.Figure()
	return fig