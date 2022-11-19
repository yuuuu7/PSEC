#Q1
""" port = str(input("Please enter ports that were found to be open '|' \n"))
port2 = str(input("Please input port number for your 'service': "))

port = port.split(sep="|")
string = f"Sorry port {port2} is closed! Pls choose from {port} "
for i in range(0,len(port)):
    if port[i]==port2:
        string = f"Yes port {port2} is open! "
        break
print(string) """

#Q2
""" food = str(input("dishes: ")).strip('').split(',')
food2 = str(input("food: ")).replace(' ', '')
arr = []
for item in food:
    if food2.lower() in item.replace(' ', '').lower():
        arr.append(item)
if(len(arr)!=0):
    print(f"Yes, we serve the following: {arr}")
else:
    for item in food:
        arr.append(item)
    print(f"No, please choose from the following: {arr}") """

#Q3
""" def find_string(f_s1, f_s2):
  if f_s1 in f_s2:
    return bool
  
s1 = 'ox'
s2 = 'the quick brown fox'
bool = find_string(s1, s2) # returns True if s1 in s2
if bool:
  print(True)
else:
  print(False) """

#Q4
""" def find_string(f_s1,f_s2):
  if f_s1 in f_s2:
    pos = s2.index(s1)
    return pos
  elif f_s1 not in f_s2:
    pos = -1
    return pos

s1 = 'qui'
s2 = 'the quick brown fox'
pos = find_string(s1, s2)
if pos == -1:			# s1 in s2 at index 4
  print('Not found')
else:
  print('Found at index: ', pos) """



#Q5
"""
def replace_char(f_c,f_s2,pos):
    f_s2 = f_s2[:pos] + f_c
    return f_s2  

c = 'i'
s = 'kristy'
s = replace_char(c,s,5)
print(s)	# output = 'kristi'
"""

#Q6
""" def replace_substr(f_s1,f_s2,pos):
  if f_s1 not in f_s2:
    f_s2 = f_s2.replace(f_s2[pos], f_s1)
    return f_s2

s1 = 'lazy'
s2 = 'the quik brown fox'
s = replace_substr(s1,s2,4)
print(s) 	# output = the lazy brown fox """

#Q7a
scores = [80, 39, 79, 81, 79, 70, 84, 57, 66, 86]
print("The 10 Students scored", scores)
for i in range(len(scores)):
 if 80 <= scores[i]:
  print("Scores that qualify for 'A' grade are:", sorted(scores[i]))

#Q7b

#Q9

"""import random
 
def random_list(length, min=0):
    list = []
    for i in range(0, length):
        list.append(random.randint(min,9+min))
    return list
for i in range(3):
  list = random_list(10) # the second argument is optional, default is 0
  print(list) """

#Q10a


""" def fibs(n):
  result = [0, 1]
  while len(result) < n:
   num = result[len(result) - 1] + result[len(result) - 2]
   result.append(num)
  return result

print(fibs(5)) """

