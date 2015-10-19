__author__ = 'sjp1'

import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('D:\Research\Gravity\Python')

G = 6.674e-11
M = 5.972e24
# M is kg, G is Nm^2/kg^2, so k is Nm^2/kg = kgm/s^2 m^2/kg = m^3/s^2
k = G * M

# radius l^2/k, so l^2/k = m, l^2 = mk = m m^3/s^2 = m^4/s^2, so l = m^2/s - angular momentum for unit mass
# radius earth
l = 6.371e6
# orbit moon
l = 3.844e8
v = lambda r: abs((l**2/(2*r**2)) - (k / r))

r = np.linspace(0.04, 2, 1000)
r = np.linspace(1e6, 1e8, 1000)
r = np.logspace(1, 10, 1000)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
line, = ax.plot(r, v(r), '-')
line.set_label('Potential')
ax.legend(prop={'size':11})
ax.set_xscale('log')
ax.set_yscale('log')
plt.grid()
plt.title('Gravitational Potential', fontsize=14)
plt.xlabel('Radius, m', fontsize=12)
plt.ylabel('Potential, J/kg', fontsize=12)
plt.show()
fig.savefig('potential.png')

# from pylab import *
# a = [ pow(10,i) for i in range(10) ]
# fig = pyplot.figure()
# ax = fig.add_subplot(2,1,1)
#
# line, = ax.plot(a, color='blue', lw=2)
#
# ax.set_yscale('log')
#
# show()