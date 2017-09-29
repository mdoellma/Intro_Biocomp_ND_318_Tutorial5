#Exercise 5 Om and Joshua

import os
import numpy
import pandas


#Set working directory and read in wages file
os.chdir('C:\\Users\\joshu\\OneDrive\\github\\BioComp\\Intro_Biocomp_ND_318_Tutorial5\\')
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
#isolate the gender, yearsexp, and wages for the dataframe (df)
Slice3=wages.loc[:, ['gender','yearsExperience','wage' ]]
#Slice 3 is now the working df. We will now print the highest earner
highEarn=Slice3.nlargest(1,'wage')
print "The highest earner is:" , highEarn
#We will not print the lowest earner
lowEarn=Slice3.nsmallest(1,'wage')
print "The lowest earner is:" , lowEarn
#We will indicate the number of top ten earners that are females. 
TopWages=wages.nlargest(10,'wage')
print "The number of femaales in the top ten earners is:"
TopWages.loc[TopWages.gender == 'female', 'gender'].count()
