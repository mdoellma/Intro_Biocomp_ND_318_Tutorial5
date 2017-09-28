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
print("Highest Earner:")
print(highest_earner)

#return gender, yearsExp, and wage for highest earner
lowest_earner = wages.sort_values(['wage']).iloc[0]
print("Lowest Earner:")
print(lowest_earner)

#return number of females in top ten earners
top_ten = wages.sort_values(['wage'],ascending=False).iloc[0:10]
print(len(top_ten[top_ten.gender=="female"]))
#-- End Challenge 2

#--Start Challenge 3
# get separate dataframes for yearsSchool and sort by wage, lowest first
years_12 = wages[wages.yearsSchool == 12].sort_values(['wage'])
years_16 = wages[wages.yearsSchool == 16].sort_values(['wage'])

#get the minimum wage for the first row in each dataframe
minwage_12 = years_12.iloc[0].wage
minwage_16 = years_16.iloc[0].wage

#output
print('Increase in minimum wage after graduating college is', minwage_16 - minwage_12)
#--End of Challenge 3--