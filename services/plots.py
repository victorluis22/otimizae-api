import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np

def f(function, x):
  return eval(function)

def plot2D(function, resultx, resulty, min, max, step=0.1):
  fig = Figure()
  ax = fig.subplots()
  ax.set_xlabel('x')
  ax.set_ylabel('f(x)')
  ax.set_title(f'Gráfico da função f(x) = {function}', fontsize=20)
  ax.grid(True)

  x_values = np.arange(min, max+step, step)
  y_values = [f(function, x) for x in x_values]

  ax.plot(x_values, y_values, label=f'f(x) = {function}')
  ax.scatter(resultx, resulty, c='red', label=f'Mínimo ({round(resultx, 3)}, {round(resulty, 3)})')
  ax.legend()

  buf = BytesIO()
  fig.savefig(buf, format="png")
  data = base64.b64encode(buf.getbuffer()).decode("ascii")

  fig.savefig("result.png")

  return data
  