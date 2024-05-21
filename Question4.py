
print('---------------Question 4 -> Point 1-----------------')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(f'Length of the set it_companies is {len(age)}')
print('')

#----------------------------------------------------

print('---------------Question 4 -> Point 2-----------------')
it_companies.add('Twitter')
print("After adding Twitter company:\n", it_companies)
print('')

#----------------------------------------------------

print('---------------Question 4 -> Point 3-----------------')
it_companies.update({'Infosys','Capgemini','Wipro','TCS'})
print("After adding multiple items:\n",it_companies)
print('')

#----------------------------------------------------

print('---------------Question 4 -> Point 4-----------------')
it_companies.remove('Infosys')
print("After removing Infosys company:\n",it_companies)
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 5-----------------')
#Remove
it_companies.remove('TCS')
print("After removing TCS:",it_companies)
#Discard
it_companies.discard('TCS')
print("After discarding TCS company which is not present:",it_companies)
print("Discard does not throw error in case element not present in the set")
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 6-----------------')
A = {19, 22, 24, 20, 25, 26}
print(f'A : {A}')
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'B : {B}')
print("Join A and B:", A.union(B))
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 7-----------------')
A = {19, 22, 24, 20, 25, 26}
print(f'A : {A}')
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'B : {B}')
print("A intersection B:", A.intersection(B))
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 8-----------------')
A = {19, 22, 24, 20, 25, 26}
print(f'A : {A}')
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'B : {B}')
print("Is A Subset of B:", A.issubset(B))
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 9-----------------')
A = {19, 22, 24, 20, 25, 26}
print(f'A : {A}')
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(f'B : {B}')
print("Disjoint : ", A.isdisjoint(B))
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 10-----------------')
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A = A.union(B)
B = B.union(B)
print(f'A after joining with B: {A}')
print(f'B after joining with B: {B}')
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 11-----------------')
print(f'A : {A}')
print(f'B : {B}')
print(f'Symmertic Difference between A and B: {A.symmetric_difference(B)}')
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 12-----------------')
print(f'A : {A}')
print(f'B : {B}')
A.clear()
B.clear()
print(f'A and B after deleting completely\n A: {A} \n B: {B}')
print('')
#----------------------------------------------------

print('---------------Question 4 -> Point 13-----------------')
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Converting list to set:", set(age))
#Length of set(age)
print("Length of set:",len(set(age)))
#Length of list(age)
print("Length of list:",len(age))
print('Difference is because set does not allow duplicate values')
print('')
#----------------------------------------------------