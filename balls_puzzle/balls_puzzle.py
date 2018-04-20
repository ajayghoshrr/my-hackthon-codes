'''

author - ajayghoshrr@gmail.com

'''
import os

#function for reading input and writing input
def _read_write(file_path, read = False, write = False, content = None):
    with open(file_path, 'r+') as f:
        if read == True:
            return f.readlines()
        elif write == True:
            f.writelines(["%s " % item for item in content])
            return True
        else:
            exit()
#main function
def main():
    #read
    input_list = _read_write(os.path.join(os.getcwd(), 'input.txt'), read= True)
    K = int(input_list[0].strip('\n'))
    K_list = sorted(list(map(int,input_list[1].strip('\n').split(','))))
    N = int(input_list[2].strip('\n'))
    _list = []
    _difference = 99999999999
    for i in range(0, K-N+1):
        #abs difference - smallest
        if abs(int(K_list[i])-int(K_list[i + (N-1)])) <=_difference:
            _difference = abs(int(K_list[i])-int(K_list[i + (N-1)]))
            _list = K_list[i: i + N]
    #write
    input_list = _read_write(os.path.join(os.getcwd(), 'output.txt'), write= True, content= _list)


if __name__ == '__main__':
    main()
#complexity - < Big O(n)