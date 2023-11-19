def addGoldenData (data, time, d, x1, fx1, x2, fx2, a, b):
  """Add data of each iteration to a dictionary that will be used to generate a table"""
  data['time'].append(time)
  data['d'].append(d)
  data['x1'].append(x1)
  data['fx1'].append(fx1)
  data['x2'].append(x2)
  data['fx2'].append(fx2)
  data['a'].append(a)
  data['b'].append(b)

def addBissectionData (data, time, lmbda, flmbda, a, b):
  """Add data of each iteration to a dictionary that will be used to generate a table"""
  data['time'].append(time)
  data['lmbda'].append(lmbda)
  data['flmbda'].append(flmbda)
  data['a'].append(a)
  data['b'].append(b)

def addNewtonData (data, time, lmbda, firstderiv, secondderiv, lmbda_next):
  """Add data of each iteration to a dictionary that will be used to generate a table"""
  data['time'].append(time)
  data['lmbda'].append(lmbda)
  data['firstderiv'].append(firstderiv)
  data['secondderiv'].append(secondderiv)
  data['lmbdanext'].append(lmbda_next)