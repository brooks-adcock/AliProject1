course_names = ['csc121', 'csc122', 'csc221']


def show_roster(r_list):
	course_name = input('Which course would you like to see the roster for? ')
	course_index = course_names.index(course_name.lower())
	if course_index == -1:
		print("Invalid Course Name")
		print("Valid Courses Are: ", course_names)
	elif len(r_list[course_index]) == 0:
		print("No one is currently registered for ", course_name)
	else:
		print(course_name, " has ", len(r_list[course_index]), " people registered. They are...")
		for user_id in sorted(r_list[course_index]):
			print(user_id)


def change_max_size(r_list , m_list):
	course_name = input('Which course would you change the max size?: ')
	course_index = course_names.index(course_name.lower())
	if course_index == -1:
		print("Invalid Course Name")
		print("Valid Courses Are: ", course_names)
	else:
		current_enrollment = len(r_list[course_index])
		print("Current Enrollment: ", current_enrollment)
		print("Current Max Size: ", m_list[course_index])

		new_max_size = current_enrollment - 1
		while new_max_size < current_enrollment:
			new_max_size = input("New Max Size: ")

			if new_max_size < current_enrollment:
				print("Max size cannot be less than current enrollment")
			else:
				m_list[course_index] = new_max_size
				print("Course max sized changed to ", new_max_size)
		



	pass