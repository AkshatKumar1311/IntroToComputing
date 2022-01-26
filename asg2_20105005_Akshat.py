
print("Q1","\n")

input_string = "Python is a case sensitive language"
print(input_string)

print("\n(a)The length of the input string is",len(input_string))

print("\n(b)Reverse of the given input string: \n",input_string[ : :-1]) 

new_string = input_string[10:26]
print("\n(c)Store 'a case sensitive' in new string: \n ",new_string)

updated_string = input_string.replace("a case sensitive","object oriented")
print("\n(d)Updated string after replacing 'a case sensitive' with 'object oriented': \n",updated_string)

index_substring = input_string.find('a')
print("\n(e)The index of substring 'a' in the given input string: \n",index_substring)

inp_string = input_string.replace(' ', '')
print("\n(f)String after removing the white spaces from the given input string: \n",inp_string,"\n")


print("Q2")

name = "Akshat kumar"
SID = 20105005
department_name = "ECE"
CGPA = 9.9
print(f"\nHey, {name} Here!\n"
      f"My SID is {SID} \n"
      f"I am from {department_name} department and my CGPA is {CGPA}\n")


print("Q3")

a = 56
b = 10
print("\n(a)With the help of bitwise AND operator:\n",a & b)

print("\n(b)With the help of bitwise OR operator:\n",a | b)

print("\n(c)With the help of bitwise XOR operator:\n",a ^ b)

print("\n(d)")
print("Bitwise Left shift a with 2 bits: \n",a << 2)
print("Bitwise Left shift b with 2 bits: \n",b << 2)

print("\n(e)")
print("Bitwise Right shift a with 4 bits: \n",a >> 4)
print("Bitwise Right shift b with 4 bits: \n",b >> 4,"\n")

print("Q4")

num1 = float(input("\nEnter the first number:\n"))
num2 = float(input("Enter the second number:\n"))
num3 = float(input("Enter the third number:\n"))

if(num1 > num2) and (num1 > num3):
    print(f"First number i.e. {num1} is the greatest.")
elif (num2 > num1) and (num2 > num3):
    print(f"Second number i.e. {num2} is the greatest.")
else:
    print(f"Third number i.e. {num3} is the greatest.\n")

print("Q5")

input_string = input("\nEnter the string:\n")
print("\nThe word 'name' is present in the entered string or not (Yes or No)?")

if "name" in input_string:
    print("Yes \n")
else:
    print("No \n")

print("Q6 " ,"\n")

side1 = int(input("Enter the first side of a triangle:\n"))
side2 = int(input("Enter the second side of a triangle:\n"))
side3 = int(input("Enter the third side of a triangle:\n"))
print("\nThe given input lengths can form a triangle or not (Yes or No)?")

sum1 = side1 + side2
sum2 = side2 + side3
sum3 = side3 + side1

if side1 > sum1 or side1 > sum2 or side1 > sum3:
    print("No")
elif side2 > sum1 or side2 > sum2 or side2 > sum3:
    print("No")
elif side3 > sum1 or side3 > sum2 or side3 > sum3:
    print("No")
else:
    print("Yes")
