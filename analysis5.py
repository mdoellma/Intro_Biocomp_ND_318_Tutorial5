##### Python Script for Ex 5
# Biocomputing - 9/22/17
# Brittni Bertolet and Devin Shirley

=======
# Script for Ex 5 CHALLENGE
#Task 1 (Brittni)

#SET WORKING DIRECTORY WITH 'wages.csv' INSIDE FOR FOLLOWING CODE TO WORK
# For Brittni: os.chdir('/Users/brittnibertolet/Desktop/Intro_Biocomp_ND_318_Tutorial5/')

# Read in the data set
import pandas as pd
data = pd.read_csv("wages.csv")

# Sort the data by gender first, then yearsExperience
data = data.sort_values(by = ['gender', 'yearsExperience']) 

# Drop the other columns that we don't care about
data = data.iloc[:,0:2]

# Remove duplicates 
data = data.drop_duplicates(subset=['gender', 'yearsExperience'])

# Write file 
data.to_csv("uniqueGenderExperience.txt", sep=" ", index=False)

#Task 2 (devin)
#Part1: gender, yearsExperience, and wage for the highest earner
#add data again because 'data' dataframe now only contains gender/experience combo
wages= pd.read_csv("wages.csv")
#sort by wage
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
#add numpy so we can math...
import numpy as np
#'wages' dataframe is still unaltered and can be used again
#first we want non-college graduates' average minimum wages
schoolTwelve=wages[wages.yearsSchool==12]
NoCollegeMinimum=np.average(schoolTwelve.wage)
#second we want college graduates' average minimum wages
schoolSixteen=wages[wages.yearsSchool==16]
CollegeMinimum=np.average(schoolSixteen.wage)
print("Minimum Starting Wage For Individuals with No College:",NoCollegeMinimum,"Minimum Starting Wage for Individuals with College:",CollegeMinimum)
#take the difference between the two groups
Difference=np.subtract(CollegeMinimum, NoCollegeMinimum)
print("Difference in Starting Wage Between College Graduates and Not:", Difference)

