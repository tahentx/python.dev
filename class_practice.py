class Tracker:
	def __init__(self, axis, manufacturer):
		self.axis = ""
		self.manufacturer = ""

china_lake = Tracker("single","SunPower")

china_lake.manufacturer = "SunPower"
print(china_lake.manufacturer)
		