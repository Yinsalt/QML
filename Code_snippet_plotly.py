import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


pio.renderers.default = "browser"
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = go.Figure(go.Surface(x=X, y=Y, z=Z))
fig.update_layout(title="Paraboloid", autosize=False, width=600, height=600)

#interactive
fig.show()
