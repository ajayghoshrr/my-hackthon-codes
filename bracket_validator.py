
#----------bracket validator  -----

def bracket_validation(string):
    count_f = 0
    count_b = 0
    if len(string)>=2:
        if string[0] == ')' or string[-1] == '(':
            return False
        else:
            for bracket in string:
                if bracket == ')':
                    count_b = count_b + 1
                else:
                    count_f = count_f + 1
        if count_f == count_b :
            return True
        else:
            return False
        
    
x = bracket_validation("()()()()")
print x
