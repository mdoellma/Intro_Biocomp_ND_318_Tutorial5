#Tutorial
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