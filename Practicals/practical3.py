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
"""scores = [80, 39, 79, 81, 79, 70, 84, 57, 66, 86]
print("The 10 Students scored", scores)
for i in range(len(scores)):
 if 80 <= scores[i]:
  print("Scores that qualify for 'A' grade are:", sorted(scores[i]))"""

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

#Q12
'''
open_ports = input("Enter the service:port found to be open separated by '|': ")

services_ports = open_ports.replace(" ", "").split("|")

print("\nThese are the ports found and their corresponding services:")
for item in services_ports:
    service, port = item.split(":")
    print(f"{service} on port {port}")

s = input('
 1) Search for open port
 2) Search for service running 
 3) Update Dictionary
 Please enter request: ')
if(s == '1'):
    open = []
    s1 = input("Enter the port number: ")
    
    for item in services_ports:
        service, port = item.split(":")
        if(port==s1):
          open.append(port)
    if(len(open)):
      print("Port", open, "is open")
    else:
      print(f"Sorry, Port {s1} is not open")
          
elif(s == '2'):
    open = []
    s2 = input("Enter the service name: ")
    for item in services_ports:
     service, port = item.split(":")
     if(service == s2):
      open.append(service)
     
    if(len(open)):
     print("service",open, "is open")
    else:
     print(f"Service {s2} is not running")

    

elif(s == '3'):
    s3 = input('Enter service:port: ')
    services_ports.append(s3)
    print(services_ports)
'''

#Q13
'''os = ['Windows10', 'Debian', 'Ubuntu','Redhat']
portlist = {25:"SMTP", 80:"HTTP", 443:"HTTPS", 23:"TELNET"}

for num, osPort in list(enumerate(zip(os,portlist),1)):
  osPort = list(osPort)
  print(f'{num}: Ping port {osPort[1]} on {osPort[0]} OS for {portlist[osPort[1]]}')'''


# Q14
'''def read_file(f_fn):
    # create an empty dictionary to store the menu items
    menu = {}

    # open the file for reading
    with open(f_fn, "r") as fn:
        # read each line of the file
        for line in fn:
            # split the line on the comma character to separate the
            # dish name and price
            dish, price = line.strip().split(",")

            # add the dish and price to the menu dictionary
            menu[dish] = price
    return(menu)
    
def display_menu(menu):
  print(f'No\tItem\t\tPrice')
  

fn = './spams_menu.txt'

dict_menu = read_file(fn)
print('SP Automated Menu System')
display_menu(dict_menu) '''

#Q15
'''my_dict = {'hospital': {'AMK': {'Orthopaedic': {}, 'Heart Centre': {'Ward-33': {'bed-1': {"patient_id": "id-1",
      "patient_name": "ChinChiaHo",
      "patient_age": 35,
      "patient_gender": "M",
      "patient_weight": 63.5,
      "patient_height": 1.72,
      "patient_date_admitted": "2021-10-01",
      "patient_date_discharged": "2021-10-01"}
, 'bed-2':{"patient_id": "id-2",
      "patient_name": "MaSieHoh",
      "patient_age": 38,
      "patient_gender": "F",
      "patient_weight": 53.5,
      "patient_height": 1.55,
      "patient_date_admitted": "2021-10-01",
      "patient_date_discharged": "2021-10-01"}}, 'Ward-55':{}}}, 'SGH':{}}}

inner_dict = my_dict['hospital']
inner_dict_2_AMK = inner_dict['AMK']
inner_dict_2_SGH = inner_dict['SGH']
inner_dict_3_o = inner_dict_2_AMK['Orthopaedic']
inner_dict_3_h = inner_dict_2_AMK['Heart Centre']
inner_dict_4_ward1 = inner_dict_3_h['Ward-33']
inner_dict_4_ward2 = inner_dict_3_h['Ward-55']
inner_dict_5_bed1 = inner_dict_4_ward1['bed-1']
inner_dict_5_bed2 = inner_dict_4_ward1['bed-2']



print('Bed no\tID\tName\t\tAge\tGender\tWeight\tHeight\tDateAdmitted\tDateDischarged')

print('1', end='\t')
for patient_stuff, patient_stats in inner_dict_5_bed1.items():
  print(f'{patient_stats}', end='\t') '''
   
'''obj = [{'name': 'yuliang', 'sex': 'male'}, {'name': 'zavier','sex':'female'}]

for i in range(len(obj)):
 d = obj.pop(0)

 d.update({'name': d.pop('name'), 'gender': d.pop('sex')})

 obj.append(d)

for i, item in enumerate(obj):
    print(f"{i + 1}:")
    print(f"Name: {item['name']}")
    print(f"Gender: {item['gender']}")
    if(item['gender'] == 'female'):
        print('no rights') '''


#MOCK MST Q3
'''def rate(x):
  if no_units <= 500:
      return no_units*0.01*x
  elif no_units < 1001:
      return (no_units - 500)*0.02*x + 500*0.01*x
  elif no_units > 1000:
      return (500*0.01 + 500*0.02 + (no_units-1000)*0.03)*x



hdb_factor = 1
condo_factor = 1.1
landed_factor = 1.2



counter = 0
while counter == 0:
    dwelling_type = input("Choose: ")
    no_units = int(input("Enter your number of units: "))
    pay_amt = 0
    if dwelling_type == '1':
      pay_amt = rate(hdb_factor)
      print(f"Total amount to pay is: ${pay_amt:.2f}")
    elif dwelling_type == '2':
      pay_amt = rate(condo_factor)
      print(f"Total amount to pay is: ${pay_amt:.2f}")
    elif dwelling_type == '3':
      pay_amt = rate(landed_factor)
      print(f"Total amount to pay is: ${pay_amt:.2f}") '''



