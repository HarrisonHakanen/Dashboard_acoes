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

	dbc.Row([
		dbc.Col([

			html.Legend("Ações", className="card-title"),
            html.Div(
                dcc.Dropdown(
                id="dropdown-acoes",
                clearable=False,
                style={"width": "100%"},
                persistence=True,
                persistence_type="session",
                multi=True)                       
            ),


		]),


	],style={"padding": "25px"}),

	dbc.Row([

		dbc.Col([
			dbc.Button("Carregar ações", color="error", id="carregar_acoes", value="acoes", className="btn btn-success"),

		]),
	],style={"padding": "25px"}),

	html.Hr(),

	dbc.Row([

		dbc.Col([
			dbc.Nav(
	        [
	            dbc.NavLink("Negociações", href="/dashboards", active="exact"),
	            dbc.NavLink("Altas baixas", href="/altas_baixas", active="exact"),
	            dbc.NavLink("Previsões", href="/previsoes", active="exact"),
	        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}),
			html.H5(id="testeH4"),
		]),

	],style={"padding": "25px"}),

	dbc.Row([
		dbc.Col([

			dbc.Checklist(
                options=[],
                value=[1],
                id="check_acoes",
                switch=True),

		]),

	])


])




@app.callback(
	[Output("dropdown-acoes", "options"),
	Input("tickers","data")]
)

def popula_dropdown(data):

	df = pd.DataFrame(data)
	
	val = df.Acoes.unique().tolist()

	return [([{"label": x, "value": x} for x in df.Acoes.unique()])]


@app.callback(Output("testeH4","children"),
	Output("check_acoes","options"),
	
	[Input("carregar_acoes","n_clicks"),
	Input("dropdown-acoes","value"),
	

	])

def carregar_acoes(n,drop_data):
	
	if(n):
		
		data = drop_data
		
		return [data,data]

	return []