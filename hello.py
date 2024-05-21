ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'Sorted Array : {ages}')
minAge = ages[0]
maxAge = ages[-1]
print(f'Minimum val: {minAge}')
print(f'Maximum val: {maxAge}')

#----------------------------------------------------
ages.append(minAge)
ages.append(maxAge)
print(f'Array after adding minAge and maxAge {ages}')

#----------------------------------------------------
arrayLen = len(ages)
if arrayLen % 2 == 0:
    middle = arrayLen/2
    median = ages[middle] + ages[middle+1])