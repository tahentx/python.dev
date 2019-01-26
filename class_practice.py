import csv
with open('sd_metstations.csv', 'r') as csv_file:
	met = csv.reader(csv_file)
	metlist = list(met)


class Site:
	def __init__(self, lat, long):
		self.lat = ""
		self.long = ""

ironmountain = Site(metlist[0][1],metlist[1][2])
ironmountain.lat = metlist[0][1]
ironmountain.long = metlist[1][2]
print("The latitude of Iron Mountain Flanders is " + str(ironmountain.lat) + "and the longitude is " + str(ironmountain.long))
# ironmountain = Site(met[1:],met[2])
# ironmountain.lat = met[1]
# print(ironmountain.lat)

		