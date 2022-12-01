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
import math

import pdb
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO
import funcoes




layout = dbc.Col([

		dbc.Row([
			dbc.Col([
				html.H1("Indicadores", className="text-primary"),
			]),
		],style={"padding": "25px"}),


		dbc.Row([
			dbc.Row([
				dbc.Row([				
					dbc.Col([
						html.H5("Aroon"),
					],width=8),
					dbc.Col([
						dbc.Button(id="negociacoes_aroon",children=["Negociações"])
					],width=2),
					dbc.Col([
						dbc.Button(id="config_aroon",children=["Configurações"])
					],width=2),
				]),
				html.Hr(),

				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="aroon_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12),

			]),

			dbc.Row([
				dbc.Col([
				
					dcc.RangeSlider(step=1,value=[4,8],id="aroon_marker_slice")
				
				],width=12),
			]),

			dbc.Row([
				dbc.Col([
					
					dbc.Col([
						dbc.Card(dcc.Graph(id="grafico_aroon_info"))
					]),
				],width=12),
			]),
			

		],style={"padding": "25px"}),



		dbc.Row([
			dbc.Row([
				dbc.Row([				
					dbc.Col([
						html.H5("MACD"),
					],width=8),
					dbc.Col([
						dbc.Button(id="negociacoes_macd",children=["Negociações"])
					],width=2),
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
					],width=8),
					dbc.Col([
						dbc.Button(id="negociacoes_bollinger",children=["Negociações"])
					],width=2),
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
					],width=8),
					dbc.Col([
						dbc.Button(id="negociacoes_rsi",children=["Negociações"])
					],width=2),
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
				dbc.Row([				
					dbc.Col([
						html.H5("SAR"),
					],width=8),
					dbc.Col([
						dbc.Button(id="negociacoes_sar",children=["Negociações"])
					],width=2),
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
					],width=8),
					dbc.Col([
						dbc.Button(id="negociacoes_force_index",children=["Negociações"])
					],width=2),
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

		dbc.Row([

			dbc.Row([
				dbc.Row([				
					dbc.Col([
						html.H5("Candlestick"),
					],width=10),
					dbc.Col([
						dbc.Button(id="config_candlestick",children=["Configurações"])
					],width=2),
				]),
				html.Hr(),
				dbc.Col([
					dcc.Slider(4, 48,
					    step=None,id="candle_marker2",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48'},value=8
					)
				],width=12,style={'display':'none'}),

				
				dbc.Col([
					dcc.Slider(4, 240,
					    step=None,id="candle_marker",
					    marks={4: '4',8: '8',12:'12',16:'16',20:'20',24:'24',28:'28',32:'32',
					        36:'36',40:'40',44:'44',48:'48',52:'52',56:'56',60:'60',64:'64',
					        68:'68',72:'72',76:'76',80:'80',84:'84',88:'88',92:'92',96:'96',
					        100:'100',104:'104',108:'108',112:'112',116:'116',120:'120',124:'124',
					        128:'128',132:'132',136:'136',140:'140',144:'144',148:'148',152:'152',
					        154:'154',156:'156',160:'160',164:'164',168:'168',172:'172',176:'176',
					        180:'180',184:'184',188:'188',192:'192',196:'196',180:'180',184:'184',
					        188:'188',192:'192',196:'196',200:'200',204:'204',208:'208',212:'212',
					        216:'216',220:'220',224:'224',228:'228',232:'232',236:'236',240:'240'},value=8,

					)
				],width=12,style={'display':''}),
				
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

		#Modal Aroon------------------------------------------
		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Configurações aroon")),

			dbc.ModalBody([
				dbc.Row([
                    dbc.Col([
						html.H5("Dias anteriores (padrão 25)"),
						dcc.Input(id="dias_anteriores_aroon", type="number",className="form-control form-control-lg"),
					]),
                ]),

			]),

			dbc.ModalFooter([
				dbc.Button("Aplicar",id="aplicar_aroon",color="success"),
				dbc.Button("Restaurar padrão",id="restaurar_macd",color="warning"),
			])

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_aroon",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),

		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Negociações aroon")),

			dbc.ModalBody([
				dbc.Row([
               		dbc.Col([
               			dbc.Row([
               				html.H5("Tabela de compras"),
               			]),
               			dbc.Row([
               				html.Div(id="tabela_compras_aroon", className="dbc"),
               			]),
               			

               		],width=6),

					dbc.Col([
						dbc.Row([
							html.H5("Tabela de vendas"),
						]),

						dbc.Row([
							html.Div(id="tabela_vendas_aroon", className="dbc"),
						]),

					],width=6),
                ]),
                dbc.Row([

                	dbc.Col([
                		dbc.Card([
                			dbc.CardBody([
                				html.H4("Porcentagem média de retorno", className="card-title"),
                				html.H5(id="confianca_aroon"),
                			]),
                		])
                	]),
                	dbc.Col([
                		dbc.Card([
                			dbc.CardBody([
                				html.H4("Quantidade de negociações", className="card-title"),
                				html.H5(id="qtd_negociacao_aroon"),
                			]),
                		])
                	]),
       			]),

			]),

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_negociacoes_aroon",
        size="xl",
        is_open=False,
        centered=True,
        backdrop=True),



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

		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Negociações macd")),

			dbc.ModalBody([
				dbc.Row([
               		dbc.Col([
               			dbc.Row([
               				html.H5("Tabela de compras"),
               			]),
               			dbc.Row([
               				html.Div(id="tabela_compras_macd", className="dbc"),
               			]),

               		],width=6),

					dbc.Col([
						dbc.Row([
							html.H5("Tabela de vendas"),
						]),
						

						dbc.Row([
							html.Div(id="tabela_vendas_macd", className="dbc"),
						]),

					],width=6),
                ]),
                dbc.Row([
       				html.H5(id="confianca_macd"),
       			]),

			]),

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_negociacoes_macd",
        size="xl",
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


        dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Negociações bollinger")),

			dbc.ModalBody([
				dbc.Row([
               		dbc.Col([
               			dbc.Row([
               				html.H5("Tabela de compras"),
               			]),
               			
               			dbc.Row([
               				html.Div(id="tabela_compras_bollinger", className="dbc"),
               			]),

               		],width=6),

					dbc.Col([
						dbc.Row([
							html.H5("Tabela de vendas"),
						]),

						dbc.Row([
							html.Div(id="tabela_vendas_bollinger", className="dbc"),
						]),

					],width=6),
                ]),
                dbc.Row([
       				html.H5(id="confianca_bollinger"),
       			]),

			]),

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_negociacoes_bollinger",
        size="xl",
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



		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Negociações RSI")),

			dbc.ModalBody([
				dbc.Row([
               		dbc.Col([
               			dbc.Row([
               				html.H5("Tabela de compras"),
               			]),
               			
               			dbc.Row([
               				html.Div(id="tabela_compras_rsi", className="dbc"),
               			]),

               		],width=6),

					dbc.Col([
						dbc.Row([
							html.H5("Tabela de vendas"),
						]),

						dbc.Row([
							html.Div(id="tabela_vendas_rsi", className="dbc"),
						]),

					],width=6),
                ]),
                dbc.Row([
       				html.H5(id="confianca_rsi"),
       			]),

			]),

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_negociacoes_rsi",
        size="xl",
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


		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Negociações SAR")),

			dbc.ModalBody([
				dbc.Row([
               		dbc.Col([
               			dbc.Row([
               				html.H5("Tabela de compras"),
               			]),
               			
               			dbc.Row([
               				html.Div(id="tabela_compras_sar", className="dbc"),
               			]),

               		],width=6),

					dbc.Col([
						dbc.Row([
							html.H5("Tabela de vendas"),
						]),

						dbc.Row([
							html.Div(id="tabela_vendas_sar", className="dbc"),
						]),

					],width=6),
                ]),
                dbc.Row([
       				html.H5(id="confianca_sar"),
       			]),

			]),

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_negociacoes_sar",
        size="xl",
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


        #Modal CandleStick------------------------------------------
		dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Configurações Candlestick")),

			dbc.ModalBody([
				dbc.Row([
                    dbc.Col([
						html.H5("Primeira media móvel"),
						dcc.Input(id="primeira_mm", type="number",className="form-control form-control-lg"),
					],width=3),

					dbc.Col([
						html.H5("Segunda média móvel"),
						dcc.Input(id="segunda_mm", type="number",className="form-control form-control-lg"),
					],width=3),
                ]),

			]),

			dbc.ModalFooter([
				dbc.Button("Aplicar",id="aplicar_candlestick",color="success"),
				dbc.Button("Restaurar padrão",id="restaurar_force_index",color="warning"),
			])

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_candlestick",
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True),


        dbc.Modal([
			dbc.ModalHeader(dbc.ModalTitle("Negociações force index")),

			dbc.ModalBody([
				dbc.Row([
               		dbc.Col([
               			dbc.Row([
               				html.H5("Tabela de compras"),
               			]),
               			dbc.Row([
               				html.Div(id="tabela_compras_force_index", className="dbc"),
               			]),

               		],width=6),

					dbc.Col([
						dbc.Row([
							html.H5("Tabela de vendas"),
						]),
						

						dbc.Row([
							html.Div(id="tabela_vendas_force_index", className="dbc"),
						]),

					],width=6),
                ]),
                dbc.Row([
               		html.H5(id="confianca_force_index"),
               	]),

			]),

		],style={"background-color":"rgba(17,140,79,0.05)"},
        id="modal_negociacoes_force_index",
        size="xl",
        is_open=False,
        centered=True,
        backdrop=True),
])


@app.callback(
	Output('grafico_aroon_info','figure'),
	Output("aroon_marker_slice","min"),
	Output("aroon_marker_slice","max"),
	[Input("select_acao_selecionada","value"),
	Input("aroon_marker","value"),
	Input("aroon_marker_slice","value"),
	Input("Aroon_store","data")
	]

)

def popula_aroon(acao_selecionada,tempo,tempo_slice,aroon_store):

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
		dias_anteriores_aroon = aroon_store[0]

		#-----------------------------------------


		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)

		df = pd.DataFrame(df[str(datas[0]):str(datas[1])])

		date=df.index.to_list()
		highp=df["High"].to_list() # converter tudo pra lista facilita as coisas
		lowp=df["Low"].to_list()
		tf=dias_anteriores_aroon# 25 days to analyse
		AroonUp=[] 
		AroonDown=[]
		AroonDate=[]
		x=tf # ele temque comecar no ponto 25 (vulgo ignora-se os 25 primeiros dados)
		while x<len(date): # ele vai do ponto 25 até o tamanho máximo da lista
		    Aroon_up=((highp[x-tf:x].index(max(highp[x-tf:x])))/float(tf))*100 # ele pega tf periodos anteriores e olha até o ponto atual da análise, buscando o indice que está o ponto máximo dentre as máximas do ativo 
		    Aroon_down=((lowp[x-tf:x].index(min(lowp[x-tf:x])))/float(tf))*100# ele pega tf periodos anteriores e olha até o ponto atual da análise, buscando o indice que está o ponto minimo dentre o low do ativo
		    AroonUp.append(Aroon_up) 
		    AroonDown.append(Aroon_down) 
		    AroonDate.append(date[x])
		    x+=1
		df_teste=pd.DataFrame()
		AroonDown=pd.Series(AroonDown)
		df_teste["Aroon_Down"]=AroonDown
		AroonUp=pd.Series(AroonUp)
		df_teste["Aroon_Up"]=AroonUp
		AroonDate=pd.Series(AroonDate)
		df_teste["Aroon_Date"]=AroonDate
		df_teste=df_teste.set_index("Aroon_Date")

		
		df_teste.to_csv("Arquivos/Aroon/aroon"+arquivo+".csv")

		fig = go.Figure()

		fig.add_trace(
		    go.Scatter(
		        name="Aroon Up - Venda",
		        x=df_teste.index,
		        y=df_teste["Aroon_Up"],
		        line=dict(color='green', width=2))
		)
		fig.add_trace(
		    go.Scatter(
		        name="Aroon Down- Compra",
		        x=df_teste.index,
		        y=df_teste["Aroon_Down"],
		        line=dict(color='red', width=2))
		)

		fig.add_hline(y=7,line_color="blue",line_width=1, line_dash="dash")
		fig.add_hline(y=30,line_color="blue",line_width=1, line_dash="dash")
		fig.add_hline(y=50,line_color="blue",line_width=1, line_dash="dash")
		fig.add_hline(y=70,line_color="blue",line_width=1, line_dash="dash")

		fig.update_layout(xaxis_rangeslider_visible=True)
		fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

		return[fig,4,tempo]

	return [{},4,tempo]

@app.callback(
	Output('grafico_boolinger_info','figure'),
	Output("bollinger_marker_slice","min"),
	Output("bollinger_marker_slice","max"),
	[Input("select_acao_selecionada","value"),
	Input("bollinger_marker","value"),
	Input("bollinger_marker_slice","value"),
	Input("Bollinger_store","data")]
)


def popula_boolinger(acao_selecionada,tempo,tempo_slice,bollinger_store):

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

		mm_superior = bollinger_store[1]

		mm_inferior = bollinger_store[2]
		#-----------------------------------------


		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")


		if isinstance(acao_selecionada,list):
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]

			
		else:
			df = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]


		df.set_index("Date",inplace=True)


		df = pd.DataFrame(df[str(datas[0]):str(datas[1])]['Close'])



		#Médias móveis de 20 em 20 dias
		mm = df.rolling(bollinger_store[0]).mean()

		#Desvio padrão de 20 em 20 dias
		std = df.rolling(bollinger_store[0]).std()

		

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


		
		#sup_band.to_csv("Arquivos/Bollinger/"+arquivo+"sup_band.csv")
		#inf_band.to_csv("Arquivos/Bollinger/"+arquivo+"inf_band.csv")
		#mm.to_csv("Arquivos/Bollinger/"+arquivo+"mm.csv")
		#std.to_csv("Arquivos/Bollinger/"+arquivo+"std.csv")
		compras.to_csv("Arquivos/Bollinger/"+arquivo+"compras.csv")
		vendas.to_csv("Arquivos/Bollinger/"+arquivo+"vendas.csv")
		#bandas_bollinger.to_csv("Arquivos/Bollinger/"+arquivo+"bandas_bollinger.csv")
		#df.to_csv("Arquivos/Bollinger/"+arquivo+"fechamentos.csv")
		
		

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
	Input("macd_marker_slice","value"),
	Input("Macd_store","data")
	
)

def popula_macd(acao_selecionada,tempo,tempo_slice,macd_config):


	

	if len(acao_selecionada) > 0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]

		else:
			
			ticker = acao_selecionada


		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

		
		fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")



		#ATRIBUTOS---------------------------

		datas = funcoes.data_slicer(tempo_slice)
		
		rapida = macd_config[0]
		lenta = macd_config[1]
		sinal = macd_config[2]
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

		
		#df["Close"].to_csv("Arquivos/Macd/"+arquivo+"close.csv")
		pd.DataFrame(MACD).to_csv("Arquivos/Macd/"+arquivo+"macd.csv")
		pd.DataFrame(sinal).to_csv("Arquivos/Macd/"+arquivo+"sinal.csv")
		

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
	Input("rsi_marker_slice","value"),
	Input("Rsi_store","data")
)

def popula_rsi(acao_selecionada,tempo,tempo_slice,rsi_config):

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


		
		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

		#ATRIBUTOS---------------------------
		datas = funcoes.data_slicer(tempo_slice)

		inferior = rsi_config[0]
		superior = rsi_config[1]
		dias_anteriores = rsi_config[2]

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
		
		rsi.to_csv("Arquivos/RSI/rsi"+arquivo+".csv")

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
	Input("candle_marker_slice","value"),
	Input("CandleStick_store","data")]
)

def popula_candlestick(acao_selecionada,tempo,tempo_slice,candlestick_config):


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


		#criando novos campos de medias móveis
		df['mm9'] = df['Close'].rolling(candlestick_config[0]).mean()
		df['mm11'] = df['Close'].rolling(candlestick_config[1]).mean()


		fig = go.Figure()
		fig.add_trace(go.Candlestick(
		    name='Fechamento', 
		    x=df.index, 
		    open=df["Open"], 
		    high=df["High"],
		    low=df["Low"],
		    close=df["Close"]))

		fig.add_trace(go.Scatter(x = df.index,y = df["mm9"],name = "Média móvel "+str(candlestick_config[0]), line_color = "green"))
		fig.add_trace(go.Scatter(x = df.index,y = df["mm11"],name = "Média móvel "+str(candlestick_config[1]), line_color = "yellow"))

		fig.update_layout(height=700)
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
	Input("sar_marker_slice","value"),
	Input("Sar_store","data")]
)


def popula_sar(acao_selecionada,tempo,tempo_slice,sar_config):
	
	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]


		else:
			
			ticker = acao_selecionada

		

		#Atributos--------------------------------
		datas = funcoes.data_slicer(tempo_slice)

		iaf = sar_config[0]

		maxaf = sar_config[1]

		#-----------------------------------------
		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker
		
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

		SAR_df.to_csv("Arquivos/Sar/sar"+arquivo+".csv")


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
	Input("force_marker_slice","value"),
	Input("ForceIndex_store","data")]
)

def popula_forceIndex(acao_selecionada,tempo,tempo_slice,forceIndex_config):
	if len(acao_selecionada)>0:

		if isinstance(acao_selecionada,list):
			
			ticker = acao_selecionada[0]

		else:
			
			ticker = acao_selecionada

		arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

		#Atributos--------------------------------
		datas = funcoes.data_slicer(tempo_slice)

		n = forceIndex_config[0]

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

		AAPL_ForceIndex.to_csv("Arquivos/ForceIndex/forceIndex"+arquivo+".csv")

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



#Modal macd--------------------------------------------------
@app.callback(
    Output('modal_macd','is_open'),
    Input('config_macd','n_clicks'),
    State('modal_macd','is_open'),
)
def open_modal_macd(n1,is_open):

	if 'config_macd'==ctx.triggered_id:
		return not is_open

@app.callback(
	Output("Macd_store","data"),
	Input("aplicar_macd","n_clicks"),
	Input("rapida_mm","value"),
	Input("lenta_mm","value"),
	Input("sinal","value")
)
def aplicar_macd(n1,rapida,lenta,sinal):

	if "aplicar_macd" == ctx.triggered_id:

		if rapida == None or rapida == "":
			rapida = 12

		if lenta == None or lenta == "":
			lenta = 26

		if sinal == None or sinal == "":
			sinal = 9


		return [rapida,lenta,sinal]

	return [12,26,9]


@app.callback(
    Output('modal_negociacoes_macd','is_open'),
    Output('tabela_compras_macd','children'),
    Output('tabela_vendas_macd','children'),
    Output('confianca_macd','children'),
    Input('negociacoes_macd','n_clicks'),
    Input("select_acao_selecionada","value"),
    State('modal_negociacoes_macd','is_open'),
)
def open_negociacoes_macd(n1,acao_selecionada,is_open):
	
	if "negociacoes_macd" == ctx.triggered_id:

		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
				
				ticker = acao_selecionada[0]

			else:
				
				ticker = acao_selecionada


			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

			sinal = pd.read_csv("Arquivos/Macd/"+arquivo+"sinal.csv")
			macd = pd.read_csv("Arquivos/Macd/"+arquivo+"macd.csv")


			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")

			if isinstance(acao_selecionada,list):
				df_fechamento = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]
				
			else:
				df_fechamento = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]



			maior = 0
			compras = list()
			vendas = list()

			i = 0
			
			while i < len(sinal):

				if maior == 0:
					if macd["Close"].values[i] > sinal["Close"].values[i]:

						compras.append(macd["Date"].values[i])

						maior = 1

				else:

					if macd["Close"].values[i] < sinal["Close"].values[i]:
						
						vendas.append(macd["Date"].values[i])

						maior = 0
				i+=1

			
			compras = pd.DataFrame(compras,columns=["Date"])			
			vendas = pd.DataFrame(vendas,columns=["Date"])

			compras["Valor"] = getMACDValues(compras,df_fechamento)
			vendas["Valor"] = getMACDValues(vendas,df_fechamento)

			tabela_compra = dash_table.DataTable(compras.to_dict('records'), [{"name": i, "id": i} for i in compras.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			tabela_venda = dash_table.DataTable(vendas.to_dict('records'), [{"name": i, "id": i} for i in vendas.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			conf = calculaConfiabilidade(compras,vendas)


			return not is_open,tabela_compra,tabela_venda,round(sum(conf)/len(conf),2)

	return is_open,[],[],[]



def getMACDValues(macd,fechamento):

	valores_macd = list()

	i = 0
	while i < len(macd):

		j = 0

		while j < len(fechamento):

			if macd["Date"].values[i] == fechamento["Date"].values[j]:
				valores_macd.append(round(fechamento["Close"].values[j],2))

			j+=1

		i+=1

	return valores_macd
#-----------------------------------------------------------



#Modal bollinger------------------------------------------
@app.callback(
    Output('modal_bollinger','is_open'),
    Input('config_bollinger','n_clicks'),
    State('modal_bollinger','is_open'),
)
def open_modal_bollinger(n1,is_open):

	if 'config_bollinger'==ctx.triggered_id:
		return not is_open


@app.callback(
	Output("Bollinger_store","data"),
	Input("aplicar_bollinger","n_clicks"),
	Input("dias_anteriores_bollinger","value"),
	Input("mm_inferior","value"),
	Input("mm_superior","value"),
)
def aplicar_bollinger(n1,dias_anteriores,mm_inferior,mm_superior):

	if "aplicar_bollinger" == ctx.triggered_id:

		if dias_anteriores == None or dias_anteriores == "":
			dias_anteriores = 10

		if mm_superior == None or mm_superior == "":
			mm_superior = 1.5

		if mm_inferior == None or mm_inferior == "":
			mm_inferior = 1.5

		return [dias_anteriores,mm_inferior,mm_superior]

	return [10,1.5,1.5]


@app.callback(
    Output('modal_negociacoes_bollinger','is_open'),
    Output('tabela_compras_bollinger','children'),
    Output('tabela_vendas_bollinger','children'),
    Output('confianca_bollinger','children'),
    Input('negociacoes_bollinger','n_clicks'),
    Input("select_acao_selecionada","value"),
    State('modal_negociacoes_macd','is_open'),
)
def open_modal_bollinger(n1,acao_selecionada,is_open):
	if "negociacoes_bollinger" == ctx.triggered_id:

		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
				
				ticker = acao_selecionada[0]

			else:
				
				ticker = acao_selecionada


			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker


			compras = pd.read_csv("Arquivos/Bollinger/"+arquivo+"compras.csv")
			vendas = pd.read_csv("Arquivos/Bollinger/"+arquivo+"vendas.csv")


			compras.drop("Superior",inplace=True,axis="columns")
			compras.drop("Inferior",inplace=True,axis="columns")
			compras.drop("ticker",inplace=True,axis="columns")

			vendas.drop("Superior",inplace=True,axis="columns")
			vendas.drop("Inferior",inplace=True,axis="columns")
			vendas.drop("ticker",inplace=True,axis="columns")


			tabela_compra = dash_table.DataTable(compras.to_dict('records'), [{"name": i, "id": i} for i in compras.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			tabela_venda = dash_table.DataTable(vendas.to_dict('records'), [{"name": i, "id": i} for i in vendas.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			compras.rename(columns={"Compras":"Valor"},inplace=True)
			vendas.rename(columns={"Vendas":"Valor"},inplace=True)

			conf = calculaConfiabilidade(compras,vendas)			
			
			return not is_open,tabela_compra,tabela_venda,round(sum(conf)/len(conf),2)

	return is_open,[],[],[]
#-----------------------------------------------------------





#Modal rsi--------------------------------------------
@app.callback(
    Output('modal_rsi','is_open'),
    Input('config_rsi','n_clicks'),
    State('modal_rsi','is_open'),
)
def open_modal_rsi(n1,is_open):

	if 'config_rsi'==ctx.triggered_id:
		return not is_open


@app.callback(
	Output("Rsi_store","data"),
	Input("inferior_rsi","value"),
	Input("superior_rsi","value"),
	Input("dias_anteriores_rsi","value"),
	Input("aplicar_rsi","n_clicks")
)
def aplicar_rsi(inferior,superior,dias_anteriores,n1):

	if "aplicar_rsi" == ctx.triggered_id:
		if inferior == None or inferior == "":
			inferior = 0.3

		if superior == None or superior == "":
			superior = 0.7

		if dias_anteriores == None or dias_anteriores == "":
			dias_anteriores = 14


		return [inferior,superior,dias_anteriores]

	return [0.3,0.7,14]


@app.callback(
    Output('modal_negociacoes_rsi','is_open'),
    Output('tabela_compras_rsi','children'),
    Output('tabela_vendas_rsi','children'),
    Output('confianca_rsi','children'),
    Input('negociacoes_rsi','n_clicks'),
    Input("select_acao_selecionada","value"),
    State('modal_negociacoes_rsi','is_open'),
    Input("Rsi_store","data")
)
def open_negociacoes_rsi(n1,acao_selecionada,is_open,rsi_config):
	if "negociacoes_rsi" == ctx.triggered_id:

		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
				
				ticker = acao_selecionada[0]

			else:
				
				ticker = acao_selecionada

			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

			rsi_df = pd.read_csv("Arquivos/RSI/rsi"+arquivo+".csv")

			fechamento_df = pd.read_csv("Arquivos/Info/fechamento.csv")

			rsi_df.drop(rsi_df.columns[2],inplace=True,axis=1)

			inferior = rsi_config[0]
			superior = rsi_config[1]

			vendas = rsi_df.loc[rsi_df["Close"]>=rsi_df["Close"].max()*superior]
			compras = rsi_df.loc[rsi_df["Close"]<=rsi_df["Close"].max()*inferior]

			vendas.drop(vendas.columns[1],inplace=True,axis=1)
			compras.drop(compras.columns[1],inplace=True,axis=1)

			vendas["Valor"] = getRSIValues(vendas,fechamento_df)
			compras["Valor"] = getRSIValues(compras,fechamento_df)

			tabela_compra = dash_table.DataTable(compras.to_dict('records'), [{"name": i, "id": i} for i in compras.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)


			tabela_venda = dash_table.DataTable(vendas.to_dict('records'), [{"name": i, "id": i} for i in vendas.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			conf = calculaConfiabilidade(compras,vendas)

			return not is_open,tabela_compra,tabela_venda,round(sum(conf)/len(conf),2)

	return is_open,[],[],[]

def getRSIValues(rsi,fechamento):

	valores_rsi = list()

	i = 0
	while i < len(rsi):

		j = 0

		while j < len(fechamento):

			if rsi["Date"].values[i] == fechamento["Date"].values[j]:
				valores_rsi.append(round(fechamento["Close"].values[j],2))

			j+=1

		i+=1

	return valores_rsi
#-----------------------------------------------------------



#Modal sar--------------------------------------------
@app.callback(
    Output('modal_sar','is_open'),
    Input('config_sar','n_clicks'),
    State('modal_sar','is_open'),
)
def open_modal_sar(n1,is_open):

	if 'config_sar'==ctx.triggered_id:
		return not is_open


@app.callback(
	Output("Sar_store","data"),
	Input("iax","value"),
	Input("max_af","value"),
	Input("aplicar_sar","n_clicks")
)
def aplicar_sar(iax,maxaf,n1):

	if "aplicar_sar" == ctx.triggered_id:

		if iax == None or iax == "":
			iax = 0.2

		if maxaf == None or maxaf == "":
			maxaf = 0.2

		return[iax,maxaf]
	return[0.2,0.2]


@app.callback(
    Output('modal_negociacoes_sar','is_open'),
    Output('tabela_compras_sar','children'),
    Output('tabela_vendas_sar','children'),
    Output('confianca_sar','children'),
    Input('negociacoes_sar','n_clicks'),
    Input("select_acao_selecionada","value"),
    State('modal_negociacoes_macd','is_open'),
)
def open_negociacoes_sar(n1,acao_selecionada,is_open):
	
	if "negociacoes_sar" == ctx.triggered_id:

		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
				
				ticker = acao_selecionada[0]

			else:
				
				ticker = acao_selecionada


			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

			SAR_df = pd.read_csv("Arquivos/Sar/sar"+arquivo+".csv")
			fechamento_df = pd.read_csv("Arquivos/Info/fechamento.csv")
			
			
			compras = SAR_df.drop(SAR_df.columns[[0,2,3,4,5,6]],axis=1)
			vendas = SAR_df.drop(SAR_df.columns[[0,2,3,4,5,7]],axis=1)

			compras.dropna(inplace=True)
			vendas.dropna(inplace=True)

			tabela_compra = dash_table.DataTable(compras.to_dict('records'), [{"name": i, "id": i} for i in compras.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			tabela_venda = dash_table.DataTable(vendas.to_dict('records'), [{"name": i, "id": i} for i in vendas.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)
			
			compras.rename(columns={"dates":"Date","psarbull":"Valor"},inplace=True)
			vendas.rename(columns={"dates":"Date","psarbear":"Valor"},inplace=True)

			conf = calculaConfiabilidade(compras,vendas)

			return not is_open,tabela_compra,tabela_venda,round(sum(conf)/len(conf),2)

	return is_open,[],[],[]
#-----------------------------------------------------------



#Modal Force index--------------------------------------------
@app.callback(
    Output('modal_force_index','is_open'),
    Input('config_force_index','n_clicks'),
    State('modal_force_index','is_open'),
)
def open_modal_force_index(n1,is_open):

	if 'config_force_index'==ctx.triggered_id:
		return not is_open

@app.callback(
	Output("ForceIndex_store","data"),
	Input("aplicar_force_index","n_clicks"),
	Input("dias_anteriores_force_index","value"),
)
def aplicar_force_index(n1,dias_anteriores):

	if "aplicar_force_index" == ctx.triggered_id:

		if dias_anteriores == None or dias_anteriores == "":
			dias_anteriores = 21

		return [dias_anteriores]

	return[21]


@app.callback(
    Output('modal_negociacoes_force_index','is_open'),
    Output('tabela_compras_force_index','children'),
    Output('tabela_vendas_force_index','children'),
    Output('confianca_force_index','children'),
    Input('negociacoes_force_index','n_clicks'),
    Input("select_acao_selecionada","value"),
    State('modal_negociacoes_macd','is_open'),
)
def open_negociacoes_force_index(n1,acao_selecionada,is_open):
	
	if "negociacoes_force_index" == ctx.triggered_id:

		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
				
				ticker = acao_selecionada[0]

			else:
				
				ticker = acao_selecionada


			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

			forceIndex_df = pd.read_csv("Arquivos/ForceIndex/forceIndex"+arquivo+".csv")
			fechamento_df = pd.read_csv("Arquivos/Info/fechamento.csv")

			forceIndex_df = forceIndex_df.drop(forceIndex_df.columns[[1,2,3,4,5,6,7,8,9,10,11]],axis=1)
			
			vendas = forceIndex_df.loc[forceIndex_df["ForceIndex"]>0]
			compras = forceIndex_df.loc[forceIndex_df["ForceIndex"]<0]

			vendas["Valor"] = getForceIndexValues(vendas,fechamento_df)
			compras["Valor"] = getForceIndexValues(compras,fechamento_df)
			
			vendas.drop("ForceIndex",inplace=True,axis=1)
			compras.drop("ForceIndex",inplace=True,axis=1)

			tabela_compra = dash_table.DataTable(compras.to_dict('records'), [{"name": i, "id": i} for i in compras.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			tabela_venda = dash_table.DataTable(vendas.to_dict('records'), [{"name": i, "id": i} for i in vendas.columns],
	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)

			conf = calculaConfiabilidade(compras,vendas)

			return not is_open,tabela_compra,tabela_venda,round(sum(conf)/len(conf),2)

	return is_open,[],[],[]


def getForceIndexValues(forceIndex,fechamento):

	valores_forceIndex = list()

	i = 0
	while i < len(forceIndex):

		j = 0

		while j < len(fechamento):

			if forceIndex["Date"].values[i] == fechamento["Date"].values[j]:
				valores_forceIndex.append(round(fechamento["Close"].values[j],2))

			j+=1

		i+=1

	return valores_forceIndex

#Modal aroon--------------------------------------------
@app.callback(
    Output('modal_aroon','is_open'),
    Input('config_aroon','n_clicks'),
    State('modal_aroon','is_open'),
)
def open_modal_aroon(n1,is_open):

	if 'config_aroon'==ctx.triggered_id:
		return not is_open

@app.callback(
	Output("Aroon_store","data"),
	Input("aplicar_aroon","n_clicks"),
	Input("dias_anteriores_aroon","value"),
)
def aplicar_aroon(n1,dias_anteriores):

	if "aplicar_aroon" == ctx.triggered_id:
		
		if dias_anteriores == None or dias_anteriores == "":
			dias_anteriores = 25

		return [dias_anteriores]

	return[25]



@app.callback(
    Output('modal_negociacoes_aroon','is_open'),
    Output('tabela_compras_aroon','children'),
    Output('tabela_vendas_aroon','children'),
    Output('confianca_aroon','children'),
    Output('qtd_negociacao_aroon','children'),
    Input('negociacoes_aroon','n_clicks'),
    Input("select_acao_selecionada","value"),
    State('modal_negociacoes_aroon','is_open'),
)
def open_modal_aroon(n1,acao_selecionada,is_open):

	if 'negociacoes_aroon'==ctx.triggered_id:

		if len(acao_selecionada)>0:

			if isinstance(acao_selecionada,list):
			
				ticker = acao_selecionada[0]

			else:
				
				ticker = acao_selecionada

			arquivo = str(datetime.now().month) + str(datetime.now().day) + ticker

			df_aroon = pd.read_csv("Arquivos/Aroon/aroon"+arquivo+".csv")

			fechamento_acao = pd.read_csv("Arquivos/Info/fechamento.csv")

			if isinstance(acao_selecionada,list):
				df_fechamento = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada[0]]
				
			else:
				df_fechamento = fechamento_acao.loc[fechamento_acao["ticker"] == acao_selecionada]
			

			df_aroon_down = pd.DataFrame(df_aroon.loc[df_aroon["Aroon_Down"] >= 96])
			df_aroon_up = pd.DataFrame(df_aroon.loc[df_aroon["Aroon_Up"] >= 96])


			df_aroon_down["Valor"] = getAroonValues(df_aroon_down,df_fechamento)
			df_aroon_up["Valor"] = getAroonValues(df_aroon_up,df_fechamento)


			df_aroon_down.drop(["Aroon_Down","Aroon_Up"],inplace=True,axis=1) #compra
			df_aroon_up.drop(["Aroon_Up","Aroon_Down"],inplace=True,axis=1) #venda

			df_aroon_down.rename(columns={"Aroon_Date":"Date"},inplace=True)
			df_aroon_up.rename(columns={"Aroon_Date":"Date"},inplace=True)

			tabela_venda = dash_table.DataTable(df_aroon_up.to_dict('records'), [{"name": i, "id": i} for i in df_aroon_up.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)	


			tabela_compra = dash_table.DataTable(df_aroon_down.to_dict('records'), [{"name": i, "id": i} for i in df_aroon_down.columns],

	        sort_action="native",       
	        sort_mode="single",  
	        selected_columns=[],        
	        selected_rows=[],          
	        page_action="native",      
	        page_current=0,             
	        page_size=10,)
			
			conf = calculaConfiabilidade(df_aroon_down,df_aroon_up)

		return not is_open,tabela_compra,tabela_venda,round(sum(conf)/len(conf),2),len(conf)

	return is_open,[],[],[],[]

def calculaConfiabilidade(lista_compra,lista_venda):

	lista_compra["Tipo"] = "Compra"
	lista_venda["Tipo"] = "Venda"

	df_aroon_all = pd.concat([lista_compra,lista_venda]).sort_values(by='Date')

	df_aroon_all.reset_index(inplace=True)

	df_aroon_all = normalizaAroonAll(df_aroon_all)
	
	i = 0
	compras = list()
	vendas = list()
	resultado_list = list()
	recomeca = 0
	lote = 100
	
	while i < len(df_aroon_all):



		if(df_aroon_all["Tipo"]._get_value(i) == "Compra"):

			if recomeca == 1:

				total_compras=0
				total_vendas=0
				
				for x in range(len(compras)):
					total_compras += compras[x] * lote

				divisao = math.floor((len(compras) * 100)/len(vendas))

				for x in range(len(vendas)):
					total_vendas += vendas[x] * divisao

				resultado_list.append(round((round(total_vendas - total_compras,2)*100)/total_compras,2))

				recomeca = 0
				compras = list()
				vendas = list()

				compras.append(df_aroon_all["Valor"]._get_value(i))

			else:
				compras.append(df_aroon_all["Valor"]._get_value(i))

		else:
			recomeca = 1
			vendas.append(df_aroon_all["Valor"]._get_value(i))


		i+=1
	
	return resultado_list

def normalizaAroonAll(df_aroon_all):

	#Normaliza os dados para começar nas compras
	i=0
	primeiros = 0

	while i < len(df_aroon_all):

		if(primeiros == 0):

			if df_aroon_all["Tipo"]._get_value(i) == "Venda":

				df_aroon_all.drop([i],inplace=True)

			else:
				primeiros = 1

		i+=1
	df_aroon_all.reset_index(inplace=True)

	return df_aroon_all

def getAroonValues(aroon,fechamento):

	valores_aroon = list()

	i = 0
	while i < len(aroon):

		j = 0

		while j < len(fechamento):

			if aroon["Aroon_Date"].values[i] == fechamento["Date"].values[j]:
				valores_aroon.append(round(fechamento["Close"].values[j],2))

			j+=1

		i+=1

	return valores_aroon
#-----------------------------------------------------------



#Modal candlestick----------------------------------------
@app.callback(
	Output('modal_candlestick','is_open'),
	Input('config_candlestick','n_clicks'),
	State('modal_candlestick','is_open'),
)

def open_modal_candlestick(n1,is_open):

	if 'config_candlestick' == ctx.triggered_id:
		return not is_open


@app.callback(
	Output("CandleStick_store","data"),
	Input("aplicar_candlestick","n_clicks"),
	Input("primeira_mm","value"),
	Input("segunda_mm","value"),
)

def aplicar_candlestick(n1,primeira_mm,segunda_mm):

	if 'aplicar_candlestick' == ctx.triggered_id:

		if primeira_mm == None or primeira_mm == "":
			primeira_mm = 0

		if segunda_mm == None or segunda_mm == "":
			segunda_mm == 0

		return [primeira_mm,segunda_mm]

	return [0,0]
#-----------------------------------------------------------



'''
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
'''