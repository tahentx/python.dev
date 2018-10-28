lost_production = input("What is your daily system PPA loss: ")
regional_truck_roll_hourly_cost = input("What is your truck roll cost: ")
if lost_production > regional_truck_roll_hourly_cost:
	print("Roll a truck.")
else:
	print("The economics don't make sense.")  