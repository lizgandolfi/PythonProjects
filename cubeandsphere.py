'''
Ask the user to enter values for a radius. 
Now show the area of the circle and the volume of the sphere that the input radius would create. 
What is the volume of the smallest cube given the sphere can be inscribed within? 
'''

import math
radius = int(input('Enter radius ===>'))

circlearea = (math.pi) * (radius ** 2)
spherevol = ((4/3)* ((math.pi) * (radius ** 3)))

sidecube = (radius * 2)
volumecube = (sidecube ** 3)

print('\nArea of Circle:', circlearea)
print('Volume of Sphere:', spherevol)
print('Smallest Inscribed Cube:', volumecube)



