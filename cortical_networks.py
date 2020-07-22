import numpy as np


def make_linear_data(n, c=0, a=1, b=.1, xlow=0, xhigh=10):
    x = np.linspace(xlow, xhigh, n)
    eta = np.random.normal(loc=0, scale=1, size=n)
    y = c + a*x + b*eta
    return x, y

def make_sin_data(n, c=0, a=1, f=.1, b=.1, xlow=0, xhigh=10):
    x = np.linspace(xlow, xhigh, n)
    eta = np.random.normal(loc=0, scale=1, size=n)
    y = c + a*np.sin(2*np.pi*f*x) + b*eta
    return x, y

def make_dampedsin_data(n, c=0, a=1, f=.1, b=.1, xlow=0, xhigh=10):
    x = np.linspace(xlow, xhigh, n)
    eta = np.random.normal(loc=0, scale=1, size=n)
    y = c + a * np.exp(-x) * np.sin(2*np.pi*f*x) + b * eta
    return x, y

def make_syn_data(n, model='linear', params=[0, 1, .1], xlow=0, xhigh=10):
    if model == 'linear':
        c, a, b = params
        x, y = make_linear_data(n, c, a, b, xlow, xhigh)
    elif model == 'sine':
        c, a, f, b = params
        x, y = make_sin_data(n, c, a, f, b, xlow, xhigh)
    elif model == 'damped sine':
        c, a, f, b = params
        x, y = make_dampedsin_data(n, c, a, f, b, xlow, xhigh)
    else:
        raise ValueError("model has to be 'linear', 'sine' or 'damped sine'")
            
    return x, y