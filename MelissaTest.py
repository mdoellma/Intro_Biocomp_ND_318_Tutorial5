import pandas
import numpy
data = pandas.read_csv("wages.csv", delimiter=",")


column=data.iloc[0:,:4]
print(column)
w = data.sort_values('wage', ascending = False)
w=w.iloc[0:1]
print(w)


