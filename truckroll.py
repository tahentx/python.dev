import numpy as np
cost = input("What is your truck roll cost?")
budget = input("What is your annual O&M budget?")
ppa_price = .1
while cost < budget:
	cost += cost
	print(cost)
