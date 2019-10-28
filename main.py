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

	user_type = '1'
	while user_type in ['1', '2']:
		user_type = input('Enter 1 for student, 2 for admin, 0 to quit: ')

		if user_type == '1':
			student_session(roster_list, max_size_list, student_list)
		elif user_type == '2':
			admin_session(roster_list, max_size_list, student_list, admin_list)

	print('Goodbye.')
	exit(1)


def login(id_list):
	id = input('Enter ID: ')
	pin = input('Enter PIN: ')

	if (id, pin) in id_list:
		print('ID and PIN verified.')
		return id, True
	else:
		print('Invalid ID or PIN.')
		return id, False

def student_session(r_list, m_list, s_list):
	user_id, session_valid = login(s_list)

	while session_valid:
		selection = input("Enter 1 to add course, 2 to drop course, 3 to see courses you have registered, 0 to exit:")
		if selection == '0':
			session_valid = False
		elif selection == '1':
			student.add_course(user_id, r_list, m_list)
		elif selection == '2':
			student.drop_course(user_id, r_list)
		elif selection == '3':
			student.list_courses(user_id, r_list)

	print("Logging out...")


def admin_session(r_list, m_list, s_list, a_list):
	user_id, session_valid = login(a_list)

	while session_valid:
		selection = input("Enter 1 to show class roster, 2 to change max class size, 0 to exit:")
		if selection == '0':
			session_valid = False
		elif selection == '1':
			admin.show_roster(r_list)
		elif selection == '2':
			admin.change_max_size(m)

	print("Logging out...")


main()
