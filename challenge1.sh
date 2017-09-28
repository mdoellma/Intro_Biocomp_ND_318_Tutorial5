import pandas
wages=pandas.read_csv("wages.csv")
years=wages.iloc[:, 0:2]
sorted_years=years.sort_values(by= ['gender', 'yearsExperience'])
unique=sorted_years.drop_duplicates()
unique.to_csv('uniquegenderyears', sep=' ', index=False)
