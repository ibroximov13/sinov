sample_dict = {
    'emp1': {'name': 'John', 'salary': 450},
    'emp2': {'name': 'Emma', 'salary': 350},
    'emp3': {'name': 'Brad', 'salary': 600},
    'emp4': {'name': 'Jack', 'salary': 800}
}

for k,v in sample_dict.items():
    for k1,v1 in sample_dict[k].items():
        if k1 == 'salary':
            if int(v1) > 500:
                print(sample_dict[k]['name'],v1)