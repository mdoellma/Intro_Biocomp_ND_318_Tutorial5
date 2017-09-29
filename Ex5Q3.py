#Exercise 5 Question 3
import pandas
#load file
wages=pandas.read_csv("wages.csv",header=0,sep=",")
#select columns 3 & 4
newwages = wages[['yearsSchool', 'wage']]
#select only 12 years experience
grouped12 = newwages.loc[grouped['yearsSchool'] == 12]
#select only 16 years experience
grouped16 = grouped.loc[grouped['yearsSchool'] == 16]
#sort grouped12 numerically by wages
grouped12sorted = grouped12.sort_values(by= 'wage', ascending=False) 
#sort grouped16 numerically by wages
grouped16sorted = grouped16.sort_values(by= 'wage', ascending=False)
#minimum wage of high school graduate
minval12 = grouped12sorted.tail(1)
#miniumum wage of college graduate
minval16 = grouped16sorted.tail(1)
#assign minimum wage of high school graduate to variable test1
test1 = minval12["wage"].values
#assign minimum wage of college graduate to variable test2
test2 = minval16["wage"].values
#subract wages to find difference
answer = test2 - test1
print (answer)
