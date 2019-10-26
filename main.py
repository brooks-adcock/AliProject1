# ---------------------------------------------------------------------------------------------------------- #
# CSC121 Project 1
# Ali Adcock 10/25/19
# This program allows students to add/drop a class as well as allows admins to edit course size and roster
# ---------------------------------------------------------------------------------------------------------- #

import student
import admin

def main():
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    admin_list = [('7001', '777'), ('8001', '888')]
    course_list = ['csc121', 'csc122', 'csc221']
    max_size_list = [2, 2, 1]
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    user_type = input('Enter 1 for student, 2 for admin, 0 to quit: ')

def login(id_list):
    # student input
    if user_type == '1':
        id = int(input('Enter student ID: '))
        pin = int(input('Enter student PIN: '))
        for each in id_list:
            if id and pin not in each:
                print('Invalid ID or PIN.')
        else:
            print('ID and PIN verified.')
    # add in student .py
#admin input
    if user_type == '2':
        id = int(input('Enter admin ID: '))
        pin = int(input('Enter admin PIN: '))
        for each in admin_list:
            if id and pin not in each:
                print('Invalid ID or PIN.')
        else:
            print('ID and PIN verified.')
    # add in admin .py

# Exit
    if user_type == '0':
        print('Goodbye.')
