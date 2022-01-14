#program 1

#average of three numbers taken from user

print("Q1 " ,"\n")
num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
num3=int(input("Enter number 3 "))

Sum = num1 + num2 + num3    #sum of given numbers
avg  = Sum / 3              #average of given numbers

print("Sum of given numbers is ", Sum,)
print("Average of given numbers is ", avg ,'\n')

#program 2

#calculating tax in dollars

print("Q2 ",'\n')
print("All values are to be entered in dollars")
gross_income = float(input("Enter your gross income $"))
dependents = int(input("Enter number of dependents "))

tax_rate = 0.2
standard_deduction = 10000
dependent_deduction = 3000

taxable_income = (gross_income - standard_deduction - (dependent_deduction*dependents))
tax = taxable_income*tax_rate
print("The tax comes out to be $", tax,'\n') 

#program 3

#data entry of student

print("Q3 ",'\n')
print("Student = [sid, name, gender, course, cgpa]")
sid = int(input("Enter your SID "))
name = input("Enter your name ")
gender = input("Enter your gender 'M', 'F', 'U' for Male, Female, Unknown ")
course = input("Enter your course name ")
cgpa = float(input("Enter your cgpa "))
student = [sid, name, gender, course, cgpa]   #converting data provided by user into a list
print("Student info ", student, '\n')

#program 4

#getting marks of 5 students and display them in sorted manner.

print("Q4",'\n')

#taking input from user
a = int(input("Enter marks of student 1 "))
b = int(input("Enter marks of student 2 "))
c = int(input("Enter marks of student 3 "))
d = int(input("Enter marks of student 4 "))
e = int(input("Enter marks of student 5 "))
#converting input data into list
marks = [a,b,c,d,e]
print("marks of 5 students are ", marks)

#sorting the list in asecending and descending order
asc = marks.sort()
print("Marks in ascending order ", marks)

desc = marks.sort(reverse = True)
print("Marks in descending order ", marks, '\n')

#program 5

print("Q5", '\n')
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The provided list is ", color, '\n')

#removing the 4th term and returning modified list
color.pop(3)
print("The first modified list  is color a =", color)

#replacing 'Black' and 'Pink' with 'Purple'
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print("The second modified list is color b =", color2)
