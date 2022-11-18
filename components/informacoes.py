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
from dash import dcc


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
			dbc.Row([
				dbc.Row([				
					dbc.Col([
						html.H5("MACD"),
					],width=10),
					dbc.Col([
						dbc.Button(id="config_macd",children=["Configurações"])
					],width=2),
				]),
				html.Hr(),

				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="macd_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),

			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="macd_marker_slice")
				
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
					
					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_macd_info"))
					]),
				],width=12),
			]),
			

		],style={"padding": "25px"}),


		dbc.Row([
			dbc.Row([
				dbc.Row([				
					dbc.Col([
						html.H5("Bollinger"),
					],width=10),
					dbc.Col([
						dbc.Button(id="config_bollinger",children=["Configurações"])
					],width=2),
				]),
				html.Hr(),
				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="bollinger_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),

			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="bollinger_marker_slice")
				
				],width=12),
			]),			

			dbc.Row([
				dbc.Col([
					
					html.Hr(),

					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_boolinger_info"))
					]),
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([
			dbc.Row([
				dbc.Row([				
					dbc.Col([
						html.H5("RSI"),
					],width=10),
					dbc.Col([
						dbc.Button(id="config_rsi",children=["Configurações"])
					],width=2),
				]),
				html.Hr(),
				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="rsi_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="rsi_marker_slice")
				
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_rsi_info"))
					]),
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Row([
				
				html.H5("Candlestick"),
				html.Hr(),

				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="candle_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),

			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="candle_marker_slice")
				
				],width=12),
			]),

			dbc.Row([
				dbc.Col([

					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_candlestick_info"))
					]),
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([

			dbc.Row([
				
				html.H5("Regressão linear"),
				html.Hr(),

				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="regressao_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="regressao_marker_slice")
				
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_regressao_info"))
					]),
				]),
			])

		],style={"padding": "25px"}),


		
		dbc.Row([

			dbc.Row([
				dbc.Row([				
					dbc.Col([
						html.H5("SAR"),
					],width=10),
					dbc.Col([
						dbc.Button(id="config_sar",children=["Configurações"])
					],width=2),
				]),
				html.Hr(),

				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="sar_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="sar_marker_slice")
				
				],width=12),
			]),
			dbc.Row([
				dbc.Col([
					

					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_sar_info"))
					]),
				]),
			]),

		],style={"padding": "25px"}),


		dbc.Row([
			dbc.Row([
				
				dbc.Row([				
					dbc.Col([
						html.H5("Force Index"),
					],width=10),
					dbc.Col([
						dbc.Button(id="config_force_index",children=["Configurações"])
					],width=2),
				]),
				html.Hr(),

				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="force_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="force_marker_slice")
				
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_ForceIndex_info"))
					]),
				]),
			])

		],style={"padding": "25px"}),




		#Modal MACD------------------------------------------
		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Configurações MACD")),

			dbc.ModalBody([
				dbc.Row([
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

                ]),

			]),

			dbc.ModalFooter([
				dbc.Button("Aplicar",id="aplicar_macd",color="success"),
				dbc.Button("Restaurar padrão",id="restaurar_macd",color="warning"),
			])

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_macd",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),


        #Modal Bollinger------------------------------------------
		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Configurações Bollinger")),

			dbc.ModalBody([
				dbc.Row([
                    dbc.Col([
						html.H5("Dias anteriores (padrão 10)"),
						dcc.Input(id="dias_anteriores_bollinger", type="number",className="form-control form-control-lg"),
					]),

					dbc.Col([
						html.H5("Quantidade de desvio padrão superior (padrão 1.5)"),
						dcc.Input(id="mm_superior", type="number",className="form-control form-control-lg"),
					]),
					dbc.Col([
						html.H5("Quantidade de desvio padrão inferior (padrão 1.5)"),
						dcc.Input(id="mm_inferior", type="number",className="form-control form-control-lg"),
					]),

                ]),

			]),

			dbc.ModalFooter([
				dbc.Button("Aplicar",id="aplicar_bollinger",color="success"),
				dbc.Button("Restaurar padrão",id="restaurar_bollinger",color="warning"),
			])

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_bollinger",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),


        #Modal RSI------------------------------------------
		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Configurações RSI")),

			dbc.ModalBody([
				dbc.Row([
                    dbc.Col([
						html.H5("Inferior (padrão 0.3)"),
						dcc.Input(id="inferior_rsi", type="number",className="form-control form-control-lg"),
					]),

					dbc.Col([
						html.H5("Superior (padrão 0.7)"),
						dcc.Input(id="superior_rsi", type="number",className="form-control form-control-lg"),
					]),
					dbc.Col([
						html.H5("Dias anteriores (padrão 14)"),
						dcc.Input(id="dias_anteriores_rsi", type="number",className="form-control form-control-lg"),
					]),

                ]),

			]),

			dbc.ModalFooter([
				dbc.Button("Aplicar",id="aplicar_rsi",color="success"),
				dbc.Button("Restaurar padrão",id="restaurar_rsi",color="warning"),
			])

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_rsi",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),


        #Modal SAR------------------------------------------
		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Configurações SAR")),

			dbc.ModalBody([
				dbc.Row([
                    dbc.Col([
						html.H5("IAF (padrão 0.2)"),
						dcc.Input(id="iax", type="number",className="form-control form-control-lg"),
					]),

					dbc.Col([
						html.H5("MAX AF (padrão 0.2)"),
						dcc.Input(id="max_af", type="number",className="form-control form-control-lg"),
					]),
                ]),

			]),

			dbc.ModalFooter([
				dbc.Button("Aplicar",id="aplicar_sar",color="success"),
				dbc.Button("Restaurar padrão",id="restaurar_sar",color="warning"),
			])

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_sar",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),


		#Modal Force Index------------------------------------------
		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Configurações Force Index")),

			dbc.ModalBody([
				dbc.Row([
                    dbc.Col([
						html.H5("Dias anteriores (padrão 21)"),
						dcc.Input(id="dias_anteriores_force_index", type="number",className="form-control form-control-lg"),
					]),
                ]),

			]),

			dbc.ModalFooter([
				dbc.Button("Aplicar",id="aplicar_force_index",color="success"),
				dbc.Button("Restaurar padrão",id="restaurar_force_index",color="warning"),
			])

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_force_index",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),
])


@app.callback(
	Output('grafico_boolinger_info','figure'),
	Output("bollinger_marker_slice","min"),
	Output("bollinger_marker_slice","max"),
	[Input("select_acao_selecionada","value"),
	Input("bollinger_marker","value"),
	Input("bollinger_marker_slice","value")]
)


def popula_boolinger(acao_selecionada,tempo,tempo_slice):

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
		datas = funcoes.data_slicer(tempo_slice)

		mm_superior = 1.5

		mm_inferior = 1.5
		#-----------------------------------------


		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)


		df = pd.DataFrame(df[str(datas[0]):str(datas[1])]['Close'])



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


		'''
		sup_band.to_csv("Arquivos/Bollinger/"+arquivo+"sup_band.csv")
		inf_band.to_csv("Arquivos/Bollinger/"+arquivo+"inf_band.csv")
		mm.to_csv("Arquivos/Bollinger/"+arquivo+"mm.csv")
		std.to_csv("Arquivos/Bollinger/"+arquivo+"std.csv")
		compras.to_csv("Arquivos/Bollinger/"+arquivo+"compras.csv")
		vendas.to_csv("Arquivos/Bollinger/"+arquivo+"vendas.csv")
		bandas_bollinger.to_csv("Arquivos/Bollinger/"+arquivo+"bandas_bollinger.csv")
		df.to_csv("Arquivos/Bollinger/"+arquivo+"fechamentos.csv")
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


		fig.update_layout(xaxis_rangeslider_visible=True)
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return [fig,4,tempo]
			
	return [{},4,tempo]

@app.callback(
	Output('grafico_macd_info','figure'),
	Output("macd_marker_slice","min"),
	Output("macd_marker_slice","max"),
	Input("select_acao_selecionada","value"),
	Input("macd_marker","value"),
	Input("macd_marker_slice","value")
	
)



def popula_macd(acao_selecionada,tempo,tempo_slice):


	

	if len(acao_selecionada) > 0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]

		else:
			
			ticker = acao_selecionada


		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")



		#ATRIBUTOS---------------------------

		datas = funcoes.data_slicer(tempo_slice)
		
		rapida = 12
		lenta = 26
		sinal = 9
		#------------------------------------



		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)

		
		df = pd.DataFrame(df[str(datas[0]):str(datas[1])]['Close'])
		

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

		'''
		df["Close"].to_csv("Arquivos/Macd/"+arquivo+"close.csv")
		pd.DataFrame(MACD).to_csv("Arquivos/Macd/"+arquivo+"macd.csv")
		pd.DataFrame(sinal).to_csv("Arquivos/Macd/"+arquivo+"sinal.csv")
		'''

		fig.update_layout(xaxis_rangeslider_visible=True)
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
		

		return [fig,4,tempo]

	return [{},4,tempo]



@app.callback(
	Output('grafico_rsi_info','figure'),
	Output("rsi_marker_slice","min"),
	Output("rsi_marker_slice","max"),
	Input("select_acao_selecionada","value"),
	Input("rsi_marker","value"),
	Input("rsi_marker_slice","value")
)

def popula_rsi(acao_selecionada,tempo,tempo_slice):


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
		datas = funcoes.data_slicer(tempo_slice)

		superior = 0.7
		inferior = 0.3
		dias_anteriores = 14


		#------------------------------------


		df.set_index("Date",inplace=True)
		
		df = pd.DataFrame(df[str(datas[0]):str(datas[1])]['Close'])


		df = df[df.index > str(datas[0])]

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
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return [fig,4,tempo]

	return [{},4,tempo]


@app.callback(
	Output('grafico_candlestick_info','figure'),
	Output("candle_marker_slice","min"),
	Output("candle_marker_slice","max"),
	[Input("select_acao_selecionada","value"),
	Input("candle_marker","value"),
	Input("candle_marker_slice","value")]
)

def popula_candlestick(acao_selecionada,tempo,tempo_slice):


	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada


		#Atributos--------------------------------
		datas = funcoes.data_slicer(tempo_slice)

		#-----------------------------------------

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)


		df = pd.DataFrame(df[str(datas[0]):str(datas[1])])

		fig = go.Figure()
		fig.add_trace(go.Candlestick(
		    name='Fechamento', 
		    x=df.index, 
		    open=df["Open"], 
		    high=df["High"],
		    low=df["Low"],
		    close=df["Close"]))

		fig.update_layout(height=700)
		fig.update_layout(xaxis_rangeslider_visible=True)
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return [fig,4,tempo]


	return [{},4,tempo]


@app.callback(
	Output('grafico_regressao_info','figure'),
	Output("regressao_marker_slice","min"),
	Output("regressao_marker_slice","max"),
	Input("select_acao_selecionada","value"),
	Input("regressao_marker","value"),
	Input("regressao_marker_slice","value")
)


def popula_regressao(acao_selecionada,tempo,tempo_slice):

	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada

		

		#Atributos--------------------------------
		datas = funcoes.data_slicer(tempo_slice)

		#-----------------------------------------

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)


		df = pd.DataFrame(df[str(datas[0]):str(datas[1])])


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

		fig.update_layout(xaxis_rangeslider_visible=True)
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return [fig,4,tempo]


	return [{},4,tempo]


@app.callback(
	Output('grafico_sar_info','figure'),
	Output("sar_marker_slice","min"),
	Output("sar_marker_slice","max"),
	[Input("select_acao_selecionada","value"),
	Input("sar_marker","value"),
	Input("sar_marker_slice","value")]
)


def popula_sar(acao_selecionada,tempo,tempo_slice):
	
	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada

		

		#Atributos--------------------------------
		datas = funcoes.data_slicer(tempo_slice)

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

		df = pd.DataFrame(df[str(datas[0]):str(datas[1])])

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

		fig.update_layout(xaxis_rangeslider_visible=True)
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return [fig,4,tempo]

	return [{},4,tempo]



@app.callback(
	Output('grafico_ForceIndex_info','figure'),
	Output("force_marker_slice","min"),
	Output("force_marker_slice","max"),
	[Input("select_acao_selecionada","value"),
	Input("force_marker","value"),
	Input("force_marker_slice","value")]
)

def popula_forceIndex(acao_selecionada,tempo,tempo_slice):
	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]

		else:
			
			ticker = acao_selecionada


		#Atributos--------------------------------
		datas = funcoes.data_slicer(tempo_slice)

		n = 21

		#-----------------------------------------

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]
			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)

		df["Date"] = df.index

		df = pd.DataFrame(df[str(datas[0]):str(datas[1])])

		AAPL_ForceIndex = funcoes.ForceIndex(df,n)

		fig = go.Figure()

		fig.add_trace(
		    go.Scatter(
		        name="Fechamento",
		        x=AAPL_ForceIndex.index,
		        y=AAPL_ForceIndex["ForceIndex"],
		        line=dict(color='blue', width=1))
		)
		fig.add_hline(y=AAPL_ForceIndex["Close"].max(),line_color="red")



		fig.update_layout(xaxis_rangeslider_visible=True)
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return [fig,4,tempo]


	return [{},4,tempo]






#Modais

@app.callback(
    Output('modal_macd','is_open'),
    Input('config_macd','n_clicks'),
    State('modal_macd','is_open'),
)
def open_modal_macd(n1,is_open):

	if n1:
		return not is_open


@app.callback(
    Output('modal_bollinger','is_open'),
    Input('config_bollinger','n_clicks'),
    State('modal_bollinger','is_open'),
)
def open_modal_bollinger(n1,is_open):

	if n1:
		return not is_open


@app.callback(
    Output('modal_rsi','is_open'),
    Input('config_rsi','n_clicks'),
    State('modal_rsi','is_open'),
)
def open_modal_rsi(n1,is_open):

	if n1:
		return not is_open



@app.callback(
    Output('modal_sar','is_open'),
    Input('config_sar','n_clicks'),
    State('modal_sar','is_open'),
)
def open_modal_sar(n1,is_open):

	if n1:
		return not is_open


@app.callback(
    Output('modal_force_index','is_open'),
    Input('config_force_index','n_clicks'),
    State('modal_force_index','is_open'),
)
def open_modal_force_index(n1,is_open):

	if n1:
		return not is_open