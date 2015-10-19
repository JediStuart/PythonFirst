__author__ = 'sjp1'

import math

CONVERT_TO_MILLI = 1e3
CONVERT_M_TO_CM = 1e2

print('Circuit:')
I = 1 # A
print('Current:', I, 'C/s')
q = 1.602e-19 # C
print('Charge on electron:', q, 'C')
electron_per_s = I / q
print('Electrons per second: %.4g electrons/s' % electron_per_s)
P = 1 # W
print('Power:', P, 'J/s')
Energy_per_electron = P / electron_per_s
print('Energy per electron:', Energy_per_electron, 'J/electron')

# drift velocity copper
print('\nCopper:')
rho = 8.94e3 # kg/m^3
weight = 63.546e-3 # kg/mol
N_A = 6.02e23 # atoms
Fermi_v = 1.57e6 # m/s
atoms_per_vol = N_A * rho / weight
print('Atoms per m^3: %.4g /m^3' % atoms_per_vol)
radius = 5e-4 # m
print('Radius:', radius*1e3, 'mm')
area = math.pi * radius**2
print('Cross-sectional area: %.4g m^2' % area)
drift_velocity = I / (atoms_per_vol * area * q)
print('Drift velocity: %.4g m/s' % drift_velocity)
atoms_per_area = atoms_per_vol**(2/3)
print('Atoms per m^2: %.4g /m^2' % atoms_per_area)
atoms_across_wire = atoms_per_area * area
print('Atoms across cross-section of wire: %.4g atoms' % atoms_across_wire)
electrons_per_atom = 1
electron_distance_per_second = drift_velocity
print('Electron distance per second: %.4g m' % electron_distance_per_second)
linear_electron_density = electrons_per_atom * atoms_per_vol**(1/3)
print('Linear electron density: %.4g electrons/m' % linear_electron_density)
linear_electron_swept_per_second = linear_electron_density * electron_distance_per_second
print('Linear electron swept per second: %.4g electrons' % linear_electron_swept_per_second)
electron_per_s_wire = linear_electron_swept_per_second * electrons_per_atom * atoms_across_wire
print('Electrons per second: %.4g electrons' % electron_per_s_wire)

print('\nEnergy:')
m_e = 9.109e-31 # kg
print('Mass of electron:', m_e, 'kg')
c = 2.9979e8 # m/s
print('Speed of light: %.5g m/s' % c)
delta_m_e = Energy_per_electron / c**2
print('Change in mass: %.5g kg' % delta_m_e)
rel_delta_m_e = delta_m_e / m_e
print('Relative change in mass: %.5g' % rel_delta_m_e)

velocity = c * (1 - (1/(1+rel_delta_m_e))**2)**0.5
print('Velocity: %.5g m/s' % velocity)

print('\nPoynting vector:')
J_axial = I / area
print('Current density: %.3e A/m^2' % J_axial)
sigma = 1 / 16.78e-9
print('Conductivity: %.3e S/m' % sigma)

E_axial = J_axial / sigma
print('Electric field, axial: %.3f mV/m' % (CONVERT_TO_MILLI * E_axial))
S = J_axial**2 * radius / (2 * sigma) # J^2 r / 2 sigma,  maybe missing factor 2????
print('Poynting vector at surface: %.3f W/m^2' % S)

power_per_m = S * 2 * math.pi * radius # S x 2 pi r x length
print('Power, per cm: %.3f mW/cm' % (CONVERT_TO_MILLI * power_per_m / CONVERT_M_TO_CM))
length_of_wire = 0.2
power_total = power_per_m * length_of_wire
print('Power lost for %f cm of wire: %.3f mW/cm' % (CONVERT_M_TO_CM * length_of_wire, CONVERT_TO_MILLI * power_total))
length = 1
resistance_per_metre = 1 / (area * sigma) # rho length / A = rho / A
print('Resistance per metre: %.3e ohm/m' % resistance_per_metre)
power_loss_per_metre = 1**2 * resistance_per_metre # I^2 R
print('Power loss per metre: %.3e ohm/m, per cm: %.3e ohm/m' % (power_loss_per_metre, power_loss_per_metre / 100))


