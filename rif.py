employees = ['Bob','Joe','Bill','Mike','Steve','Matt']
headcount = len(employees)
rif = input("Your headcount is " + str(headcount) + ". Who is to be terminated? ")
# confirm = input("We need to terminate " + rif + ", is that correct? Y or N. \n")
# if confirm == 'Y':
# 	print("Ok. We will terminate " + rif + ".")
# else:
# 	print("Ok. He can stay.")
for x in employees:
	if x == rif:
		continue
	print(employees)


		
