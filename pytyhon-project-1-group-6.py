"""
1)	Build a program that:
•	Displays a list of snacks and drinks with item numbers and prices. 
•	Ask the user to choose items by number in a loop.
•	 Keeps track of selected items and their prices.
•	Ends when the user types "done".
•	Finally prints a receipt showing: List of selected items with prices and total cost
"""
# Import datetime class from datetime module
#Used for to get the current date in the reciept
from datetime import datetime

# # Import datetime class from datetime module
# #Used for to get the current date in the reciept
# from datetime import datetime

# snacks = {1:["Doritos", 2.99],
#           2:["Cheetos", 3.99],
#           3:["Cheez-its", 5.99],
#           4:["Beef Jerky", 4.99], 
#           5:["Oreos" , 6.99],
#           6:["M&M's", 6.59], 
#           7:["Snickers", 7.99],
#           8:["Rice Krispie Treats", 8.99],
#           9:["Granola Bars", 5.99], 
#           10:["Pretzel/Chex Mix", 9.99]}  
# drinks = {1:["Water", 1.99],
#           2:["Tea", 2.69],
#           3:["Coffee", 5.99],
#           4:["Apple Juice", 5.99],
#           5:["Orange Juice", 4.99],
#           6:["Coca Cola", 2.99],
#           7:["Green Tea", 3.99],
#           8:["Ginger Tea", 3.99],
#           9:["Nectar", 6.99],
#           10:["Ginger ale", 3.99]}  #

# print("Item Number:    Price:     Snacks")
# print("----------------------------------------")
# for k,v in snacks.items():
#     print(f"Item #{k}          {v[1]}      {v[0]}")
# print("----------------------------------------")
# print("From above snacks display, please select the Item#. If you don't any of the tems listed, type 'done' : ")
# snacks_selected = {} #Tracks of selected snacks and their prices.
# while True:
#     item_number = input("Please select Item#1. Example: 1,2, 3. If you are done selecting, type 'done' : ")
#     if(str(item_number).lower() == "done"):
#         break  #Exit from the loop
#     else:
#         snacks_selected[int(item_number)] = snacks[int(item_number)]

# print("Item Number:    Price:     Drinks")
# print("----------------------------------------")
# for k,v in drinks.items():
#     print(f"Item #{k}          {v[1]}      {v[0]}")
# print("----------------------------------------")
# print("From above drinks display, please select the Item#. If you don't any of the tems listed, type 'done' : ")
# drinks_selected = {} #Tracks of selected drinks and their prices.
# while True:
#     item_number = input("Please select Item#1. Example: 1,2, 3. If you are done selecting, type 'done' : ")
#     if(str(item_number).lower() == "done"):
#         break
#     else:
#         drinks_selected[int(item_number)] = drinks[int(item_number)]

# now = datetime.now()  #Get the curret time
# print(f"======Receipt=======" )
# print("Here are the snacks selected")
# print("Item Number:    Price:     Drinks")
# print("----------------------------------------")
# price = 0.0  #used to get the total price
# for k,v in snacks_selected.items(): #Enumerating the selected snacks from temp tracked dictionary
#     print(f"Item #{k}          {v[1]}      {v[0]}")
#     price += v[1]   #Summing up the price for snacks
# print("----------------------------------------")

# print("Here are the drinks selected")
# print("Item Number:    Price:     Drinks")
# print("----------------------------------------")
# for k,v in drinks_selected.items(): #Enumerating the selected drinks from temp tracked dictionary
#     print(f"Item #{k}          {v[1]}      {v[0]}")
#     price += v[1] #On top of the snacks, it adds the price of erach drinks selected
# print("----------------------------------------")

# price = round(price*1.06, 2)  #Adding 6% gov tax from the total price value
# print(f"Total Price with 6% gov tax included:= ${price}")
# print(f"Date: {now}" )   #Printing the current time

"""
2)	Write a program that:
•	Has a predefined dictionary of groceries with prices.
•	Lets the user "add" items by typing their names.
•	For each valid item, asks for the quantity.
•	Keeps adding to the cart until the user types "checkout".
•	Displays a final bill: each item, quantity, subtotal, and total.
"""
# gorceriies_dictionary = {"Spinach":4.99,
#                           "Kale":3.99,
#                           "Arugula":5.99,
#                           "Salad Greens":4.99,
#                           "Broccoli":4.59,
#                           "Sweet Potatos":2.99,
#                           "Carrots":3.99,
#                           "Onion":2.99,
#                           "Apple":6.99,
#                           "Garlic":4.99
#                          }

# print("Price      Item")
# print("----------------------------------------")
# for k,v in gorceriies_dictionary.items():
#     print(f"${v}      {k}")
# print("----------------------------------------")

# # print("----------------------------------------")
# # print("From above groceries list, please type their name. If you don't any of the tems listed, type 'done' : ")
# cart ={}
# while True:
#     grocery_name = input("Please select groceries name from the list: Example: Spinach,Kale etc: If you are done selecting, type 'checkout' : ")
#     if(str(grocery_name).lower() == "checkout"):
#         break
#     else:
#         quantity = int(input(f"Please Enter quantity for: {grocery_name}==>"))
#         cart[grocery_name.title()] = quantity

# print("Here are the selection")
# print(cart)

# Subtotal = {}
# total = 0.0
# for k,v in cart.items():
#     #price = 0.0
#     for key, value in gorceriies_dictionary.items():
#         if k==key:
#             #price = round(value*v*1.06, 2)  #Including goverment tax
#             Subtotal[k] = round(value*v*1.06, 2)
#             total+= Subtotal[k]

# print("Here are the selection with subtotal:")

# print("Subtotal      Quantity        Item")
# print("----------------------------------------")
# for itm, qnt in cart.items():
#     for k,subt in Subtotal.items():
#         if itm == k:
#             print(f"${subt}           {qnt}             {itm}")

# print(f"Total = ${round(total, 2)}")

# print("----------------------------------------")


"""
3)	Build a to-do list manager that
•	Allows users to add tasks with priorities (e.g., "Buy milk - high").
•	Lets them view the current list, delete tasks by number, and mark tasks as complete.
•	Keeps looping until the user types "exit".
•	Shows a summary at the end: number of completed tasks vs pending.
"""
# to_do_list = {}   #{task:priority}  #Priority: High, Midium, Law
# complted_tasks = {} #Tracks completed tasks
# pending_tasks = {} #Track pending tasks
# i = 1
# while True: #Building a to-do list manager
#     track = []
#     #Allows users to add tasks with priorities
#     get_to_do_list = input("Please Enter things to do? to end, type 'exit' : ")
#     if(get_to_do_list.lower() == 'exit'):
#         break
#     else:
#         set_priority =input("What is the Priority?[High, Medium, Low] : ")
#         track.append(get_to_do_list)
#         track.append(set_priority)
#         #to_do_list[get_to_do_list] = set_priority
#         to_do_list[i] = track  
#         i+=1
# #Viewing the current list
# print("------------------------------------------")
# print("-------------To Do Lists------------------")
# print("------------------------------------------")
# print("No.:  Priorities:     To Do List")
# print("------------------------------------------")
# for k,v in to_do_list.items():
#     print(f"{k}          {v[1]}          {v[0]}")
# print("----------------------------------------")

# print("Working on To-do-list....")
# print("In progeess...")

# for k,v in to_do_list.items():
#     status = input(f"Have you completed No. {k}, which is {v[0]} with priority {v[1]} -->[y/n] : ")
#     if status.lower() =='y':
#         complted_tasks[k] = v
#     else:
#         pending_tasks[k] = v


# #Viewing the completed tasks
# print("------------------------------------------")
# print("-------------Completed Tasks--------------")
# print("------------------------------------------")
# print("No.:  Priorities:     To Do List")
# print("------------------------------------------")
# for k,v in complted_tasks.items():
#     print(f"{k}          {v[1]}          {v[0]}")
# print("----------------------------------------")


# #Viewing the pending tasks
# print("------------------------------------------")
# print("-------------Pending Tasks----------------")
# print("------------------------------------------")
# print("No.:  Priorities:     To Do List")
# print("------------------------------------------")
# for k,v in pending_tasks.items():
#     print(f"{k}          {v[1]}          {v[0]}")
# print("----------------------------------------")

# #Shows a summary at the end: number of completed tasks vs pending.
# print("------------------------------------------")
# print("---number of completed tasks vs pending---")
# print("------------------------------------------")
# print("Total Number of Completed Tasks: ", len(complted_tasks) )
# print("Total Number of Pending Tasks: ", len(pending_tasks) )
# print("------------------------------------------")


"""
4)	 Movie Ticket Booking Simulation
-	Simulate a movie theater booking system that:
•	Shows a list of available movie titles, showtimes, and seat prices.
•	Asks the user to choose a movie and number of tickets.
•	Confirms total price and asks if they want to book another movie.
•	Ends when they say "no" and displays total bookings and cost.
"""
# list_of_movies_avalable = {  #{"title","Showtime", "price", ]}
#     1:["Titanic","Monday 9PM-10:15Pm          ", 15],        #space is used for indentetion during display
#     2:["Titanic","Monday 10PM-11:15Pm         ", 20],        #space is used for indentetion during display
#     3:["Titanic","Friday 10PM-11:15Pm         ", 30],        #space is used for indentetion during display
#     4:["       Pay it forward","Saturday 9PM-10:15Pm ", 20], #space is used for indentetion during display
#     5:["       Pay it forward","Saturday 10PM-11:15Pm", 30]  #space is used for indentetion during display
# }  

# #Shows a list of available movie titles
# print("--------------------------------------------------------------")
# print("-------------List of available movies-------------------------")
# print("--------------------------------------------------------------")
# print("No.:  price:   Showtime:                        Title")
# print("--------------------------------------------------------------")
# for k,v in list_of_movies_avalable.items():
#     print(f"{k}     ${v[2]}      {v[1]}     {v[0]}")
# print("--------------------------------------------------------------")

# avaiable_seats = ["A1", "A2", "A3", "A4", "A5", "A6", "A7",
#                   "B1", "B2", "B3", "B4", "B5", "B6", "B7",
#                   "C1", "C2", "C3", "C4", "C5", "C6", "C7",
#                   "D1", "D2", "D3", "D4", "D5", "D6", "D7"
#                   ]

# ###When seat is occupied, update the SEAT as X[1-7]
# #Everytime there is a booking, update the seat to X[1-7] ON seat_status
# seat_status =  ["A1", "A2", "A3", "A4", "A5", "A6", "A7",
#                 "B1", "B2", "B3", "B4", "B5", "B6", "B7",
#                 "C1", "C2", "C3", "C4", "C5", "C6", "C7",
#                 "D1", "D2", "D3", "D4", "D5", "D6", "D7"
#                 ]

# # select_movie = input("From above list, please select movie: Example 1,2 etc. Type 'exit' to quit")
# # qountity = input("How many tickets do you want?")
# total_available_seat = 28
# total_price = 0.0
# sold_seat = 0

# counter = 0  #helps to exits outer loop before asking for another movies selection

# while True:
#     while True:
#         counter +=1
#         select_movie = input("From above list, please select movie: Example 1,2 etc. Type 'exit' to quit : ")
 
#         if select_movie =='exit':
#             counter = 0
#             break
#         else:
#             qauntity = int(input("How many tickets do you want? :"))
#             if(total_available_seat - qauntity <  0):
#                 print(f"We only have {total_available_seat} seat(s) left")
#                 qauntity = int(input("How many tickets do you want based on the avaialable seat? :"))
    
#             total_available_seat -= qauntity
#             total_price += round(list_of_movies_avalable[int(select_movie)][2]*qauntity*1.06, 2)  #including tax
#             sold_seat +=qauntity
#             print("----------------Please select seats----------------------")
#             for k in avaiable_seats:
#                 if int(k[1]) % 7 != 0:
#                     print(k, end ='\t')
#                 else:
#                     print(k, end ='\n')
#             print("----------------Please select seats----------------------")
            
#             #Updating the sold seats with X !!!
#             j = 0
#             while j < qauntity:
#                 select_seat = input(f"From above list, please select seat(s) for ticket #{j+1} : Example A1,B2: ").upper()
#                 indx = seat_status.index(select_seat)
#                 #only changing the first seat character to X. 
#                 #This allows to use: int(k[1]) % 7 != 0:
#                 seat_status[indx] = "X" + select_seat[1] #Concatinating
#                 j+=1
#             print(f"--------Seat Map for {list_of_movies_avalable[int(select_movie)][0]} : {list_of_movies_avalable[int(select_movie)][1]}---")
#             for k in seat_status:
#                 if int(k[1]) % 7 != 0:
#                     if k[0] =='X':
#                         print("XX", end ='\t')
#                     else:
#                         print(k, end ='\t')

#                 else:
#                     if k[0] =='X':
#                         print("XX", end ='\n')
#                     else:
#                         print(k, end ='\n')
#             print(f"--------Seat Map for {list_of_movies_avalable[int(select_movie)][0]} : {list_of_movies_avalable[int(select_movie)][1]}---")
#             #Reset seats for the next movies:

#             seat_status =  ["A1", "A2", "A3", "A4", "A5", "A6", "A7",
#                             "B1", "B2", "B3", "B4", "B5", "B6", "B7",
#                             "C1", "C2", "C3", "C4", "C5", "C6", "C7",
#                             "D1", "D2", "D3", "D4", "D5", "D6", "D7"
#                             ]
#     if counter == 0: #exits outer loop before asking for another movies selection
#         break
#     boolean = input("Do you want to book another movies? [y/n]: ")
#     if boolean.lower() == 'n':
#         break

# print(f"The total number of ticket booked : {sold_seat}")
# print(f"The total  sale with gov tax  is  : ${round(total_price,2)}")


"""
5)	Create a basic quiz game that:
•	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
•	Ask the user each question and records their answers.
•	At the end, displays:
o	The user's score (e.g., 7/10)
o	Correct answers for any questions they got wrong
"""
quiz= [{"Can a LIST have duplicate values in python? [Yes/No] ":"Yes"}, 
       {"Can a SET have duplicate values in python? [Yes/No] ": "No"}, 
       {"What is SQL stands for?": "Structured Query Language"},
       {"Can a key in a dictionary be duplicated in python?[Yes/No] ":"No"},
       {"Can we have multiple keys referencing to the same value without issue in dictionary? [Yes/No] ":"Yes"}]
assesment = []

correct_answer = []
for i in range(5):
    for k,v in quiz[i].items():
        print(f"{k}")
        answer = input("What is your answer? ")
        if answer.lower() == v.lower():
            assesment.append(1)
        else:
            assesment.append(0)
            correct_answer.append({k:v})
sum = 0
for i in range(len(assesment)):
    sum +=assesment[i]
print("----------------------------")
print(f"Your score:  {sum} out of 5")
print("----------------------------")
print()
print("Here is the correct answers for the questions you got wrong")
print("-----------------------------------------------------")
for i in range(len(correct_answer)):
    for k,v in correct_answer[i].items():
        print(f"{k} ==> {v}")
print("-----------------------------------------------------")
