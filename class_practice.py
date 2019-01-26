import csv
with open('sd_metstations.csv', 'r') as csv_file:
	met = csv.reader(csv_file)
	metlist = list(met)


class Site:
	def __init__(self, lat, long):
		self.lat = ""
		self.long = ""

print(metlist)

# ironmountain = Site(met[1:],met[2])
# ironmountain.lat = met[1]
# print(ironmountain.lat)

		