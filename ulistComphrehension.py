numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

name = 'Angela'
letters_list = [letter for letter in name]

new_list = [n*2 for n in range(1,5)]
print(new_list)

names = ['Alex','Beth','Carolina','Dave','Freddie']

new_names = [name.upper() for name in names if len(name)>4]
print(new_names)

import random

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passed_students = {student:score for (student,score) in student_scores.items() if score > 60}

print(passed_students)