# cost = input("What is your truck roll cost?")
# budget = input("What is your annual O&M budget?")
# PPA units in kWh
ppa = 0.15
# Plant capacity in kw
# plant_dc_capacity = 996.48
# plant_ac_capacity = 744
energy_billable = 4000
def daily_loss(ppa,energy_billable):
	print(ppa * energy_billable)
daily_loss(ppa,energy_billable)
	
while cost > daily_loss:
	cost += cost
	print(cost)
	# if cost == ppa_rate:
	# break
	# print("It makes economic sense to roll a truck.")