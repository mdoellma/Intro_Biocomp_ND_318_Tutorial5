#script to compare gender and years experience 
#Authors: Melissa Stephens and Janice Love 
#Date: 2017.09.23

#Check working directory!!
import numpy 
import pandas
wages = pandas.read_csv("wages.csv")
wages.drop_duplicates()
wages.loc[:, 'gender':'yearsExperience'] 
Q1 = wages.loc[:, 'gender': 'yearsExperience']
gender_sorted = Q1.sort_values('gender')#sort by gender first
print gender_sorted.head(n=30)
y = gender_and_years.drop_duplicates()
print y.head(n=20)

