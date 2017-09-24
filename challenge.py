#script to compare gender and years experience 
#Authors: Melissa Stephens and Janice Love 
#Date: 2017.09.23

#Check working directory!!

f = open('myoutput.txt' ,'w+')
print f 


import numpy
import pandas
wages = pandas.read_csv("wages.csv")

y = wages.drop_duplicates('yearsExperience')

Q1 = y.loc[:, 'gender': 'yearsExperience']

gender_sorted = Q1.sort_values('gender') #sort by gender first
print gender_sorted.head(n=30),

z = gender_sorted.sort_index(axis = 1)
print z,
sorted_data = z.sort_values('yearsExperience')
print sorted_data 

sorted_data.to_csv(path_or_buf=f, sep=',')


f.close()
