import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
         ,'o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9','10']
symbol=['!','@','#','$','%','^','&','*']

print("Welcome to password generator")

letter=int(input("Enter the letter you would like to ? \n"))
symbols=int(input("Enter the symbol you would like \n"))
number=int(input("Enter the number you would \n"))

#method 1
password=""
password_list=[]
for i in range(1,letter+1):
    char= random.choice(letters)
    password=password + char
print(password)


for i in range(1,symbols+1):
    symb = random.choice(symbol)
    password=password + symb
print(password)

for i in range(1,number+1):
    num = random.choice(numbers)
    password=password + num
print(password)

#method 2
password_list=[]
for i in range(1,letter+1):
    char= random.choice(letters)
    password_list= password_list + char

for i in range(1,symbols+1):
    symb = random.choice(symbol)
    password_list= password_list + symb


for i in range(1,number+1):
    num = random.choice(numbers)
    password_list = password_list+ num

print(password_list)






