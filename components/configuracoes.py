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

	html.Legend("Configurações"),

	dbc.Row([
		html.H5("Bollinger"),
		dbc.Col([
			
			html.H5("Período de análise"),

			dcc.DatePickerRange(
				id="periodo_analise",
				start_date_placeholder_text="Data inicial",
				end_date_placeholder_text="Data final",   
				calendar_orientation='vertical')
		]),

		dbc.Col([
			html.H5("Dias anteriores (padrão 10)"),
			dcc.Input(id="dias_anteriores", type="number",className="form-control form-control-lg"),
		]),

		dbc.Col([
			html.H5("Quantidade de desvio padrão superior (padrão 1.5)"),
			dcc.Input(id="mm_superior", type="number",className="form-control form-control-lg"),
		]),
		dbc.Col([
			html.H5("Quantidade de desvio padrão inferior (padrão 1.5)"),
			dcc.Input(id="mm_inferior", type="number",className="form-control form-control-lg"),
		]),
	],style={"padding": "25px"}),

	html.Hr(),

	dbc.Row([

		html.H5("MACD"),

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

	html.Hr(),

	dbc.Row([

		html.H5("RSI"),

		dbc.Col([
			
			html.H5("Período de análise"),

			dcc.DatePickerRange(
				id="periodo_analise_rsi",
				start_date_placeholder_text="Data inicial",
				end_date_placeholder_text="Data final",   
				calendar_orientation='vertical')
		]),

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
	],style={"padding": "25px"}),

	
	html.Hr(),

	dbc.Row([

		html.H5("Candlestick"),

		dbc.Col([
			
			html.H5("Período de análise"),

			dcc.DatePickerRange(
				id="periodo_analise_candlestick",
				start_date_placeholder_text="Data inicial",
				end_date_placeholder_text="Data final",   
				calendar_orientation='vertical')
		]),
	],style={"padding": "25px"}),


	html.Hr(),


	dbc.Row([

		dbc.Col([
			dbc.Button("Aplicar", color="error", id="aplicar", value="acoes", className="btn btn-success"),
		],width=2),
		dbc.Col([
			dbc.Button("Restaurar padrões", color="error", id="restaurar", value="acoes", className="btn btn-success"),
		],width=2),
	],style={"padding": "25px"}),

])