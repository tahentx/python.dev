employees = ['Bob','Joe','Bill','Mike','Steve','Matt']
rif = input("Who is terminated? ")
confirm = input("We need to terminate " + rif + ", is that correct? Y or N. \n")
if confirm == 'Y':
	print("Ok. We will terminate " + rif + ".")
else:
	print("Ok. He can stay.")