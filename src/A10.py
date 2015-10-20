__author__ = 'sjp1'

METRES_IN_A_MILE = 1609
SECONDS_IN_AN_HOUR = 3600
CONVERT_TO_KILO = 1e-3
CONVERT_TO_MEGA = 1e-6

mass = 13782 # kg
print('Mass: %i kg' % mass)
speed_in_mph = 350 # mph
print('Speed: %i mph' % speed_in_mph)
speed = speed_in_mph * METRES_IN_A_MILE / SECONDS_IN_AN_HOUR
print('Velocity: %.1f m/s' % speed)
energy = 0.5 * mass * speed**2
print('Energy: %.2f MJ' % (CONVERT_TO_MEGA*energy))
momentum = mass * speed
print('Momentum: %.2f MN s' % (CONVERT_TO_MEGA*momentum))

bullet_velocity = 1070 # m/s
print('Muzzle velocity: %i m/s' % bullet_velocity)
bullet_mass = 0.395 # kg
print('Projectile mass: %.3f kg' % (bullet_mass))
rate_of_fire = 3900 / 60 # rps
print('Rate of fire: %.2f rounds/s' % rate_of_fire)
time_of_fire = 2 # s
print('Time of fire: %i s' % time_of_fire)
momentum_per_bullet = bullet_mass * bullet_velocity
print('Momentum per projectile: %.2f N s' % (momentum_per_bullet))
momentum_per_burst = momentum_per_bullet * rate_of_fire * time_of_fire
print('Momentum per burst: %.2f kN s' % (CONVERT_TO_KILO*momentum_per_burst))
velocity_change = momentum_per_burst / mass
print('Change in velocity: %.2f m/s' % (velocity_change))
print('Change in velocity: %.2f mph' % (velocity_change*SECONDS_IN_AN_HOUR/METRES_IN_A_MILE))

