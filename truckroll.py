ppa_price = 10
production_capacity = 250
def opportunity_cost (ppa_price, production_capacity):
	opp_cost = ppa_price * production_capacity
	return opp_cost
print(str(opportunity_cost))