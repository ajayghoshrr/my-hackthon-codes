# code for nestway drive. converting the digits to binary , count no of ones, finding smallest/common values

'''
Sample test case - 
Input :
3
9
6 2 11 1 9 14 13 4 18
3
7 3 1
3
1 2 4

Output:

1 6 11
1 3 7 
1


'''

#function for count the no of 1s - BIT MANIPULATION is used - Right shift
def count_ones(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

#Main function
def main():
    smart_set = []
    no_of_test_cases = int(input())
    for i in range(no_of_test_cases):
        test_case = int(input())
        test_case_value = raw_input()
        test_case_list = test_case_value.split()
        sample_dict = {}
        if len(test_case_list) == test_case:
            for i in test_case_list:
                #making a sample dictionary with number as key and no of 1s as value
                sample_dict[int(i)]=count_ones(int(i))
            temp_list = []
            #sorting the dictionary based on values and then giving priority to the keys using lambda function
            temp = sorted(sample_dict.items(), key=lambda x: x[1])
            compare_var_val = -1
            #Just storing the smallest data - in the list
            for i in range(len(temp)):
                if temp[i][1]==compare_var_val:
                    compare_var_val = temp[i][1]
                    pass
                else:
                    temp_list.append(temp[i][0])
                    compare_var_val = temp[i][1]
            smart_set.append(sorted(list(set(temp_list))))
    #printing the smart list
    for i in smart_set:
        for j in i:
            print j,
        print ''

main()
