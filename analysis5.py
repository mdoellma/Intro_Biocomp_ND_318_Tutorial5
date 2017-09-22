##### Python Script for Ex 5
# Biocomputing - 9/22/17
# Brittni Bertolet and Devin Shirley

# Set working directory
# For Brittni: os.chdir('/Users/brittnibertolet/Desktop/Intro_Biocomp_ND_318_Tutorial5/')

# Read in the data set
import pandas 
data = pd.read_csv('wages.csv')

# Sort the data by gender first, then yearsExperience
data = data.sort_values(by = ['gender', 'yearsExperience']) 

# Drop the other columns that we don't care about
data = data.iloc[:,0:2]

# Remove duplicates 
data = data.drop_duplicates(subset=['gender', 'yearsExperience'])

# Write file 
data.to_csv("uniqueGenderExperience.txt", sep=" ", index=False)
