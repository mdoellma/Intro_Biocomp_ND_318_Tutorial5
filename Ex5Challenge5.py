#!/bin/python
from __future__ import print_function
import pandas, numpy

def Q1solution(wages):
    ordered=wages.sort_values("yearsExperience")
    ordered=ordered.reset_index(drop=True)
    outText=[]
    for i in range(ordered.shape[0]):
        pair = "{} {}".format(ordered.gender[i],ordered.yearsExperience[i])
        if pair not in outText:
            outText.append(pair)
    
    outFile=open('gender-yearsExperience.txt','w')
    print('\n'.join(outText),file=outFile)
    outFile.close()
    return

def Q2solution(wages):
    """
    #############################
    Assume that pandas and numpy have already been imported and that you have
    access to wages.csv as the pandas dataframe object wages. Leave the return,
    write your code (indented) between the "def Q2solution" and the "return"
    #############################
    >>> testG = ["male","female","male","male","female","male","male","male","female","male","male"]
    >>> testYE = [6,5,4,1,1,10,8,2,5,3,4]
    >>> testYS = [12,12,16,14,13,16,18,6,16,12,21]
    >>> testW =[2.09405811,12.861342479,6.1056621467999994,3.9808917197,5.6311238472,1.3456535391,3.8947576562,1.3551971812,4.4437861058,3.9808917197,0.086111532]
    >>> d = {'gender' : testG,'yearsExperience' : testYE,'yearsSchool' : testYS,'wage' : testW}
    >>> df = pandas.DataFrame(data=d)
    >>> Q2solution(df)
    
    """
    
    
    return

def Q3solution(wages):
    """
    >>> testG = ["male","female","male","male","female","male","male","male","female","male","male"]
    >>> testYE = [6,5,4,1,1,10,8,2,5,3,4]
    >>> testYS = [12,12,16,14,13,16,18,6,16,12,21]
    >>> testW =[2.09405811,12.861342479,6.1056621467999994,3.9808917197,5.6311238472,1.3456535391,3.8947576562,1.3551971812,4.4437861058,3.9808917197,0.086111532]
    >>> d = {'gender' : testG,'yearsExperience' : testYE,'yearsSchool' : testYS,'wage' : testW}
    >>> df = pandas.DataFrame(data=d)
    >>> Q3solution(df)
    "Those with a 4 year degree (16 yearsSchool) earned 2.6352381806 more than those with just a high school degree (12 yearsSchool)."
    """
    print "Not Working"
    return

################################

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print "Done."
    # wages = pandas.read_csv("wages.csv")