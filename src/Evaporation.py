__author__ = 'sjp1'

import math

hbar = 1.055e-34 # m^2 kg / s
G = 6.674e-11 # N m^2 / kg^2
c = 2.9979e8 # m/s

M_s = 1.989e30 # kg
r_s = 2 * G * M_s / c**2
r_s = 0.3 # m

t_ev = ( 640 * math.pi * r_s**3 * c**2) / (hbar * G)
M = r_s * c**2 / (2 * G)
M_solar = M / M_s

K_ev = 3.562e32 # W / kg
P = K_ev / M**2

print('Radius %g m, mass %.2e kg (%.2e solar) : evaporation time %.2e s, power %.2e W.' % (r_s, M, M_solar, t_ev, P))


