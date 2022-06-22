# from operator import index


# capital_cities={"Kenya":"Nairobi","Ghana":"Accra","Madagascar":"Antananarivo"}
# for key in capital_cities.keys():
#     print(f"This are the value {capital_cities [key]}")
#     # print(f" {key}'s superpower is {capital_cities[key]}.")
# # print(capital_cities.items())  


# #option 2
# capital_cities={"Kenya":"Nairobi","Ghana":"Accra","Madagascar":"Antananarivo"}
# for key,value in capital_cities.items():
#     print(f" {key}'s capital city is {capital_cities[key]}.")

##DICTIONARY COMPREHENSIONS
# from requests import get


# elements={"Hydrogen":'H',"Bismuth":"Bi","Iron":"Fe","Carbon":"C","Silicon":"Si","Helium":"He"}    
# for key in elements.values():
#  print(elements.values())

# #Write a for loop that loops over the elements dictionary you created 
# #in exercise 2, above. Print each item as “Symbol => Name” on a single line.

# for value in elements:
#     print(value,':',elements[value])
    
# for key in elements:
# #    print(key,':',elements[key])
#  [print(key,':',value) for key, value in elements.items()]


# #add Oxygen Sodium and zinc to elements dict
#firstmethod .update() keyword
# additions={"Oxygen":"O2","Sodium":"Na","Zinc":"Zn"}
# elements={"Hydrogen":'H',"Bismuth":"Bi","Iron":"Fe","Carbon":"C","Silicon":"Si","Helium":"He"}   
# elements.update(additions)
# print(elements)
 
# #second method
# #create another variable  and merge using (**) unpack operator
# elementss=dict(elements,**additions)
# print(elementss)

# ##obtaining values from keys
# print(elements["Hydrogen"])

# ##Looking up a dictionary key given its values 

#first method index()method separates lists of keys and values then get key by position of value as they correspond
# print(list(elements.keys())[list(elements.values()).index("Bi")])
# print(list(elements.keys())[list(elements.values()).index("Zn")])
# #second method dict.item() method
# def get_key(val):
#     for key,value in elements.items():
#         if val==value:
#             return key
# print(get_key("Na"))

# # [ ] The school's domain has changed from (ie.com) to (ie.org)
# # Write a program to modify the email addresses in the `records` dictionary to reflect this change

# students = {100001: ['Shaz Anota', 'anota@ie.com'], 200001: ['Speria Niwenyisiga', 'speria@ie.com'], 300001: ['Sabdio Godana', 'sabby@ie.com'], 400001: ['Yasmin Mahad', 'yasminm@ie.com'],500001: ['Sakina Noha', 'sakins@ie.com']}

# x = "anota@ie.com"
# y = x.split(".com")
# print(y)
# y = y[0] + '.org'
# # print(y)

# for key in students.keys():
#     email = students[key][1]
#     y = email.split('.com')[0]
#     students[key][1] = y + '.org'
    
# print(students)

# # [ ] You want to send a mass email to all students, so you need a list of all the email addresses in `students`
# # Write a program to extract the email addresses from the `students` dictionary and store them in a list
# students = {100001: ['Shaz Anota', 'anota@ie.com'], 200001: ['Speria Niwenyisiga', 'speria@ie.com'], 300001: ['Sabdio Godana', 'sabby@ie.com'], 400001: ['Yasmin Mahad', 'yasminm@ie.com'],500001: ['Sakina Noha', 'sakins@ie.com']}
# email = []
# for key in students.keys():
#     email.append(students[key][1])
    
# print(email)


# #Outputting student details in rows  
# Wanafunzi ={1001:['Atieno Chris','Kisumu Kenya'],2001:['Fardosa Ibrahim','Garrisa,kenya'],3001:['Sabdio Godana','Marsabit Kenya'],4001:['Yasmin Mahad','Mogadishu Somalia']}
# for id in sorted(Wanafunzi.keys()):
#     print("{0:^20s} | {1:^9d} | {2:>20s}".format(Wanafunzi[id][0], id, Wanafunzi[id][1]))

# ##contacts list dictionaries example
# my_contacts={"Mum":"0703-514-021","Brother":"0728-098-876","Bestie":"0740-145-619","Opodocuz":"0748-876-765"}
# name=input("Enter a name: ")
# number=my_contacts[name]
# print("Number is {:s}".format(number))

# name=input("Enter a name: ")
# try:
#     number = my_contacts[name]
#     print("Number is: {:s}".format(number))
# except KeyError as  exception_object:
#  print("{:s} is not in your list".format(name))

# #adding or changing a contact
# name = input("Enter a name")
# number =input("Enter a number:")
# my_contacts[name]=[number]
# print("Recently updated contact:",my_contacts)

# #Deleting a contact

# my_contacts={"Mum":"0703-514-021","Brother":"0728-098-876","Bestie":"0740-145-619","Opodocuz":"0748-876-765"}
# try:
#     number=my_contacts.pop(name)
#     print("{:s}:{:s} was removed from contacts".format(number))
# except KeyError as exception_object:
#     print("{:s} was added then deleted from your contacts".format(name))

# print("New contacts:" ,my_contacts)    

# #Updating  value of an  existing item as inputed by the user else if item is new display an error
# Stationaries ={"Exercise book":40.50,"Eraser":5.15,"Pencils":3.90,"Pen":10.00}
# item =input("Enter an item:")
# price =float(input("Enter price: "))
# if(item in Stationaries):
#     Stationaries[item]=price
# else:
#     print("Latest item!")

# # print(Stationaries.update()) #returns none as latest item entered will not be added to dictionary above method is for updating price only
# print(Stationaries)

# #testing if item has been identified by correct price
# Stationaries ={"Exercise book":40.50,"Eraser":5.15,"Pencils":3.90,"Pen":10.00}

# item = input("Please enter a item: ")

# if (item in Stationaries):
#     print("Price of {} is: ${:4.2f}".format(item, Stationaries[item]))
# elif (item not in Stationaries):
#     print("Price not in the dictionary")

# # Checking for an item by its price
# Stationaries ={"Exercise book":40.50,"Eraser":5.15,"Pencils":3.90,"Pen":10.00}

# price = float(input("Please enter an exact price: "))

# if (price in Stationaries.values()):
#     print("There is a matching stationary")
# else:
#     print("There is no stationary matching this price")


##Random out of topic question looping through two different lists and have the output in one list
x=[x for x in range(2)] 
y=[y for y in range(5)if y%2==1] 
z=[(x,y)for x,y in zip(x,y)] 
print(z)  
print(type(x),type(z))