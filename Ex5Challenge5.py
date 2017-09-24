#!/bin/python
"""
BIOS 30318/60318 - Introduction to Biocomputing
Exercise 5 Challenge
Grant Keller and Kathleen Nicholson
"""
from __future__ import print_function
import pandas
import numpy

def Q1solution(wages):
    """
    Writes out a file containing all the unique gender-yearsExperience pairs
    in the data set given (wages.csv). These are written to file
    "gender-yearsExperience.txt" saved in the current working directory.
    """
    ordered = wages.sort_values("yearsExperience")
    ordered = ordered.reset_index(drop=True)
    outText = []
    for i in range(ordered.shape[0]):
        pair = "{} {}".format(ordered.gender[i], ordered.yearsExperience[i])
        if pair not in outText:
            outText.append(pair)
    outFile = open('gender-yearsExperience.txt', 'w')
    print('\n'.join(outText), file=outFile)
    outFile.close()
    return

def Q2solution(wages):
    """
    #############################
    Assume that pandas and numpy have already been imported and that you have
    access to wages.csv as the pandas dataframe object wages. Leave the
    return, write your code (indented) between the "def Q2solution" and the
    "return"
    #############################
    >>> testG = ["male","female","male","male","female","male","male","male","female","male","male"]
    >>> testYE = [6,5,4,1,1,10,8,2,5,3,4]
    >>> testYS = [12,12,16,14,13,16,18,6,16,12,21]
    >>> testW =[2.09405811,12.861342479,6.1056621467999994,3.9808917197,5.6311238472,1.3456535391,3.8947576562,1.3551971812,4.4437861058,3.9808917197,0.086111532]
    >>> d = {'gender' : testG,'yearsExperience' : testYE,'yearsSchool' : testYS,'wage' : testW}
    >>> df = pandas.DataFrame(data=d)
    >>> Q2solution(df)
    The highest earner makes 12.861342479, is female and has 5 years of experience.
    The lowest earner makes 0.086111532, is male and has 4 years of experience.
    There are 3 females in the top ten earners.
    """
    
    return

def Q3solution(wages):
    """
    Prints to stdout the difference in minimum wage for yearsSchool 12 (HS)
    and 16 (college) in this dataset (wages.csv).
    
    >>> testG = ["male","female","male","male","female","male","male","male","female","male","male"]
    >>> testYE = [6,5,4,1,1,10,8,2,5,3,4]
    >>> testYS = [12,16,12,14,13,12,18,6,16,16,21]
    >>> testW =[2.09405811,12.861342479,6.1056621467999994,3.9808917197,5.6311238472,1.3456535391,3.8947576562,1.3551971812,4.4437861058,3.9808917197,0.086111532]
    >>> d = {'gender' : testG,'yearsExperience' : testYE,'yearsSchool' : testYS,'wage' : testW}
    >>> df = pandas.DataFrame(data=d)
    >>> Q3solution(df)
    Those with a 4 year degree (16 yearsSchool) earned 2.6352381806 more than those with just a high school degree (12 yearsSchool).
    """
    minWage = lambda wages,num: min(wages.wage[wages.yearsSchool == num])
    print("Those with a 4 year degree (16 yearsSchool) earned {0} more than those with just a high school degree (12 yearsSchool).".format(minWage(wages, 16)-minWage(wages, 12)))
    return

################################

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("Done.")
    wages = pandas.read_csv("wages.csv")    
    Q1solution(wages)
    Q2solution(wages)
    Q3solution(wages)
    