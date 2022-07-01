import numpy as np


velocities = np.array([30, 40, 50])
angles = np.array([40, 45, 50])
height = 2
g = 9.81

angle_radians = np.radians(angles)
v_mps = velocities/3.6
v_mps_h = v_mps*np.cos(angle_radians)
v_mps_v = v_mps*np.sin(angle_radians)

airtime = (v_mps_v+np.sqrt(v_mps_v**2+2*g*height))/g
throw_distance = v_mps_h*airtime
