# --- sorting mail id based on digits in the mail - infosys question

import re

def gmail_order_program(mail_list):
    x = {}
    for i in mail_list:
        y = re.findall(r'\d',i) 
        x[y[0]] = i
    key = x.keys()
    sort_key = sorted(key)
    final_list = []
    for i in sort_key:
        final_list.append(x[i])
    return final_list
        
 
mail_list = ['ajayghoshrr2@gmail.com', '3aha@gmail.com', '1wer@gmail.com']        
sorted_mail_list = gmail_order_program(mail_list)
print sorted_mail_list
