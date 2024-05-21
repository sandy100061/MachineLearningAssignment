text = "I am a teacher and I love to inspire and teach people"
resultSet = set()
for item in text.split(' '):
    resultSet.add(item)
print(f'Unique words are : \n{resultSet}')