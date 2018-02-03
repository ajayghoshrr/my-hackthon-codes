'''

Shawn and Arrays
Shawn has been obsessed about arrays since he read how fun they can be. He recently had a visitor who was ready to challenge Shawn in any array challenge. 
Shawn thought about challenging him to a question that he has been working on. He gave the visitor two arrays that contain n positive integers and asked him to check if the arrays are equal.

The arrays will be equal if both the arrays contain the same elements. The permutation of elements doesn’t matter. 
If they are not equal, the visitor needs to find the smallest single positive integer element that can be added 
to any one of the elements of any of the arrays to make them equal.

Help the visitor in solving the challenge.

Constraints

1<=T<=100

1<=n<=10000

0<=ar[i]<=1000

Sample Input Format

The first line of input consists of an integer T which is the number of test cases

The first line of each test case contains an integer n which indicates the size of both arrays

The second and third line of each test case contains n space separated integers which are the elements of the first and second arrays respectively

Sample Output Format

For each test case, if

The arrays are equal, print "Yes" (Without quotes)

If the arrays are not equal, print out two space separated integers p and q. Here p is the smallest positive integer that needs to be added to an element of array q


If there is no such integer, then print “No” (Without quotes)


#------------------------------------------
Input
======
3
5
1 4 0 2 5
2 0 5 1 4
3
1 7 1
7 7 1
3
3 1 7
2 5 4

Output
======
Yes
6 1
No


'''








def helper(array1, array2):
    if array2[0] > array1[0]:
        out1 = int(array2[0]) - int(array1[0])
        out2 = array1[0]
        #print "HU"
    else:
        out1 = int(array1[0]) - int(array2[0])
        out2 = array2[0]
    return out1, out2

no_of_test_cases = int(input())
#print no_of_test_cases
for i in range(no_of_test_cases):
    max_limit = int(input())
    #print max_limit
    array_1 = raw_input()
    array_2 = raw_input()
    array1 = sorted(array_1.split())
    array2 = sorted(array_2.split())
    array1 = map(int, array1)
    array2 = map(int, array2)
    if array1 == array2:
        print "Yes"
    elif len(array1) != len(array2):
        print "No"
    else:
        dj = []
        #print array1,array2
        while(len(set(array1) & set(array2)) != 0):
            try:
                m = 0
                if array1[m] in array2:
                    #print "A"
                    io = array1[m]
                    array1.pop(array1.index(array1[m]))
                    array2.pop(array2.index(io))
                    m =m+1
                    #print array2,array1
                else:
                    #print 'B'
                    dj.append(array1[m])
                    array1.pop(array1.index(array1[m]))
                    m = m+1
            except:
                pass
        #print array1, array2, dj
        if len(array1)>1 or len(array2)>1 or len(dj)>1:
            print "No"
        else:
            if len(dj) == 0 and (len(array2)==1 and len(array1) == 1):
                out1,out2=helper(array1,array2)
                print out1,out2
            else:
                if len(dj) == 1 and len(array1)==1:
                    out1, out2 = helper(dj, array1)
                    print out1, out2
                elif len(dj) == 1 and len(array2)==1:
                    out1, out2 = helper(dj, array2)
                    print out1, out2
                else:
                    print "No"



