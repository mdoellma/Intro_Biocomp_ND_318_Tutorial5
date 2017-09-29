#Excercise 5: Question 1
import pandas
#load file and replace commas with spaces
wages=pandas.read_csv("wages.csv",header=0,sep=",")
#select columns 1 & 2
newwages = wages[['gender' , 'yearsExperience']]
#sort by gender first and then years experience
sorted=newwages.sort_values(['gender', 'yearsExperience'], ascending=[True, False])
print(sorted)
#drop duplicates/unique 
dropped = sorted.drop_duplicates()
print (dropped)
