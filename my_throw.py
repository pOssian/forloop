'''
Make another program called my_throw.py which takes input by the user: 
Angle (in degrees), 
Velocity (in km/h)
Throw height (in meter).

Calculate and print the following information:
i. The throw angle using radians
α = math.radians(θ)
where θ is the throw angle in degrees.
'''

from cmath import cos
import math


angle = 90 #float(input('Add throwing angle in degrees: '))
velocity = 50 #float(input('Add the velocity in km/h: '))
throw_height = 2 #float(input('Add how high you are throwing, in meter: '))
rad_angles = math.radians(angle)

print(round(rad_angles, 2))


# ii. The throw velocity in meter/second
throw_v = (velocity/3.6)

# iii. The throw velocity in the horizontal direction (in m/s), given by
horizontal_v = ((velocity/3.6) * math.cos(rad_angles))

# iv. The throw velocity in the vertical direction, given by
vertical_v = ((velocity/3.6) * math.sin(rad_angles))
print(round(vertical_v, 2))

g = 9.81

# The ball airtime, given by:
air_time = ((vertical_v + (math.sqrt(vertical_v**2 + 2 * g * throw_height)))/g)
print(round(air_time, 2))


# vi. The throw distance, given by:
throw_dist = (horizontal_v * air_time)
print(throw_dist)

'''
It’s a common knowledge that throwing a ball at 45degrees angle
gives the longest throw. But is that also true when you are standing up (h0>0)? 
Try h0=2, is the longest throw also at 45degrees, a little bit less or a little bit more?
'''









