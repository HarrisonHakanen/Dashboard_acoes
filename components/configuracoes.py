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

	html.Legend("Configurações")

])