"""Stata Gtools Bechmarking Figures."""

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'

df = pd.read_csv('./test/bench.csv')
df.at[0, 'command'] = 'collapse<br><sup>(sum, mean)</sup>'
df.at[1, 'command'] = 'collapse<br><sup>(sd, median)</sup>'
df.at[2, 'command'] = 'reshape long'
df.at[3, 'command'] = 'reshape wide'

fig = go.Figure()
fig.add_trace(go.Bar(x=df['dnative'], y=df['command'], name='Stata', orientation='h'))
fig.add_trace(go.Bar(x=df['dgtools'], y=df['command'], name='Gtools', orientation='h'))

fig.update_layout(
    title={
        'text': 'Stata vs Gtools<br><sup>Time (seconds) with 10M obs and 1,000 groups</sup>',
        'x': 0.5,
    },
    yaxis={'categoryorder': 'array', 'categoryarray': df['command'].to_list()[::-1]},
    template='plotly_dark',
    legend=dict(yanchor='top', y=0.99, xanchor='right', x=0.95),
    margin=dict(t=40, r=40, b=40, l=40, pad=4),
    width=600,
    height=600,
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
)

fig.show()

pio.write_image(fig, './test/bench_dark.svg', format='svg')

fig.update_layout(
    title={
        'text': 'Stata vs Gtools<br><sup>Time (seconds) with 10M obs and 1,000 groups</sup>',
        'x': 0.5,
    },
    yaxis={'categoryorder': 'array', 'categoryarray': df['command'].to_list()[::-1]},
    template='plotly_white',
    legend=dict(yanchor='top', y=0.99, xanchor='right', x=0.95),
    margin=dict(t=40, r=40, b=40, l=40, pad=4),
    width=600,
    height=600,
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
)

fig.show()
pio.write_image(fig, './test/bench_light.svg', format='svg')
