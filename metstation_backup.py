import csv
with open('sd_metstations.csv', 'r') as csv_file:
	met = csv.DictReader(csv_file)
	for row in met:
		coords_1 = (met[1][1],met[1][2])
		coords_2 = (met[2][1],met[2][2])	
		print(geopy.distance.distance(coords_1, coords_2).miles)
		next(met)