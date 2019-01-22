import geopy.distance
import csv
import numpy as np

with open('sd_metstations.csv', 'r') as csv_file:
	metstations = csv.reader(csv_file)
	metstationlist = list(metstations)
	backup = []
	met = np.array(metstationlist)
	def calculate_distance(coords_1,coords_2):
		coords_1 = metstationlist[ : ,1:2]
		coords_2 = metstationlist[1,1:2]
		return geopy.distance.distance(coords_1, coords_2).miles

	calculate_distance()

	# for line in range(1,len(metstationlist)):
	# 	coords_1 = (metstationlist[1][1],metstationlist[1][2])
	# 	coords_2 = (metstationlist[2][1],metstationlist[2][2])	
		# print(geopy.distance.distance(coords_1, coords_2).miles)




# for line in range(1, len(metstationlist)):
# 	for x in enumerate(metstationlist):
# 		coords_1 = (metstationlist[1])
		
	# for line in metstationlist:
	# 	print(line[0])
		# print(line[1:])
		# TODO: create a list from the row
		


		# TODO: find the distance between one row and each of the rest of the rows
		# TODO: identify the one that is closest to that row
		# TODO: Insert that value into a new array
		# TODO: Repeat the distance analysis for the next row
		# TODO: Write the shortest distance values to new file with name of site and distance value

# coords_1 = (52.2296756, 21.0122287)
# coords_2 = (52.406374, 16.9251681)
# print(geopy.distance.distance(coords_1, coords_2).miles)
