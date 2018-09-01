cost = input("What is your truck roll cost?")
# budget = input("What is your annual O&M budget?")
# PPA units in kWh
ppa = 0.15
# Plant capacity in kw
# plant_dc_capacity = 996.48
# plant_ac_capacity = 744
energy_billable = 4000
def daily_loss(ppa,energy_billable):
	loss_calculation = ppa * energy_billable
	return loss_calculation
	print(loss_calculation)
daily_loss(ppa,energy_billable)


# while int(cost) > int(daily_loss):
# 	daily_loss += daily_loss
# 	print(daily_loss)
	# if cost == ppa_rate:
	# break
	# print("It makes economic sense to roll a truck.")