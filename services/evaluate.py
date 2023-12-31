import math

ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}

def f(expression, x):
    """Evaluates a math expression."""
    # Compile the expression
    code = compile(expression, "<string>", "eval")

    # Validate allowed names
    for name in code.co_names:
        if name not in ALLOWED_NAMES and name != 'x':
            raise NameError(f"O uso de '{name}' não é reconhecido")

    return eval(code, {"__builtins__": {}, "x": x}, ALLOWED_NAMES)

def deriv_f(function, x, h=0.000001):
  """Evaluates the first order derivative of a math expression."""
  return (f(function, x + h) - f(function, x - h))/(2*h)


def deriv2_f(function, x, h=0.000001):
  """Evaluates the second order derivative of a math expression."""
  return (f(function, x-h) + f(function, x+h) - 2*f(function, x))/(h**2)