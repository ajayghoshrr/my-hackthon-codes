#used to take input from the file and print to the file.
#quite interesting
import sys
def redirect_to_file(text):
    #print text
    original = sys.stdout
    sys.stdout = open('redirect.txt', 'a+')
    print text
    sys.stdout = original

def main():
    redirect_to_file("Hello"*1000)
    redirect_to_file("Amme Devi")
def input():
    sys.stdin = open('input.txt', 'r')
    x =raw_input()
    y = raw_input()
    print x
    print y
if __name__ == '__main__':
    main()
    input()
    #redirect_to_file('Python Rocks')


