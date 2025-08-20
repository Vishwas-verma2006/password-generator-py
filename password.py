#program of randon password genrator 

import random 

char = "asdffghjklopiuytrewqzxcvbnm123@"
lenght = int(input("Enter the lenght of password:- "))
password = ""
for i in range(0,lenght):
    password += random.choice(char)
    
print(password)

#program of password genrator with your name 
import random 
chars = "123456789"   # you can use this also - "qwertyuioplkjhgfdsazxcvbnm!#$%0987654321"
lenght = int(input("Enter the lenght of your password:- "))
password = "Vishwas@"

for i in range(0,lenght):
    password += random.choice(chars)
    
print(password) 

#passowrd genrator with hint 
import random
h = ["Your password cotain a name", # this are all hints 
    "Your password is 11 character",
    "password Data- name,one symbol,numeric value"]
password = "Vishwas@123"
i = input("Enter the password:- ")
if i == password:
    print("---UNLOCK---")
while i != password:
    hint = random.choice(h) # new hint genrate every time 
    print(hint) # show the hint of password 
    i = input("Enter the password:- ")
    
    if i == password:
        print("---UNLOCK---")
        break

