#!/bin/python
"""
BIOS 30318/60318 - Introduction to Biocomputing
Exercise 5 Challenge
Grant Keller and Kathleen Nicholson
"""
from __future__ import print_function
import sys
import pandas

def q1solution(wages):
    """
    Writes out a file containing all the unique gender-yearsExperience pairs
    in the data set given (wages.csv). These are written to file
    "gender-yearsExperience.txt" saved in the current working directory.
    """
	# remove yearsSchool and wage columns from the data set
    ordered = wages.drop(["yearsSchool", "wage"], axis=1)
	# sort by gender then yearsExperience, so that the output consists of
	# 	blocks of gender sorted alphabetically (e.g. female then male) 
	# 	sorted numerically by yearsExperience (i.e. female 1-18 followed by male 2-19)
    ordered.sort_values(["gender", "yearsExperience"], inplace=True)
	# removes non-unique rows on "ordered" object
    ordered.drop_duplicates(inplace=True)
	# writes out a space-delimited csv file containing only unique 
	# 	gender-yearsExperience pairs to :gender-yearsExperience.txt"
    ordered.to_csv('gender-yearsExperience.txt', sep=' ', index=False)
    return
def q2solution(wages):
    """
    #############################
    Assume that pandas and numpy have already been imported and that you have
    access to wages.csv as the pandas dataframe object wages. Leave the
    return, write your code (indented) between the "def Q2solution" and the
    "return"
    #############################
    >>> testG = ["male","female","male","male","female","male","male","male","female","male"]
    >>> testYE = [6,5,4,1,1,10,8,2,5,4]
    >>> testYS = [12,12,16,14,13,16,18,6,16,21]
    >>> testW =[2.094,12.861,6.105,3.980,5.631,1.345,3.894,1.355,4.443,0.086]
    >>> d = {'gender' : testG,'yearsExperience' : testYE,'yearsSchool' : testYS,'wage' : testW}
    >>> df = pandas.DataFrame(data=d)
    >>> Q2solution(df)
    The highest earner makes 12.861, is female and has 5 years of experience.
    The lowest earner makes 0.086, is male and has 4 years of experience.
    There are 3 females in the top ten earners.
    """
    earners = wages.drop(["yearsSchool"], axis=1)
    earners.sort_values(["wage"], inplace=True)
    earners.head(n=1)
    
    earners = wages.drop(["yearsSchool"], axis=1)
    earners.sort_values(["wage"], inplace=True)
    earners.tail(n=1)
    
    earners = wages.drop(["yearsSchool"], axis=1)
    earners.sort_values(["wage"], inplace=True)
    earners.tail(n=10)
    earners.ix['female']
    # the code breaks down when I attempt to filter 
    series.str.len("earners")
    print("There are {0} females who are top ten earners.").".format(len("earners"))"
    return
def q3solution(wages):
    """
    Prints to stdout the difference in minimum wage for yearsSchool 12 (HS)
    and 16 (college) in this dataset (wages.csv).
    ################
    >>> testG = ["male","female","male","male","female","male","male","male","female","male","male"]
    >>> testYE = [6,5,4,1,1,10,8,2,5,3,4]
    >>> testYS = [12,16,12,14,13,12,18,6,16,16,21]
    >>> testW =[2.094,12.861,6.105,3.980,5.631,1.345,3.894,1.355,4.443,3.98,0.086]
    >>> d = {'gender' : testG,'yearsExperience' : testYE,'yearsSchool' : testYS,'wage' : testW}
    >>> df = pandas.DataFrame(data=d)
    >>> q3solution(df)
    Those with a 4 year degree (16 yearsSchool) earned 2.635 more than those with just a high school degree (12 yearsSchool).
    """
	# Anonymous function which returns the smallest wage given a pandas dataframe
	# 	to search through and a number of years in school to search by.
    min_wage = lambda wages, num: min(wages.wage[wages.yearsSchool == num])
    print("Those with a 4 year degree (16 yearsSchool) earned {0} more than those with just a high school degree (12 yearsSchool).".format(min_wage(wages, 16)-min_wage(wages, 12)))
    return
################################
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Done.")
    WAGES = pandas.read_csv("wages.csv")
    q1solution(WAGES)
    q2solution(WAGES)
    q3solution(WAGES)
    