#imports toolset
import pandas

#creates workable data set
wages=pandas.read_csv("wages.csv")

#--Start Challenge 1--
#returns the gender and yearsExperience columns
ge=wages.iloc[0:,0:2]

#returns the columns with no duplicates
ge=ge.drop_duplicates()

#sorts the columns by gender then yearsExperience
ge=ge.sort_values(['gender', 'yearsExperience'])
print(ge)
#--End Challenge 1--

#--Start Challenge 2
#return gender, yearsExp, and wage for highest earner
highest_earner = wages.sort_values(['wage']).iloc[len(wages) - 1]
print(highest_earner)

#return gender, yearsExp, and wage for highest earner
lowest_earner = wages.sort_values(['wage']).iloc[0]
print(lowest_earner)

#return number of females in top ten earnesr
top_ten = wages.sort_values(['wage'],ascending=False).iloc[0:10]
print(len(top_ten[top_ten.gender=="female"]))
#-- End Challenge 2

#--Start Challenge 3
#Returns the yearsExp and wage columns
minmax=wages.iloc[0:,2:]

#Sorts the set by the yearsExp column
minmax=minmax.sort_values(['yearsSchool'])
minmax

#Finds and sets a variable for the lowest 16yr earner and lowest 12yr earner
min=minmax.head(n=1)
min=min.iloc[0,1]
max=minmax.tail(n=1)
max=max.iloc[0,1]

#Does the aritmetic and prints the value
D=max-min
print('Increase in minimum wage after graduating college is' , D)

#---------------- 
# get separate dataframes for yearsSchool and sort by wage, lowest first
years_12 = wages[wages.yearsSchool == 12].sort_values(['wage'])
years_16 = wages[wages.yearsSchool == 16].sort_values(['wage'])

#get the minimum wage for the first row in each dataframe
minwage_12 = years_12.iloc[0].wage
minwage_16 = years_16.iloc[0].wage

#output
print('Increase in minimum wage after graduating college is', minwage_16 - minwage_12)


#--End of Challenge 3--