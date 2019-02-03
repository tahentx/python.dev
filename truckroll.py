import csv
from random import *
outage = randint(1,1000)

with open('Academy pvwatts_hourly.csv', 'r') as csv_file:
	model = csv.reader(csv_file)
	model_list = list(model)

# print(model_list)

equipment = ['combiner','tracker','inverter', 'transformer', 'breaker']

def random_outage_generator(equipment):
	equipment_offline = sample(equipment, 1)
	print('Event: ' + str(equipment_offline[0]) + ' failure today; estimated lost kWh: ' + str(outage) + '.')



random_outage_generator(equipment)