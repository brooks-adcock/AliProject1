course_list = ['csc121' , 'csc122' , 'csc221']
max_size_list = [2, 2, 1]
roster_list = [['1004' , '1003'] ,  ['1001'] , ['1002']]



# id is the ID of the student to be added
# r_list is the list of class rosters; m_list is the list of maximum class sizes.
def add_course(id, r_list, m_list):
    add_c = input('Which course would you like to add? ')
    add_c.upper()
    while add_c not in course_list:
        print('Course not found.')
        add_c = input('Which course would you like to add? ')
    if id in r_list[0]:
        print('You are already registered in that course.')
    else:
        print('Class is full.')
    if id not in r_list[1]:
        r_list[1].append(id)
        print('You are not registered in this course.' , add_c)
    else:
        print('You are already registered in that course.')
    if id not in r_list[2]:
        print('Class is full.')


# id is the ID of the student to be dropped
# r_list is the roster list
def drop_course(id , r_list):
    drop_c = input('Which course would you like to drop? ')
    drop_c.upper()
    while drop_c not in course_list:
        print('Course not found.')
        drop_c = input('Which course would you like to add? ')
    if id in r_list[0]:
        r_list[0].remove(id)
        print('Course dropped.')
    else:
        print('You are not registered in that course.')
    if id not in r_list[1]:
        r_list[1].append(id)
        print('You are not registered in this course.')
    else:
        print('Course dropped')
        r_list[1].remove(id)
    if id not in r_list[2]:
        print('Course dropped')
        r_list[2].remove(id)



# def list_courses(id , r_list):


