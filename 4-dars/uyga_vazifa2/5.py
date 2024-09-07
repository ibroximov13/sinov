students = {
    101: {'name': 'Alice', 'age': 17, 'grade': '11th'},
    102: {'name': 'Bob', 'age': 16, 'grade': '10th'},
    103: {'name': 'Charlie', 'age': 18, 'grade': '12th'}
}
ism = input("Ism kiriting: ")
for k,v in students.items():
    # print(k)
    for k1,v1 in students[k].items():
        if k1 == 'name':
            print(str(v1))
if not ism == v1:
    new = {
        104:{'name': ism,
            'age': int(input("age = ")),
            'grade': input("grade = ")
            }
        }
    students.update(new)
print(students)
            
