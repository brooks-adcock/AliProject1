course_names = ['csc121', 'csc122', 'csc221']


# id is the ID of the student to be added
# r_list is the list of class rosters; m_list is the list of maximum class sizes.
def add_course(id, r_list, m_list):
    course_name = input('Which course would you like to add? ')
    course_index = course_names.index(course_name.lower())
    if course_index == -1:
        print("Invalid Course Name")
        print("Valid Courses Are: ", course_names)
    elif id in r_list[course_index]:
        print("You're already registered for ", course_name)
    elif len(r_list[course_index]) > m_list[course_index]:
        print("Tough luck,", course_name, " is already full")
    else:
        r_list[course_index].append(id)
        print("You've added ", course_name)


# id is the ID of the student to be dropped
# r_list is the roster list
def drop_course(id , r_list):
    course_name = input('Which course would you like to drop? ')
    course_index = course_names.index(course_name.lower())

    if course_index == -1:
        print("Invalid Course Name")
        print("Valid Courses Are: ", course_names)
    elif id not in r_list[course_index]:
        print("You're not registered for ", course_name)
    else:
        r_list[course_index].remove(id)
        print("You have dropped ", course_name)


def list_courses(id , r_list):
    registered_course_indices = []
    for index in range(len(r_list)):
        if id in r_list[index]:
            registered_course_indices.append(index)

    if len(registered_course_indices) == 0:
        print("You are not registered for any classes yet.")
    else:
        print("You are registered for ", len(registered_course_indices), "course(s). They are...")
        for index in registered_course_indices:
            print(course_names[index])


