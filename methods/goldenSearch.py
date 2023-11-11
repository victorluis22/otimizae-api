def f(function, x):
  return eval(function)

def goldenSectionSearch(function, start, end, limit=0.00001):
  goldenRatio = (5**(1/2) - 1) / (2)
  time = 0
  a, b = start, end

  while time < 100:
    d = goldenRatio * (b - a)
    x1 = a + d
    x2 = b - d
    fx1 = f(function, x1)
    fx2 = f(function, x2)

    if abs(x2 - x1) < limit:
      return [x1, fx1, time]

    if fx1 > fx2:
      b = x1
    elif fx2 > fx1:
      a = x2

    time += 1


if __name__ == '__main__':
    function = "x**2 - 6*x + 15"
    a = -10
    b = 10

    minimun = goldenSectionSearch(function, a, b)

    print(f'Mínimo encontrado entre [{a}, {b}] = {minimun}\n')