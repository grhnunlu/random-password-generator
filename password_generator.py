import random as r #importing random library for random choosing password
len_of_password = int(input("How many characters for password: ")) # asking length of password
chars_all = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM*-+/@#[]{}.,!£$%&=?0123456789" # define the characters for the password
chars_lower = "qwertyuiopasdfghjklzxcvbnm" 
chars_upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
chars_special = "*-+/@#[]{}.,!£$%&=?"
chars_num = "0123456789"
password = ""
if len_of_password >= 8 and password <= 32: # at least 1 special char, 1 upper char, 1 number
    for i in range(len_of_password-3):
        password += chars_all[r.randint(0,len(chars_all)-1)]  # adding random characters to password
    password += chars_upper[r.randint(0, len(chars_upper) - 1)]
    password += chars_special[r.randint(0, len(chars_special) - 1)]
    password += chars_num[r.randint(0, len(chars_num) - 1)]
else:
    print("enter a number between 8 and 32")
password = ''.join(r.sample(password, len(password)))
print(password)
