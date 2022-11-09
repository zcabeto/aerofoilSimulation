
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

lr = 2e-3

df = pd.read_csv("aerofoilData.csv")
T = df["Max Thickness"].to_numpy().reshape(-1,1)
tC = df["T Chord"].to_numpy().reshape(-1,1)
P = df["Max Camber"].to_numpy().reshape(-1,1)
pC = df["P Chord"].to_numpy().reshape(-1,1)
A = df["AngleDeg"].to_numpy().reshape(-1,1)
CL = df["CL"].to_numpy().reshape(-1,1)
variables = [T,tC,P,pC,A]

scaler = StandardScaler()
T_ = scaler.fit_transform(T)
tC_ = scaler.fit_transform(tC)
P_ = scaler.fit_transform(P)
pC_ = scaler.fit_transform(pC)
A_ = scaler.fit_transform(A)
scalVars = [T_,tC_,P_,pC_,A_]

def gradDescent(variables, y, lr, iterations=2000):
    thetas = [np.zeros((1,1))]
    for i in range(len(variables)):
        thetas.append(np.zeros((1,1)))

    for i in range(iterations):
        toSumMSE = thetas[0] - y
        for j in range(len(variables)):
            toSumMSE += variables[j].dot(thetas[j+1])

        deltaTheta = (2/len(toSumMSE)) * np.sum(toSumMSE)
        thetas[0] -= lr * deltaTheta
        for i in range(len(variables)):
            deltaTheta = (2/len(toSumMSE)) * variables[i].T.dot(toSumMSE)
            thetas[i] -= lr * deltaTheta

    return thetas

thetas = gradDescent(scalVars,CL,lr)
print(thetas)
            

            
