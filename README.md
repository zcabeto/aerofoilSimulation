# aerofoilSimulation
simulates the operation of different aerofoil moving through fluids

initial Bernoulli Calculator created through a multitude of research into generalised equations to calculate the coefficient of lift based upon an aerofoil's max camber, aspect ratio, and angle of attack. This, however, makes assumptions such as low thickness and constant viscosity; it also does not take position of max thickness or camber into account ie. overall shape not fully taken account of.
These equations only find the low magnitude attack angle coefficients as it does not account for the drop in coefficient at the stall point. As such the equations yield linear results.

AI practice is undergone in order to progress to using Machine Learning to more accurately determine how the coefficient of lift depends on a larger set of important facors. 
Once I have caught up with learning the skills of linear regression, I want to utilise experimental data from NACS aerofoils including max camber, max thickness, and chord points to determine how CL changes with angle of attack (pre-stall). Then I want to execute the same with those factors to find the stall angle and coefficient of lift at that angle.
