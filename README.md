# aerofoilSimulation
simulates the operation of different aerofoil moving through fluids

            Bernoulli Calculator
initial Bernoulli Calculator created through a multitude of research into generalised equations to calculate the coefficient of lift based upon an aerofoil's max camber, aspect ratio, and angle of attack. This, however, makes assumptions such as low thickness and constant viscosity; it also does not take position of max thickness or camber into account ie. overall shape not fully taken account of.
These equations only find the low magnitude attack angle coefficients as it does not account for the drop in coefficient at the stall point. As such the equations yield linear results.


            CL gradient descent - now utilising poetry
I have written a short piece of code to accept experimental data from NACA aerofoils as max thickness & chord, max camber & chord, and angle. The code then computes gradient descent on the coefficients of each variable over a certain specified number of iterations. The coefficients attached to their relevant variables, with a bias coefficient, collectively derive an equation for the coefficient of lift (pre-stall). Simply for testing purposes, only a few aerofoil's data have been used, but the excel spreadsheet of the values will continue to be expanded. Next task is to do the same testing to derive the stall point based upon the same set of data.

This project is on hold while I learn and understand ML processes better.
