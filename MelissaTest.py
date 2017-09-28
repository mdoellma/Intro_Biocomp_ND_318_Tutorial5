import pandas
import numpy
import sys
import re
data = pandas.read_csv("wages.csv", delimiter=",")

selectcolumn=data.iloc[:,[0,1,3]]
H = data.sort_values('wage', ascending = False)
H=H.iloc[0:1]
print selectcolumn
print "The highest Earner is",'\n',H
w = data.sort_values('wage', ascending = False)
w=w.iloc[-1]
print "The Lowest Earner is",'\n',w

#Q3
columnQ3=data.iloc[:,2:4]
low=data.wage[data.yearsSchool == 12]
high=data.wage[data.yearsSchool == 16]
print low
print high	
lowwage=min(low)		
highwage=min(high)
difference=highwage-lowwage
print difference

