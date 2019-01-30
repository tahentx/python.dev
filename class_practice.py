import csv
import geopy.distance

with open('sd_metstations.csv', 'r') as csv_file:
	met = csv.reader(csv_file)
	metlist = list(met)


class Site:
	def __init__(self, lat, long):
		self.lat = ""
		self.long = ""

	def calculate(coords_1,coords_2):
		coords_1 = ""
		coords_2 = ""
		return geopy.distance.distance(coords_1, coords_2).miles

# Capture coordinates, assign to properties

ironmountain = Site(metlist[0][1],metlist[0][2])
ironmountain.name = metlist[0][0]
ironmountain.lat = metlist[0][1]
ironmountain.long = metlist[0][2]

sdpd_west = Site(metlist[1][1],metlist[1][2])
sdpd_west.name = metlist[1][0]
sdpd_west.lat = metlist[1][1]
sdpd_west.long = metlist[1][2]

sd_missionvalley = Site(metlist[2][1],metlist[2][2])
sd_missionvalley.name = metlist[2][0]
sd_missionvalley.lat = metlist[2][1]
sd_missionvalley.long = metlist[2][2]

sdpd_central = Site(metlist[3][1],metlist[3][2])
sdpd_central.name = metlist[3][0]
sdpd_central.lat = metlist[3][1]
sdpd_central.long = metlist[3][2]

mission_trails = Site(metlist[4][1],metlist[4][2])
mission_trails.name = metlist[4][0]
mission_trails.lat = metlist[4][1]
mission_trails.long = metlist[4][2]

inspiration = Site(metlist[5][1],metlist[5][2])
inspiration.name = metlist[5][0]
inspiration.lat = metlist[5][1]
inspiration.long = metlist[5][2]

# this code works
# backup = []

# coords_1 = [sdpd_central.lat,sdpd_central.long]
# coords_2 = [mission_trails.lat,mission_trails.long]
# coords_3 = [inspiration.lat,inspiration.long]

# backup.append(geopy.distance.distance(coords_1, coords_2).miles)
# backup.append(geopy.distance.distance(coords_1, coords_3).miles)
# print(min(backup))

sites_with_mets = [[ironmountain.lat,ironmountain.long],[sdpd_west.lat,sdpd_west.long],[sd_missionvalley.lat,sd_missionvalley.long],[sdpd_central.lat,sdpd_central.long],[mission_trails.lat,mission_trails.long],[inspiration.lat,inspiration.long]]

def calculate():
	backup = []
	for sites in enumerate(sites_with_mets):

	# backup_candidate = enumerate(sites_with_mets)
			


