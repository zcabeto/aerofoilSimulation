
import numpy as np
import pandas as pd
import matplotlib.pylot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("aerofoilData.csv")
T = df["Max Thickness"].to_numpy().reshape(-1,1)
tC = df["T Chord"].to_numpy().reshape(-1,1)
P = df["Max Camber"].to_numpy().reshape(-1,1)
pC = df["P Chord"].to_numpy().reshape(-1,1)
A = df["AngleDeg"].to_numpy().reshape(-1,1)
CL = df["CL"].to_numpy().reshape(-1,1)
