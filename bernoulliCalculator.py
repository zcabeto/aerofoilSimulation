# Bernoulli's Principle Calculator

coefLift = 1
density = 1.204                     # kg/m3 of air
velocity = input("Enter velocity: ")# m/s of aerofoil
area = 1                            # m2 of aerofoil top

lift = coefLift * (0.5*density*velocity) * area
print(lift)
