n = int(input())
cnt = n
passwords = []

while n >= 1:
    password = input()
    passwords.append(password)
    n -= 1

for password in passwords:
    
    crit_1 = False
    crit_2 = False
    crit_3 = False
    crit_4 = False
    
    for char in password:
        if char in "1234567890":
            crit_1 = True
        elif char in "qwertyuiop":
            crit_2 = True
        elif char in "asdfghjkl":
            crit_3 = True
        elif char in "zxcvbnm":
            crit_4 = True
    
    if crit_1 and crit_2 and crit_3 and crit_4:
        print("strong")
    else:
        print("weak")
            

