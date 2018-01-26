#!/bin/python

#program for finding the toper of coding competition.

#sample input given below

'''
--------------------------------Question -----------------------------------------
HackerRank has organized a hiring contest, from December until the end of January. The programmer who solves the most questions in this contest, will get an interview, which is the first step into getting hired in HackerRank. If multiple programmers have solved the highest number of questions (the case of a draw), the winner is the programmer with the maximum number of solved questions appearing first in the list as shown in the following example:

image

Given the number of programmers participating in the competition, their names and the number of questions they have solved from the beginning of December and until the end of January, find the name of the programmer who wins the competition and show how many questions he/she has solved during the competition.

Input Format

The first line contains an integer  denoting the number of programmers participating in the contest. 
The following  lines contain a string , which represents the name of each programmer and two integers and , where, 
 - number of questions the programmer has solved until the beginning of December. 
 - number of questions the programmer has solved until the end of January.

Constraints

 (the name of each programmer) can be composed of digits (0 - 9), lowercase (a - z) and uppercase (A - Z) characters, and it is a non-empty string with at most 10 characters
The names of all programmers are unique
Output Format

Print the name of the programmer who will win the competition and the number of questions he/she has solved during the period of the competition.

Sample Input 0

5
Arber 5 11
Ardit 4 12
Marsed 3 5
Gledi 2 2
Ana 1 6
Sample Output 0

Ardit 8

---------------------------------------------------------------------------------------


'''
import sys

list_of_coders = []

if __name__ == "__main__":
    n = int(raw_input().strip())
    for a0 in xrange(n):
        name, d, j = raw_input().strip().split(' ')
        name, d, j = [str(name), int(d), int(j)]
        list_of_coders.append([name,d,j])
        #Write Your Code Here
#print list_of_coders
if n>2 and n<=1000:
    sample_dict = {}

    for i in list_of_coders:
        sample_dict[i[0]] = abs(i[1] - i[2])
    big_key = ''
    big_value = -1
    equal_values = ''
    for i in list_of_coders:
        if sample_dict[i[0]] > big_value:
            big_value = sample_dict[i[0]]
            big_key = i[0]
        elif sample_dict[i[0]] == big_value:
            equal_values = sample_dict
        else:
            pass
    #print sample_dict
    print big_key,big_value
