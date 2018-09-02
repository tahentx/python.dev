cost = int(input("What is your truck roll cost?"))
# budget = input("What is your annual O&M budget?")
# PPA units in kWh
ppa = 0.15
# Plant capacity in kw
# plant_dc_capacity = 996.48
# plant_ac_capacity = 744
energy_billable = 4000
def daily_loss(ppa,energy_billable):
	loss_calculation = int(ppa * energy_billable)
	print(loss_calculation)
daily_loss(ppa,energy_billable)
daily_loss_compound = daily_loss(ppa, energy_billable)

print(type(daily_loss_compound))
print(type(cost))
# while cost > daily_loss_compound:
# 	daily_loss_compound += daily_loss_compound
# 	print(daily_loss_compound)
	# if cost == ppa_rate:
	# break
	# print("It makes economic sense to roll a truck.")