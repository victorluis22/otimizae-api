def addGoldenData (data, time, d, x1, fx1, x2, fx2, a, b):
  data['time'].append(time)
  data['d'].append(d)
  data['x1'].append(x1)
  data['fx1'].append(fx1)
  data['x2'].append(x2)
  data['fx2'].append(fx2)
  data['a'].append(a)
  data['b'].append(b)