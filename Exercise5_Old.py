#Exercise 5 Om and Joshua

import os
import numpy
import pandas


#Set working directory and read in wages file
os.chdir('/Users/omneelay/Desktop/Exercise5/Intro_Biocomp_ND_318_Tutorial5/')
wages=pandas.read_csv("wages.csv")

#START OF CHALLENGE 1
#isolate 2 columns: Gender and YearsExperience 
first2columns=wages.iloc[:,0:2]

#isolate females and males separately
females=first2columns[first2columns.gender=="female"]
males=first2columns[first2columns.gender=="male"]

#remove duplicates and make into panda dataframe form
F=females.drop_duplicates()
M=males.drop_duplicates()
f=pandas.DataFrame(F)
m=pandas.DataFrame(M)

#concatenate dataframes and write to a file
A=pandas.concat([f,m])
first2columnsA=A.iloc[:,0:2]
first2columnsA
A.to_csv("challenge1.txt",sep=' ')

#START OF CHALLENGE 2