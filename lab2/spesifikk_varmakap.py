import numpy as np
import matplotlib.pyplot as plt

C_0 = 5780.8
C_v = 4200 #J/(kg K)
m = 198.98e-3

# Temperaturer i kelvin
T2 = 15.76
T1 = 30.00
T0 = 0.00

L_S = C_0*(T1 - T2)/m - C_v*(T2 - T0)

print("L_S = {} J/kg".format(L_S))

k = 1.3806488e-23
N_A = 6.022e23
m = -5120
R = k*N_A
L_f = -m*R
print(R*7.1*1e-3)

print("L_f = {}".format(L_f))
