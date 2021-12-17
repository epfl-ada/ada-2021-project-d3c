import pandas as pd
from app import app
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

import layouts

bgc = '#323650'
data_folder = './data'

choice = 'domain'
df = pd.read_csv(data_folder + '/' + choice + '_gender_gap.csv')


@app.callback(
    Output("bar-chart", "figure"),
    Input("slider", "value"),
)
def update_bar(slider):
    choice = 'domain'
    start, end = str(slider[0])+'-01', str(slider[1])+'-12'
    t = 'news outlet'
    mask = (df['date'] >= start) & (df['date'] <= end)
    occur = df.loc[mask].groupby([choice, 'gender']).agg({'Occurrences':'sum'})
    ## Number of occurrences and percentage of occurrences
    percent = occur.groupby(level=0).apply(lambda x: 100*x/x.sum()).reset_index()
    occur = occur.reset_index()
    percent = percent.rename(columns={'Occurrences': 'percentage'})
    percent = percent.round({'percentage': 2})

    reidx = {}
    reidx[choice] = ['Fox News', 'CNN', 'NYTimes', 'NBC News', 'TIME', 'CNBC', 'BBC']

    sctx = list(reidx[choice])
    occur_male = occur[occur.gender=='male'].set_index(choice)
    occur_female = occur[occur.gender=='female'].set_index(choice)
    percent_male = percent[percent.gender == 'male'].set_index(choice)
    percent_female = percent[percent.gender == 'female'].set_index(choice)

    occur_male = occur_male.reindex(reidx[choice])
    occur_female = occur_female.reindex(reidx[choice])
    percent_male = percent_male.reindex(reidx[choice])
    percent_female = percent_female.reindex(reidx[choice])

    scty_num_male = list(occur_male.Occurrences)
    scty_num_female = list(occur_female.Occurrences)
    scty_perct_male = list(percent_male.percentage)
    scty_perct_female = list(percent_female.percentage)

    fig = go.Figure(data=[
        go.Bar(
            x=scty_num_male,
            y=sctx,
            customdata=[str(p)+'%' for p in scty_perct_male],
            hovertemplate = '<b>%{label}:</b><br>sources: %{x}(%{customdata})</br>',
            orientation='h',
            name='male',
            marker={'color':"#1F77B4"}
        ),
        go.Bar(
            x=scty_num_female,
            y=sctx,
            customdata=[str(p)+'%' for p in scty_perct_female],
            hovertemplate = "<b>%{label}:</b><br>sources: %{x}(%{customdata})</br>",
            orientation='h',
            name='female',
            marker={'color': "#ffa02d"}
        )
    ])
    fig.update_layout(
        title='Number of male and female sources by ' + t,
        font_family="Lora",
        font_color="white",
        title_font_color="white",
        # legend_font_color="black",
        # legend_title_font_color="black",
        # title_font_family="Times New Roman",
        xaxis=dict(
            title='Occurrences',
            titlefont_size=16,
            tickfont_size=14,
        ),
        yaxis=dict(
            title=t.capitalize(),
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1,
            xanchor="right",
            x=1,
            bgcolor='rgba(0,0,0,0)',
            font_color=bgc
        ),
        barmode='group',
        bargap=0.2, # gap between bars of adjacent location coordinates.
        bargroupgap=0.15, # gap between bars of the same location coordinate.
        paper_bgcolor=bgc,
    )
    fig.update_traces(marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
    return fig


@app.callback(
    Output("pie-chart", "figure"),
    Input("slider", "value"),
)
def update_pie(slider):
    start, end = str(slider[0])+'-01', str(slider[1])+'-12'
    mask = (df['date'] >= start) & (df['date'] <= end)
    fig = px.pie(df.loc[mask], values='Occurrences', names='gender',
                color_discrete_sequence=px.colors.qualitative.T10)
    fig.update_layout(
        title='Aggregate ratio between genders',
        legend=dict(
            yanchor="bottom",
            y=0.85,
            xanchor="right",
            x=1.18
        ),
        font_color='white',
        font_family="Lora",
        paper_bgcolor=bgc,
    )
    fig.update_traces(textfont_size=20, marker=dict(colors=["#cedef0", "#9d9ad9"], line=dict(color='#000000', width=2)), opacity=0.9)
    return fig