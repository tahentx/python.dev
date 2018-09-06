# Capture PPA rate from user
budget = int(input("What does it cost to roll a truck?"))
ppaRialto = int(input("What is the PPA rate (please enter whole units?"))/100
print(ppaRialto)
def energy_loss(ppa):
	loss = ppa * ppa
	return loss

lost_energy = energy_loss(ppaRialto)
print("The lost energy for Rialto is " + str(lost_energy))


# while cost > daily_loss_compound:
# 	daily_loss_compound += daily_loss_compound
# 	print(daily_loss_compound)
	# if cost == ppa_rate:
	# break
	# print("It makes economic sense to roll a truck.")