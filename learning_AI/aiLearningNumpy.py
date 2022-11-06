
import numpy as np

x = np.array([
    [1, 52, 22, 2, 31, 65, 7, 8, 24, 10],
    [12, 2322, 33, 1, 2, 3, 99, 24, 1, 42],
    [623, 24, 3, 56, 5, 2, 7, 85, 22, 110],
    [63, 4, 3, 4, 5, 64, 7, 82, 3, 20],
    [48, 8, 3, 24, 57, 63, 7, 8, 9, 1032],
    [33, 64, 0, 24, 5, 6, 72, 832, 3, 10],
    [12, 242, 2, 11, 52, 63, 32, 8, 96, 2],
    [13, 223, 52, 4, 35, 62, 7, 8, 9, 10],
    [19, 2, 3, 149, 15, 6, 172, 2, 2, 11],
    [34, 23, 32, 24, 54, 63, 1, 5, 92, 7]
])

print(x.shape)          # should be (10,10)

firstcol_x = x[:, 0]    # [all rows, index]
print(firstcol_x)
lastrow_x = x[-1]       # [row]
print(lastrow_x)
mean_lastrow = np.mean(lastrow_x)
print(mean_lastrow)     # mean average
diag_x = np.diag(x)
print(diag_x)           # diagonal components
var_diag = np.var(diag_x)
print(var_diag)         # variance of this array's elements
