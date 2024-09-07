students = {
    101: {'name': 'Alice', 'age': 17, 'grade': '11th'},
    102: {'name': 'Bob', 'age': 16, 'grade': '10th'},
    103: {'name': 'Charlie', 'age': 18, 'grade': '12th'}
}
for k,v in students[102].items():
    # print(k)
    if k == 'age':
        if k.isdigit():
            print(v)
        v += 1

    print(v)
# print(students[102]['age'])