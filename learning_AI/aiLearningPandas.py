
import pandas as pd

data = [1, 2, 3]
index = ['a', 'b', 'c']

example = pd.Series(data, index, name='series')
print(example)

print(pd.Series(data),"\n")

print(pd.DataFrame({ 'A' : { 'a':1, 'b':4}, 'B': {'a':2,'b':5}, 'C':{'a':3, 'b':6} }),"\n")

table = pd.read_csv("username.csv",sep=",")
print(table,"\n")

table.replace(to_replace='booker12', value='booker11', inplace=True)
print(table,"\n")

table1 = table.copy()
table1.loc[1] = ["grey06",2006, "Jean","Grey"]
print(table1,"\n")

print(pd.concat([table,table1],axis=1),"\n")

print(table.drop(0,axis=0),"\n")
print(table.drop("Last",axis=1),"\n")
