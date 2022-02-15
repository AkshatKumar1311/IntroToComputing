print("Q1\n")

input_string=input("Enter String: ")
if " " in input_string:
    input_string=input_string.split()
dictt={} #dict for number of occurences
for i in input_string:
    if i in dictt:
        dictt[i]=dictt[i]+1
    else:
        dictt[i]=1
print("Number of Occurrences of each character/word is:")
for j in dictt:
    print(j,dictt[j])

print("\nQ2\n")

day=int(input("Day - "))
month=int(input("Month - "))
year=int(input("Year - "))

if 1<=day<=31 and 1<=month<=12 and 1800<=year<=2025 and not (month==2 and (year%4==0 and 29<day<=31 or year%4!=0 and 28<day<=31)) and not ((month in [4,6,9,11]) and day==31) :#all valid dates
    if 1<=day<=30 and (month in [1,3,5,7,8,10,12]) or 1<=day<=29 and (month in [4,6,9,11]) or 1<=day<=27 and month==2 or year%4==0 and day==28 and month==2:#normal day of month
        day=day+1
    elif day==31 and (month in [1,3,5,7,8,10,12]) or day==30 and (month in [4,6,9,11]) or day==28 and month==2 and year%4!=0 or year%4==0 and day==29 and month==2:#final day of month
        day=1
        month=month+1
    elif month==12:#last month of year
        month=1
        year=year+1
    print(f"Next Date is: {day}/{month}/{year}")
    
else:
    print("Wrong input")

print("\nQ3\n")

my_list = [3,9,10]
print("The list is ")
print(my_list)
print("The resultant tuple is :")
my_result = [(val, pow(val, 2)) for val in my_list]
print(my_result)
    
print("\nQ4\n")

#dictionary for letter grade
letter_grade={10:"A+",9:"A",8:"B+",7:"B",6:"C+",5:"C",4:"D"}
#dictionary for performance
performance={10:"Outsanding",9:"Excellent",8:"Very Good",7:"Good",6:"Average",5:"Below Average",4:"Poor"}
#taking grade point input
grade_point=int(input("Enter grade point:"))

if grade_point in range(4,11): #grade and performance are only defined for a specific range
    print(f"\nFor Grade {grade_point} Output is:\n"
          f"\nYour Grade is '{letter_grade.get(grade_point)}' and {performance.get(grade_point)}.")
else:
    print("Error")

print("\nQ5\n")

s="ABCDEFGHIJK"#full given string

for row in range(6): #as 6 rows are required
    for col in range(row): #for empty characters
        print(" ",end="")
    length=len(s)-2*row #for total characters in each row
    print(s[0:length]) #string slice is obtained till required character

print("\nQ6\n")

dic={}
i=input("Would you like to enter students?(Y/N) ")
while i=="Y":
    sid=input("Enter SID: ")
    name=input("Enter name: ")
    dic[sid]=name
    i=input("Would you like to enter more?(Y/N) ")
    
print("\nStudent Details:")
for s in dic:
    print(s,dic[s])

print("\nSorted by SID\n",dict(sorted(dic.items())))

input_sid=input("\nEnter SID for student name: ")
print(dic[input_sid])



print("\nQ7\n")

n=int(input("Number of terms of Fibonacci sequence: "))

a=0 #first term of the fibonacci sequence
b=1 #second term
c=0

if n==1:
    print(a)
else:
    while c < n:
        print(a)
        m=a+b
        a=b
        b=m
        c=c+1


print("\nQ8\n")
    

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

print("a. ",(Set1^Set2))

print("b. ",(Set1^Set2)^Set3)


Set_d=set()
for value in range(1,11):
    if value not in Set1:
        Set_d.add(value)
print("d. ",Set_d)

Set_e=set()
for value in range(1,11):
    if value not in (Set1|Set2|Set3):
        Set_e.add(value)
print("e. ",Set_e)






















    


