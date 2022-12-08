print("***********************************" + "\n" + "ST2414 PSEC Practical 2" + "\n" + "***********************************")

#Q1
"""
try:
    number = int(input('Enter a number: '))
    if  number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
except ValueError:
    print("You did not enter a number ")

#Q2
try:
    number = int(input('Enter a number: '))
    number2 = int(input('Enter another number: '))
    if number > number2:
        print(f"{number} is bigger! ")
    elif number==number2:
        print(f"{number} and {number2} is the same! ")
    else:
        print(f"{number2} is bigger! ")
except ValueError:
    print("You did not enter a number")

Q3
years = int(input('Enter number of years in service: '))
salary = int(input('Enter current salary: $'))
    
if years < 10:
        if salary<1000:
            increment=100
        elif salary<2000:
            increment=200
        else:
            increment=300
else:
        if salary<1000:
            increment=200
        elif salary<2000:
            increment=300
        else:
            increment=400
print(f'Your increment is {increment}') """

#Q4

"""starting = int(input('Pls enter a starting number: '))
ending = int(input('Pls enter an ending number: '))

if starting < ending:
    for x in range(starting, ending, +2):
      print(x, end="\t")
    print()

else:
   for x in range(ending, starting, -2):
    print(x, end="\t")
print()
""" 

#Q5
"""starting = int(input('Pls enter a starting number: '))
ending = int(input('Pls enter an ending number: '))

if starting < ending:
    for x in range(starting+1, ending, +2):
      print(x, end="\t")
    print()

else:
   for x in range(ending+1, starting, -2):
    print(x, end="\t")
print()
"""
#Q6

"""
sum = 0
while True:
    number=input("Pls enter a number or Q to stop: ")
    if number.isnumeric()==False and number.upper()!="Q":
        print("Please enter a valid number. ")
    elif number.upper()=="Q":
        break
    else: 
        sum += int(number)
        print(f"Current total is {sum}")
print(f"Final sum is {sum}")

#Q7

while True:
    try:
        number=int(input('Please enter an integer: '))
        print("Great, you have successfully entered an integer! ")
        break
    except ValueError:
        print("No valid integer! Please try again... ")


#Q8

try:
    number = int(input('Enter a number: '))
    if  number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
except ValueError:
    print("You did not enter a number ")

#Q9
def func1():
    try:
        number = int(input('Enter a number: '))
        if  number%2==0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    except ValueError:
        print("You did not enter a number ")

def func2():
    try:
        number = int(input('Enter a number: '))
        number2 = int(input('Enter another number: '))
        if number > number2:
            print(f"{number} is bigger! ")
        elif number==number2:
            print(f"{number} and {number2} is the same! ")
        else:
            print(f"{number2} is bigger! ")
    except ValueError:
        print("You did not enter a number")

def func3():
    sum = 0
    while True:
        number=input("Pls enter a number or Q to stop: ")
        if number=="Q":
            break
        else: 
            sum += int(number)
            print(f"Current total is {sum}")
    print(f"Final sum is {sum}")

def func4():
    x = int(input('Pls enter a starting number: '))
    y = int(input('Pls enter an ending number: '))
    string = ''
    for i in range(x,y+1):
        
        if x%2==0:
            string += str(x)+"\t"
        x+=1
    print(string)   

def menu():
    choice = input("1. Determine odd or even \n2. Determine bigger number \n3. Find sum of numbers \n4. Display even numbers, inclusive \nEnter a choice: ")
    if choice=='1':
        func1()
    elif choice=='2':
        func2()
    elif choice=='3':
        func3()
    elif choice=='4':
        func4()
    else:
        print('Pls enter a valid choice')
menu()
"""

