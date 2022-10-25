# Bernoulli's Principle Calculator

import math

density = 1.204
area = float(input("Enter area: "))
AR = float(input("Enter Aspect Ratio of wing: "))
camber = float(input("Enter camber percentage: "))
weight = float(input("Enter Plane Weight: "))

print("Plane has taken off...")
velocity = float(input("Enter velocity: "))
angle = float(input("Enter angle of attack (degrees): "))

a = angle * math.pi/180         # convert to radians
p = camber/100
CLA = (2*math.pi)/(1 + (2/AR))  # coefficients...
CLZ = math.pi * (4*p - 2 + math.sqrt(16 * (p**2) + 4))
CL = (a * CLA) + CLZ

dynamicPressure = 0.5*density*(velocity**2)
lift = round(CL * dynamicPressure * area)

print(("The plane has " + str(lift) + "N of lift. This gives "
       + str(round(lift-weight)) + "N of upward force.").strip())

