
# ----- vehicle number validation ----------infosys code----

def encrypt(unique_code_list):
    rotated_list = []
    for item in unique_code_list:
        if len(item)==9:
            temp = item.split('-')
            count = 0
            alphabet = []
            for val in temp:
                for char in val:
                    if char.isalpha() == True:
                        count = count + 1
                        alphabet.append(char)
                    else:
                        pass
                        
            if count == 2:
                if len(temp[1])==4:
                    alphabet.append(temp[1][2:4])
                    alphabet.append(temp[1][0:2])
                    value = ''
                    for i in alphabet:
                        value = str(value)+str(i)   
                    rotated_list.append(value)
            elif count == 1:
                if len(temp[1])==4:
                    alphabet.append(temp[1][1:4])
                    alphabet.append(temp[1][0])
                    value = ''
                    for i in alphabet:
                        value = str(value)+str(i)   
                    rotated_list.append(value)
        
        else:
            print ("Not a proper Vehilcle Identification number")
            return False
        #del alphabet[:]
    return rotated_list
    


x=['GT21-1011','S621-9699']
z=encrypt(x)
print (z)
