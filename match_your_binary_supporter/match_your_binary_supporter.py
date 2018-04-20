'''

author - ajayghoshrr@gmail.com

'''
import os
import re
#function for reading input and writing input
def _read_write(file_path, read = False, write = False, content = None):
    with open(file_path, 'r+') as f:
        if read == True:
            return f.readlines()
        elif write == True:
            f.writelines(["%s\n" % item for item in content])
            return True
        else:
            exit()
#main function
def main():
    #read
    input_list = _read_write(os.path.join(os.getcwd(), 'input.txt'), read= True)
    _list = input_list[0]
    _final_list = []
    #parsing the each test case
    for i in input_list[1:-1]:
        try:
            #conditions
            if type(int(i.strip('\n'))) == int or len(i.strip('\n'))!=0:
                if len(re.findall(str(len(bin(int(i.strip('\n')))[2:]) + int(i.strip('\n'))), _list)) == 1 and len(re.findall(i.strip('\n'), _list)) == 1:
                    _final_list.append('{0} is SUPPORTED BY THE NUMBER {1}'.format(i.strip('\n'), len(bin(int(i.strip('\n')))[2:]) + int(i.strip('\n'))))
                elif len(re.findall(str(len(bin(int(i.strip('\n')))[2:]) + int(i.strip('\n'))), _list)) > 1 or len(re.findall(i.strip('\n'), _list)) >1:
                    _final_list.append('Exception : {0} is a duplicate entry!'.format(i.strip('\n')))
                elif len(re.findall(i.strip('\n'), _list)) == 0:
                    _final_list.append('Exception : {0} is not in the list!'.format(i.strip('\n')))
                else:
                    _final_list.append('{0} is NOT SUPPORTED'.format(i.strip('\n')))
            else:
                pass
        #catching value error
        except ValueError:
            if len(i.strip('\n'))==0:
                _final_list.append('No input provided!')
            else:
                _final_list.append('Exception : {value} is a string!'.format(value=i.strip('\n')))
                pass

    input_list = _read_write(os.path.join(os.getcwd(), 'output.txt'), write= True, content= _final_list)


if __name__ == '__main__':
    main()
#complexity - < Big O(n)
