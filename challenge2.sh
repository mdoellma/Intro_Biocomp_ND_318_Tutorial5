import pandas
wages=pandas.read_csv("wages.csv")
set2=wages.iloc[:,[0,1,3]]
sorted_wages=set2.sort_values(by= ['wage'], ascending=False)
print("The information of the highest earner is:")
print(sorted_wages.head(n=1))
print("The information of the lowest earner is:")
print(sorted_wages.tail(n=1))
top_earners=sorted_wages.head(n=10)
print("The number of females in the top ten earners is:")
top_earners['gender'].str.contains('female').value_counts()[True]
