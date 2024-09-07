def nom(user_num):
    if len(user_num) != 18:
        return False
    
    if user_num[:5] != "(998)":
        return False
    
    if not (user_num[6:8].isdigit() and user_num[8] == '-' and
            user_num[9:12].isdigit() and user_num[12] == '-' and 
            user_num[13:15].isdigit() and user_num[15] == '-' and
            user_num[16:18].isdigit()):
        return False
    return True
in_num = input("Namunaga qarab nomer kiriting: (998) xx-xxx-xx-xx\n")

if nom(in_num):
    print(True)
else:
    print(False)