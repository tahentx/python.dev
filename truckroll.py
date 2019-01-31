from random import *
outage = randint(1,1000)

equipment = ['combiner','tracker','inverter', 'transformer', 'breaker']

def random_outage_generator(equipment):
	equipment_offline = sample(equipment, 1)
	print('Event: ' + str(equipment_offline[0]) + ' failure today; estimated lost kWh: ' + str(outage) + '.')

random_outage_generator(equipment)