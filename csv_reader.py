import csv

with open('sd_metstations.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print(line)
