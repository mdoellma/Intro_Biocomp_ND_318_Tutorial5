# Script for Ex 5
#Tutorial (Devin)
#add library
import numpy
#add data
data=numpy.loadtxt(fname="test.dat",delimiter=" ")
data
#tests for equality with double == (first column, column 0)
data[:,0]==1
#test for greater than or less than (first column, column 0)
data[:,0]>2
#using logic test for an index; rows where first entry is greater than 2, all columns
data[data[:,0]>2,:]
#add pandas to work with dataframes
import pandas
#add wages data
wages=pandas.read_csv("wages.csv")
#look at rows, columns (3294 rows, 4 columns)
wages.shape
#look at first few entries
wages.head(n=5)
#indexing a dataframe is different
#can access a column from pandas using .column_name
genders=wages.gender
print(genders.shape)
genders.head(n=5)
#using brackets you can also access specific columns with .column_name
fiveGenders=wages.gender[0:5]
print(fiveGenders.shape)
fiveGenders
#each of these strategies required assigning variables
#however, SWC showed that is not always necessary
print("first five genders:", wages.gender[0:5])
#iloc function needed for numeric based indexing
fiveGenders2=wages.iloc[0:5,0]
print(fiveGenders2.shape)
fiveGenders2
#logic based indexing for datastructures using pandas
females=wages[wages.gender=="female"]
print(females.shape)
print(females.gender.unique())
#this showed only the unique values, which should only be female since that is what 
#we indexed
#Tutorial Complete
#CHALLENGE
#Task 1 (brittni)




#Task 2 (devin)
#Part1: gender, yearsExperience, and wage for the highest earner
#first sort by wage
wagesSorted=wages.sort_values(['wage'], ascending=False)
highest_earner=wagesSorted.head(1)
highest_earner
#need to remove yearsSchool 
print("Highest Earner Info:", highest_earner[['gender','yearsExperience','wage']])
#Part2: gender, yearsExerience, and wage for the lowest earner
#use the already sorted dataframe
lowest_earner=wagesSorted.tail(1)
lowest_earner
#need to remove yearsSchool
print("Lowest Earner Info:", lowest_earner[['gender','yearsExperience','wage']])
#Part3: number of females in the top ten earners in this dataset
#use the already sorted dataframe
topTenEarners=wagesSorted.head(10)
topTenEarnersFemale=topTenEarners[topTenEarners.gender=="female"]
numberTopTenEarnersFemale=topTenEarnersFemale.shape#the first value in the tuple
print("Number of females in the top ten earners:",numberTopTenEarnersFemale[0])
#Task 3 (together)




