input_dict = {'ravi': 15, 
            'rajnish': 16, 
            'sanjeev': 20, 
            'yash': 12, 
            'suraj': 10
            }
sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
