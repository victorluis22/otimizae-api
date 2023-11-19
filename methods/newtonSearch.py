from services.evaluate import f
from services.evaluate import deriv_f, deriv2_f
from services.tables import addNewtonData

def newtonSearch(data, function, x, limit=0.00001):
  lmbda = x
  lmbda_next = 0
  time = 0
  timeout = 100

  while time < timeout:
    firstDeriv = deriv_f(function, lmbda, limit)
    secondDeriv = deriv2_f(function, lmbda, limit)
    lmbda_next = lmbda - (firstDeriv / secondDeriv)

    addNewtonData(data, time, lmbda, firstDeriv, secondDeriv, lmbda_next)

    if abs(lmbda_next - lmbda) < limit:
      return [lmbda_next, f(function, lmbda_next), time]
    else:
      lmbda = lmbda_next

    time += 1

  raise TimeoutError(f"Algum erro aconteceu, programa demorou muito para responder.")
