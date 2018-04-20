'''

author : ajayghoshrr@gmail.com

'''




import json
import csv
import os

#open json file and return dictionary
def _open_json(file_path):
        try:
            with open(file_path, 'r+') as f:
                json_dict = json.load(f)
            return json_dict
        except ValueError as ex:
            print ex
#csv writer n*n matrix
def _csv_writer(list_to_write, file_name):
    with open(file_name, 'wb') as file:
        for i in list_to_write:
            csv.writer(file).writerow(i)
    file.close()

#merging of two dict
def Merge(dict1, dict2):
    dict2.update(dict1)
    return dict2

def main():
    name_dob_height = sorted(_open_json(os.path.join(os.getcwd(), 'name_dob_height.json')))
    name_dob_salary = sorted(_open_json(os.path.join(os.getcwd(), 'name_dob_salary.json')))
    final_list = []
    final_list.append(['FirstName', 'LastName', 'Dob', 'Salary', 'Height'])
    for i in range(len(name_dob_salary)):
        final_dict = Merge(name_dob_height[i],name_dob_salary[i])
        final_list.append([final_dict['First_name'], final_dict['Last_name'], final_dict['Date_of_birth'], final_dict['Salary'], final_dict['Height']])
    _csv_writer(final_list, 'json_operations.csv')


if __name__ == '__main__':
    main()
#complexity -< Big O (n)