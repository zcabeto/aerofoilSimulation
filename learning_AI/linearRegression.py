
##import numpy as np
##import pandas as pd
##import matplotlib.pyplot as plt
##from sklearn.preprocessing import StandardScaler

df = pd.read_csv("advertising.csv")
X = df['TV'].to_numpy().reshape(-1, 1)
y = df['Sales'].to_numpy().reshape(-1, 1)

plt.scatter(X, y, c='b')
plt.ylabel("Sales")
plt.xlabel("TV Advertisement Budget")

def gradDescent(X,y,lr,records,iterations=2000):
    theta0 = np.zeros((1,1))
    theta1 = np.zeros((1,1))
    thetaSet = []

    for i in range(iterations):
        toSumMSE = (theta0 + X.dot(theta1)) - y
        change_theta0 = (2/len(toSumMSE)) * np.sum(toSumMSE)
        change_theta1 = (2/len(toSumMSE)) * X.T.dot(toSumMSE)

        theta0 -= lr * change_theta0
        theta1 -= lr * change_theta1

        if i in records:
            thetaSet.append((theta0.copy(),theta1.copy()))

    return theta0, theta1, thetaSet

lr = 2e-3
theta0, theta1, thetaSet = gradDescent(X,y,lr,[10,50,200,500,1000,1500,1800])

y_pred = theta0 + X.dot(theta1)
plt.plot(X,y_pred, "r")

plt.show()
