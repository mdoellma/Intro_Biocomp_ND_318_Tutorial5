#script to compare gender and years experience 
#Authors: Melissa Stephens and Janice Love 
#Date: 2017.09.23

#Check working directory!!

#Q1 code 
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

sorted_data.to_csv(path_or_buf=f, sep=' ')


f.close()

#Q2 code is below 
import pandas
wages = pandas.read_csv("wages.csv")
w = wages.sort_values('wage')
w10 = w.iloc[:10] #need 10 because first one is column headers
print w10

female_tally = 0
for i in w10.gender:
    if i == "female":
        female_tally = female_tally + 1

print "Number of females in top ten earners is:" 
print female_tally
        




