
print('---------------Question 1 -> Point 1-----------------')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'Sorted Array : {ages}')
minAge = ages[0]
maxAge = ages[-1]
print(f'Minimum val: {minAge}')
print(f'Maximum val: {maxAge}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 2-----------------')
ages.append(minAge)
ages.append(maxAge)
ages.sort()
print(f'Array after adding minAge and maxAge {ages}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 3-----------------')
middle:int = 0
arrayLen = len(ages)
if arrayLen % 2 == 0:
    middle = int(arrayLen/2) - 1
    medianAge = (ages[middle] + ages[middle+1])/2
else:
    medianAge = ages[arrayLen/2]

# medianAge = ages[middle]
print(f'MedianAge : {medianAge}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 4-----------------')
sum = 0
for item in ages:
    sum += item
average = sum / arrayLen
print(f'Average is {average}')
print('')

#----------------------------------------------------
print('---------------Question 1 -> Point 5-----------------')
ages.sort()
min = ages[0]
max = ages[-1]
range = max - min
print(f'Range of ages is {range}')
print('')

#----------------------------------------------------

