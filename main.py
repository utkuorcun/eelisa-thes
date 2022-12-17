import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# names are Times Higher Education Classificaitons
size=[5276, 1306, 12516, 7526, 27838, 3207, 1474, 7190, 8346]
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig = go.Figure(data=[go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[5276, 1306, 12516, 7526, 27838, 3207, 1474, 7190, 8346],
    mode='markers',
    name='Physical Sciences',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 1))])


size = [5705, 1654, 11028, 7414, 9633, 784, 1840, 8238, 8498]
fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[5705, 1654, 11028, 7414, 9633, 784, 1840, 8238, 8498],
    mode='markers',
    name='Engineering and Technology',
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 2)))


size= [2567, 1113, 4677, 3170, 4455,284,1426,3931,4980]
fig.add_trace(go.Scatter(
    x=['BME', 'ENPC', 'FAU', 'ITU', 'PSL', 'SNS', 'SSSA', 'UPB', 'UPM'],
    y=[2567, 1113, 4677, 3170, 4455,284,1426,3931,4980],
    mode='markers',
    name="Computer Science",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 3)))


size = [695, 400, 5806, 1138, 13230, 348, 979, 883,3323]
fig.add_trace(go.Scatter(
    x=['BME', 'ENPC', 'FAU', 'ITU', 'PSL', 'SNS', 'SSSA', 'UPB', 'UPM'],
    y=[695, 400, 5806, 1138, 13230, 348, 979, 883,3323],
    mode='markers',
    name="Life Sciences",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 4)))


size = [632, 750, 1070, 1001, 2919, 471, 482, 313, 1593]
fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[632, 750, 1070, 1001, 2919, 471, 482, 313, 1593],
    mode='markers',
    name="Social Sciences",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 5)))

size = [739, 233, 11795,678 ,9646, 254, 1556, 725, 1903]

fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[739, 233, 11795,678 ,9646, 254, 1556, 725, 1903],
    mode='markers',
    name="Clinical, Pre-Clinical and Health",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 6)))

size = [ 345,    161, 734 , 617,  3541, 494, 120,   101,  664]
fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[ 345,    161, 734 , 617,  3541, 494, 120,   101,  664],
    mode='markers',
    name="Arts and Humanities",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 7)))


size = [333, 934, 912, 583, 2005, 108, 541, 237, 537]
fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[333, 934, 912, 583, 2005, 108, 541, 237, 537],
    mode='markers',
    name="Business and Economics",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 8)))

size = [104, 23, 239, 106, 211, 16, 26, 389,330]

fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[104, 23, 239, 106, 211, 16, 26, 389,330],
    mode='markers',
    name="Education",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 9)))


size = [17, 11, 130, 179, 12, 165, 12, 6, 52]
fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[17, 11, 130, 179, 12, 165, 12, 6, 52],
    mode='markers',
    name="Law",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color ='#325A9B')))

size = [159, 58, 559, 31, 1010, 21, 71, 17, 242]

fig.add_trace(go.Scatter(
    x=['BME','ENPC','FAU','ITU','PSL','SNS','SSSA','UPB','UPM'],
    y=[159, 58, 559, 31, 1010, 21, 71, 17, 242],
    mode='markers',
    name="Psychology",
    marker=dict(
        size=size,
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color = 10)))


app = dash.Dash()
app.layout = html.Div([
    html.H1("EELISA Partner Universities Research Output"),
    html.P("2017-2022"),
    dcc.Graph(figure=fig)
], style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'middle','text-align': 'center','height': '100%'})

app.run_server(debug=True, use_reloader=False)