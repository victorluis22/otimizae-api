from services.evaluate import f
from services.evaluate import deriv_f
from services.tables import addBissectionData

def bissectionSearch(data, function, start, end, limit=0.00001):
  time = 0
  a, b = start, end
  next_a, next_b = 0, 0
  timeout = 100

  while time < timeout:
    lmbda_k = (a + b)/2

    addBissectionData(data, time, lmbda_k, f(function, lmbda_k), a, b)
    
    if deriv_f(function, lmbda_k, limit) == 0:
      return [lmbda_k, f(function, lmbda_k), time]
    elif deriv_f(function, lmbda_k, limit) > 0:
      next_a = a
      next_b = lmbda_k
    else:
      next_a = lmbda_k
      next_b = b

    if (1/2)**time <= limit/(end-start):
      return [lmbda_k, f(function, lmbda_k), time]
    else:
      a = next_a
      b = next_b
      
    time += 1
  
  raise TimeoutError(f"Algum erro aconteceu, programa demorou muito para responder.")
