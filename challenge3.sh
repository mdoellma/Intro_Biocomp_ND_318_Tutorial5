import pandas
wages=pandas.read_csv("wages.csv")
years12=wages.wage[wages.yearsSchool==12]
years16=wages.wage[wages.yearsSchool==16]
print("Graduating college results in a minimum wage increase of: ")
years16.min()-years12.min()
