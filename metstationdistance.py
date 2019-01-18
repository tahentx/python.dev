import geopy.distance
import csv

with open('sd_metstations.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print(line)

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print(geopy.distance.distance(coords_1, coords_2).miles)