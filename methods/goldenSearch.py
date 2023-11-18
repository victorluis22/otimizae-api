from services.evaluate import f
from services.tables import addGoldenData

def goldenSectionSearch(data, function, start, end, limit=0.00001):
  goldenRatio = (5**(1/2) - 1) / (2)
  time = 0
  a, b = start, end

  while time < 100:
    d = goldenRatio * (b - a)
    x1 = a + d
    x2 = b - d
    fx1 = f(function, x1)
    fx2 = f(function, x2)

    addGoldenData(data, time, d, x1, fx1, x2, fx2, a, b)

    if abs(x2 - x1) < limit:
      return [x1, fx1, time]

    if fx1 > fx2:
      b = x1
    elif fx2 > fx1:
      a = x2

    time += 1