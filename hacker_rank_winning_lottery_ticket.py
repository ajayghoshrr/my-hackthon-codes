

'''
The SuperBowl Lottery is about to commence, and there are several lottery tickets being sold, and each ticket is identified with a ticket ID. In one of the many winning scenarios in the Superbowl lottery, a winning pair of tickets is:

Concatenation of the two ticket IDs in the pair, in any order, contains each digit from  to  at least once.
For example, if there are  distinct tickets with ticket ID  and ,  is a winning pair.

NOTE: The ticket IDs can be concantenated in any order. Digits in the ticket ID can occur in any order.

Your task is to find the number of winning pairs of distinct tickets, such that concatenation of their ticket IDs (in any order) makes for a winning scenario. Complete the function winningLotteryTicket which takes a string array of ticket IDs as input, and return the number of winning pairs.

Input Format

The first line contains  denoting the total number of lottery tickets in the super bowl. 
Each of the next  lines contains a string, where string on a  line denotes the ticket id of the  ticket.

Constraints

 length of  
sum of lengths of all 
Each ticket id consists of digits from 
Output Format

Print the number of pairs in a new line.

Sample Input 0

5
129300455 
5559948277
012334556 
56789
123456879
Sample Output 0

5
Explanation 0

Pairs of distinct tickets that make for a winning scenario are :

Ticket ID 1	Ticket ID 2	Winning Pair
Notice that each winning pair has digits from  to  atleast once, and the digits in the ticket ID can be of any order. Thus, the number of winning pairs is .

'''


#!/bin/python

import sys

def winningLotteryTicket(tickets):
    count = 0
    # Complete this function
    number = [0,1,2,3,4,5,6,7,8,9]
    #print tickets
    sample_list = []
    for i in range(len(tickets)):
        for j in range(i+1,len(tickets)):
            #print tickets[i],tickets[j]
            sample_list.append(str(tickets[i])+str(tickets[j]))
    #print sample_list,'sample_list'
    for i in sample_list:
        if len(sorted(list(set(list(i))))) == 10:
            count = count + 1
            pass
        else:
            pass
    return count
if __name__ == "__main__":
    n = int(raw_input().strip())
    tickets = []
    tickets_i = 0
    for tickets_i in xrange(n):
        tickets_t = str(raw_input().strip())
        tickets.append(tickets_t)
    result = winningLotteryTicket(tickets)
    print result
