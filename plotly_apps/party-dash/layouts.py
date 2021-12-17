import pandas as pd
from app import app
from dash import dcc
from dash import html
import plotly.express as px

choice = 'party'
df = pd.read_csv(choice + '_gender_gap.csv')
all_domains = df[choice].unique()

start, end = 2015, 2020
bgc = '#323650'

total_num = df.groupby(['date', choice]).agg({'Occurrences':'sum'}).reset_index()
female_df = df[df.gender=='female']
female_df['percent'] = 0
for i in range(len(female_df)):
    female_df.iloc[i, -1] = female_df.iloc[i,2]/total_num[(total_num['date']==female_df.iloc[i,1]) & (total_num[choice]==female_df.iloc[i,-2])]['Occurrences']

female_df['percent'] *= 100
female_df = female_df.round({'percent': 2})
line_fig = px.line(female_df,
    x="date", y="percent", color=choice,
    color_discrete_sequence=['#3366cc', '#72b7b2', '#990099', '#ff7f00', '#b3e2cd', '#af6458', '#cf1c90'])
line_fig.update_layout(
    title='Percentage of Women Quoted in different ' + choice,
    legend=dict(
        yanchor="top",
        xanchor="left",
        bgcolor='rgba(0,0,0,0)'
    ),
    font_color='white',
    font_family="Lora",
    paper_bgcolor=bgc,
)
line_fig.update_xaxes(title="Date", rangeslider_visible=True)
line_fig.update_yaxes(title="Percentage of occurrence")
app.layout = html.Div(children=[
    html.Div([
        html.Div([
            dcc.Graph(id='bar-chart'),
        ], 
        className='seven columns',
        ),
        html.Div([
            dcc.Graph(id='pie-chart'),
        ], 
        className='five columns',
        style={'margin-top': '20px'}),
        html.Div([
            dcc.RangeSlider(
                id='slider',
                min=start,
                max=end,
                marks={x: {'label': str(x), 'style': {'color': '#77b0b1'}} for x in range(start, end+1)},
                step=1,
                value=[start, end],
                tooltip={'placement': 'bottom'},
            )
        ],
        className='nine columns',
        style={'cursor': 'pointer', 'margin': '-20px 0px 50px 150px'}),
    ], 
    className='row',
    style={'background': bgc}
    ),
    html.Div(
        dcc.Loading(
            id='load-line',
            children=[
                html.Div(
                    dcc.Graph(id='line-chart', figure=line_fig),
                    className='chart', 
                    style={'background': bgc, 'margin': 'auto'}
                ),
            ],
        ),
    ),
])
