import plotly as py
import plotly
import plotly.plotly as hi
import plotly.graph_objs as go
import numpy as np

py.tools.set_credentials_file(username='tjb9197', api_key='GGNUtgx2gnb3auQbjrM7')

N = 500
random_x = np.linspace(0, 6, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y
)

data = [trace]

hi.iplot(data, filename='basic-line')
