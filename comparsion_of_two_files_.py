# ----- Compare two file and print the additional data, or which is not similar, 
#You can change into any set method like intersection, 

'''x not in s	 	test x for non-membership in s
s.issubset(t)	s <= t	test whether every element in s is in t
s.issuperset(t)	s >= t	test whether every element in t is in s
s.union(t)	s | t	new set with elements from both s and t
s.intersection(t)	s & t	new set with elements common to s and t
s.difference(t)	s - t	new set with elements in s but not in t
s.symmetric_difference(t)	s ^ t	new set with elements in either s or t but not both
s.copy()
'''
#THERE IS A PREDEFINED FUNCTION FILE COMPARE - YOU CAN USE THAT
def compare_files(file1, file2):
    with open(file1, 'r') as file1:
        with open(file2, 'r') as file2:
            same = set(file1).difference(file2)
    same.discard('\n')
    with open('some_output_file.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)
#It will create a file 'some_out_put_file' have additional data in file2
