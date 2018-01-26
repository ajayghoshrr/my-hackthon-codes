
# --------------- CTS Code - just converting a digit to roman number ---------------
def roman_converter(n):
    roman_string = ''
    sample_dict = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',0:'X'}
    if int(n)<40:
        if len(str(n))==1:
            return sample_dict[int(n)]
        else:
            x = list(str(n))[-1]
            y = list(str(n))[:-1][0]
            #print y
            for i in range(int(y)):
                #print i
                roman_string +='X'
            for i in x:
                roman_string = roman_string + sample_dict[int(i)]
            return roman_string
    else:
        print 'I cant do'
x = roman_converter(32)
print x
