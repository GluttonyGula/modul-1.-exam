grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = (sum(grades[0]) / len(grades[0]))
b = (sum(grades[1]) / len(grades[1]))
c = (sum(grades[2]) / len(grades[2]))
d = (sum(grades[3]) / len(grades[3]))
e = (sum(grades[4]) / len(grades[4]))
stud = list(students)
stud.sort()
print(stud)
# dict_students = {'Aaron': a, 'Bilbo': b, 'Khendrik': c, 'Johnny': d, 'Steve': e}
# print(dict_students)
grades_students = {stud[0]: a, stud[1]: b, stud[2]: c, stud[3]: d, stud[4]: e}
print(grades_students)
