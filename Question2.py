
print('---------------Question 1 -> Point 1-----------------')
print('Creating Empty Dog Dictionary')
dog = {}
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 2-----------------')
print('Adding name, color, breed, legs, age to the dog dictionary')
dog['name'] = 'Daisy'
dog['color'] = 'Black'
dog['breed'] = 'Labrador Retriever'
dog['legs'] = 4
dog['age'] = 14
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 3-----------------')
print('Creating Empty Student Dictionary and Adding first_name, last_name, gender, age, marital status, skills, country, city and address as keys')
student = {}

student['first_name'] = 'Sandeep'
student['last_name'] = 'Yadav'
student['gender'] = 'Male'
student['age'] = 31
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'Java', 'DotNet', 'CSS']
student['country'] = 'USA'
student['city'] = 'Kansas'
student['address'] = '106th St'
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 4-----------------')
studentLen = len(student)
print(f'Student Dictionary Length is {studentLen}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 5-----------------')
skills = student['skills']
print(f'Datatype of skills is {type(skills)}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 6-----------------')
skills.append('Angular')
skills.append('SQL')
print(f'Student Skills : {student["skills"]}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 7-----------------')
keys = list(student)
print('Student Dictionary Keys:')
print(f'{keys}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 8-----------------')
values = list(student.values())
print('Student Dictionary Values:')
print(f'{values}')
print('')

#----------------------------------------------------