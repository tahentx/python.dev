import geopy.distance
import csv

with open('sd_metstations.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print(line[1:])
		# TODO: create a list from the row
		# TODO: find the distance between one row and each of the rest of the rows
		# TODO: identify the one that is closest to that row
		# TODO: Insert that value into a new array
		# TODO: Repeat the distance analysis for the next row
		# TODO: Write the shortest distance values to new file with name of site and distance value

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print(geopy.distance.distance(coords_1, coords_2).miles)