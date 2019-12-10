import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(n,t):
    L=1.5
    dndt=-L*n
    return dndt
#initial condition
n0=10

t=np.linspace(0,10)
n=odeint(model,n0,t)
plt.plot(t,n)
plt.xlabel('sec')
plt.ylabel('cm^-3')
plt.show()
