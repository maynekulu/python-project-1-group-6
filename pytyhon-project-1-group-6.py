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

snacks = {1:["Doritos", 2.99],
          2:["Cheetos", 3.99],
          3:["Cheez-its", 5.99],
          4:["Beef Jerky", 4.99], 
          5:["Oreos" , 6.99],
          6:["M&M's", 6.59], 
          7:["Snickers", 7.99],
          8:["Rice Krispie Treats", 8.99],
          9:["Granola Bars", 5.99], 
          10:["Pretzel/Chex Mix", 9.99]}  
drinks = {1:["Water", 1.99],
          2:["Tea", 2.69],
          3:["Coffee", 5.99],
          4:["Apple Juice", 5.99],
          5:["Orange Juice", 4.99],
          6:["Coca Cola", 2.99],
          7:["Green Tea", 3.99],
          8:["Ginger Tea", 3.99],
          9:["Nectar", 6.99],
          10:["Ginger ale", 3.99]}  #

print("Item Number:    Price:     Snacks")
print("----------------------------------------")
for k,v in snacks.items():
    print(f"Item #{k}          {v[1]}      {v[0]}")
print("----------------------------------------")
print("From above snacks display, please select the Item#. If you don't any of the tems listed, type 'done'")
snacks_selected = {} #Tracks of selected snacks and their prices.
while True:
    item_number = input("Please select Item#1. Example: 1,2, 3. If you are done selecting, type 'done'")
    if(str(item_number).lower() == "done"):
        break  #Exit from the loop
    else:
        snacks_selected[int(item_number)] = snacks[int(item_number)]

print("Item Number:    Price:     Drinks")
print("----------------------------------------")
for k,v in drinks.items():
    print(f"Item #{k}          {v[1]}      {v[0]}")
print("----------------------------------------")
print("From above drinks display, please select the Item#. If you don't any of the tems listed, type 'done'")
drinks_selected = {} #Tracks of selected drinks and their prices.
while True:
    item_number = input("Please select Item#1. Example: 1,2, 3. If you are done selecting, type 'done'")
    if(str(item_number).lower() == "done"):
        break
    else:
        drinks_selected[int(item_number)] = drinks[int(item_number)]

now = datetime.now()  #Get the curret time
print(f"======Receipt=======" )
print("Here are the snacks selected")
print("Item Number:    Price:     Drinks")
print("----------------------------------------")
price = 0.0  #used to get the total price
for k,v in snacks_selected.items(): #Enumerating the selected snacks from temp tracked dictionary
    print(f"Item #{k}          {v[1]}      {v[0]}")
    price += v[1]   #Summing up the price for snacks
print("----------------------------------------")

print("Here are the drinks selected")
print("Item Number:    Price:     Drinks")
print("----------------------------------------")
for k,v in drinks_selected.items(): #Enumerating the selected drinks from temp tracked dictionary
    print(f"Item #{k}          {v[1]}      {v[0]}")
    price += v[1] #On top of the snacks, it adds the price of erach drinks selected
print("----------------------------------------")

price = round(price*1.06, 2)  #Adding 6% gov tax from the total price value
print(f"Total Price with 6% gov tax included:= ${price}")
print(f"Date: {now}" )   #Printing the current time
"""
2)	Write a program that:
•	Has a predefined dictionary of groceries with prices.
•	Lets the user "add" items by typing their names.
•	For each valid item, asks for the quantity.
•	Keeps adding to the cart until the user types "checkout".
•	Displays a final bill: each item, quantity, subtotal, and total.
"""
# I am working on this project

"""
3)	Build a to-do list manager that
•	Allows users to add tasks with priorities (e.g., "Buy milk - high").
•	Lets them view the current list, delete tasks by number, and mark tasks as complete.
•	Keeps looping until the user types "exit".
•	Shows a summary at the end: number of completed tasks vs pending.
"""

"""
4)	 Movie Ticket Booking Simulation
-	Simulate a movie theater booking system that:
•	Shows a list of available movie titles, showtimes, and seat prices.
•	Asks the user to choose a movie and number of tickets.
•	Confirms total price and asks if they want to book another movie.
•	Ends when they say "no" and displays total bookings and cost.
"""

"""
5)	Create a basic quiz game that:
•	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
•	Ask the user each question and records their answers.
•	At the end, displays:
o	The user's score (e.g., 7/10)
o	Correct answers for any questions they got wrong
"""

