# Date 03-07-2021
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# np.random.seed(42)

x_random = np.random.randint(1, 101, 1000)
y_random = np.random.randint(1, 101, 1000)

data = [go.Scatter(x=x_random, y=y_random, mode='markers')]

pyo.plot(data, filename="tutorial_2 (Scatter Plots)[Part-2].html")
