print ("\n\tWelcome to Bon Appetite")
print ("\t------------------------\n")
print ("Please have a look at our menu and order with dish number. Remember you can order at max 5 dishes !" + 
		"Keep pressing dish number and enter after that")

Menu = {1: ['European', 123], 
		2: ['Mediterranean', 245],
		3: ['North Indian', 354],
		4: ['BBQ', 1200],
		5: ['Continental', 1243], 
		6: ['Mediterranean', 523],
		7: ['Modern Indian', 343],
		8: ['Asian', 533],
		9: ['Japanese', 103],
		10:['Thai',  32],
		11:['Pan Asian', 234]
		}

max_length = 40
# print (Menu)
# print ("\n")

# print (Menu[6])
# for i in Menu.items():
# 	print (i)
s = '\tMenu\t\n'
# print (s)

for k,v in Menu.items():
	to_print = str(k) + "\t|" + v[0] + " "*(max_length-len(v[0]))+ "|" + str(v[1])
	s += to_print + "\n"
	print (to_print)
    
# print (s)
    
attempts = 0
orders = []; amts = []
amount = 0

print ("\nEnter the dish number. Enter 0 if you want to finish ordering")
s += "\n\n----------------Bill-----------------------------\n"
while attempts < 5:	
	try:
		order = int(input("Dish: "))
		if not order:
			break
		elif order not in range(11):
			raise ValueError
		else:
			orders.append(Menu[order][0])
			amts.append(Menu[order][1])
			amount = amount + Menu[order][1]
			attempts += 1
	except:
		print ("Please don't play with me ! Enter a number only.")
        
# print (s)

print ("You ordered", orders)
print ("Your total= ",amount)

for i, order in enumerate(orders):
	s += order + " "*(max_length-len(order)) + str(amts[i]) + "\n"

print(s)
    
s += "Your total= " + str(amount)

# print (s)

with open("Bill.txt", "w") as c:
	c.write(s)
    