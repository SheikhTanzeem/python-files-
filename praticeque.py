# Ek program likho jo check kare number positive hai ya negative.
# Ek program likho jo check kare number even hai ya odd.
# Ek program likho jo input age lega aur bolega "Adult" ya "Minor".

# name = str(input("ENTRE YOUR NAME"))
# number = int(input("ENTRE YOUR NUMBER"))

# if number < 0:
#     print(name , "number is negative we dont accept negative numbes")

# if number > 0:
    
#     print(name ,"we are proceeing")

# number = int(input("ENTRE YOUR NUMBER "))

# if number%2 != 0:
#     print("nrgtaive number")

# if number%2 == 0:
#     print("positive number")

# 1 se 10 tak numbers print karo.
# 1 se 100 tak sabhi even numbers print karo.
# Ek list di hai [10, 20, 30, 40], iska total sum nikalna hai for loop se.

# for i in range(1,10):
#     print(i)

# for i in range(1,101):
#     if i%2 == 0:
#         print(i)

# list = [10, 20, 30, 40] 

# numbers = [10, 20, 30, 40]   # list of numbers
# total = 0                    # starting me total 0 rakhenge

# for num in numbers:          # list ke har element ko num me lenge
#     total = total + num      # total ke andar add karte rahenge

# print("Sum =", total)        # final sum print karenge

# import json

# file = open("C:/Users/Dell/Downloads/students_flat.json" , 'r')
# f = json.load(file)
# file.close()

# print(f)


# # fru = ["apple", "banana", "cherry"]
# f = []
# for i in fru:
#     print(i.upper())

# number = [2, 4, 6, 8, 10]

# for i in number:
#     print(i* i)

# Ek function banao jo ek number lega aur uska factorial return kare.
# Ek function banao jo ek list lega aur uska sum return kare (jaise tune for loop se kiya).
# Ek function banao jo 2 numbers lega aur batayega ki dono me se kaunsa bada hai.


# def bigger ( a , b):
#     if a > b :
#         print({a} ,"IS A GREATER NUMBER" ) 
    
#     elif b > a :
#         print({b},"IS THE GREATER NUMBER")
    
#     else:
#         print("both are equal")

# # bigger( 10 ,30)
# bigger(100 , 70)


# variable = ("WELLCOME")
# print(variable) 

# DATATYPES = ["INT" , "FLOT" , "STRING" , "BOLLINE"]
# print(type(DATATYPES))
# from loguru import logger
# a = 5 
# b = 10
# print(a+b) 

# a = 10 
# b = 2 
# print (a%b)

# a = int(input("print the value sir"))
# b = int(input("entre the second value "))
# print(a+b)

# print(type(a))
# print(type(b))

# a = int(input('entre the first number '))
# b = int(input('entre the second number '))

# print(a>b)

a = int(input('entre the number 1'))
b = int(input('entre the number 2'))

print('the two number avg is ',(a+b)/2)