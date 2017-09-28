import pandas
import numpy
data = pandas.read_csv("wages.csv", delimiter=",")

H = data.sort_values('wage', ascending = False)
H=H.iloc[0:1]
print "The highest Earner is",'\n',H
w = data.sort_values('wage', ascending = False)
w=w.iloc[-1]
print "The Lowest Earner is",'\n',w

#Q3
columnQ3=data.iloc[:,2:4]
for line in columnQ3:
	if line == 12:
		print line


