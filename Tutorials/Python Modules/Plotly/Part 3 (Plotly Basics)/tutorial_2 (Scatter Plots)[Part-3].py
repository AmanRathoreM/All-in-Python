# Date 03-07-2021
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go



x_random = np.random.uniform(1, 100000, 100000)
y_random = np.random.uniform(1, 100000, 100000)

data = [go.Scatter(x=x_random, y=y_random, mode='markers')]

pyo.plot(data, filename="tutorial_2 (Scatter Plots)[Part-3].html")
