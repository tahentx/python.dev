from random import *
outage = randint(1,1000)

equipment = ['combiner','tracker','inverter', 'transformer', 'breaker']
equipment_offline = sample(equipment, 1)
print('Event: ' + str(equipment_offline[0]) + ' failure today; estimated lost kWh: ' + str(outage) + '.')