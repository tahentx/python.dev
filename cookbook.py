# Ingest Upton inverter data
# with open('workorder.txt', 'r') as f:
#  data = f.read()
#  print(data)

# Write new work order
wo1 = []
wo1.append("WO-43528")
wo1.append("WO-21342")
wo1.append("WO-88887")
wo1.append("WO-23955")

file = open("workorder.txt", "r+")
for i in range(4):
	file.write(wo1[i])
	# file.write("\n")

for line in file:
	print(line)
file.close()