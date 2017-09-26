#imports toolset
import pandas

#creates workable data set
wages=pandas.read_csv("wages.csv")

#returns the gender and yearsExperience columns
ge=wages.iloc[0:,0:2]

#returns the columns with no duplicates
ge=ge.drop_duplicates()

#sorts the columns by gender then yearsExperience
ge=ge.sort_values(['gender', 'yearsExperience'])
print(ge)