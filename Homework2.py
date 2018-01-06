import csv

def Min(field):
	if field == d_csvfile.fieldnames[0]:
		print min(l_ZipCode)
		print "-------------------"
	elif field == d_csvfile.fieldnames[1]:
		print min(l_TotalPopulation)
		print "-------------------"
	elif field == d_csvfile.fieldnames[2]:
		print min(l_MedianAge)
		print "-------------------"
	elif field == d_csvfile.fieldnames[3]:
		print min(l_TotalMales)
		print "-------------------"
	elif field == d_csvfile.fieldnames[4]:
		print min(l_TotalFemales)
		print "-------------------"
	elif field == d_csvfile.fieldnames[5]:
		print min(l_TotalHouseholds)
		print "-------------------"
	elif field == d_csvfile.fieldnames[6]:
		print min(l_AverageHouseholdSize)
		print "-------------------"
	else:
		print "Wrong Field!"
		print "-------------------"

def Max(field):
	if field == d_csvfile.fieldnames[0]:
		print max(l_ZipCode)
		print "-------------------"
	elif field == d_csvfile.fieldnames[1]:
		print max(l_TotalPopulation)
		print "-------------------"
	elif field == d_csvfile.fieldnames[2]:
		print max(l_MedianAge)
		print "-------------------"
	elif field == d_csvfile.fieldnames[3]:
		print max(l_TotalMales)
		print "-------------------"
	elif field == d_csvfile.fieldnames[4]:
		print max(l_TotalFemales)
		print "-------------------"
	elif field == d_csvfile.fieldnames[5]:
		print max(l_TotalHouseholds)
		print "-------------------"
	elif field == d_csvfile.fieldnames[6]:
		print max(l_AverageHouseholdSize)
		print "-------------------"
	else:
		print "Wrong Field!"
		print "-------------------"

def Avg(field):
	sum = 0
	if field == d_csvfile.fieldnames[0]:
		for val in l_ZipCode:
			sum = sum + int(val)
		print sum / len(l_ZipCode)
		print "-------------------"
	elif field == d_csvfile.fieldnames[1]:
		for val in l_TotalPopulation:
			sum = sum + int(val)
		print sum / len(l_TotalPopulation)
		print "-------------------"
	elif field == d_csvfile.fieldnames[2]:
		for val in l_MedianAge:
			sum = sum + float(val)
		print sum / len(l_MedianAge)
		print "-------------------"
	elif field == d_csvfile.fieldnames[3]:
		for val in l_TotalMales:
			sum = sum + int(val)
		print sum / len(l_TotalMales)
		print "-------------------"
	elif field == d_csvfile.fieldnames[4]:
		for val in l_TotalFemales:
			sum = sum + int(val)
		print sum / len(l_TotalFemales)
		print "-------------------"
	elif field == d_csvfile.fieldnames[5]:
		for val in l_TotalHouseholds:
			sum = sum + int(val)
		print sum / len(l_TotalHouseholds)
		print "-------------------"
	elif field == d_csvfile.fieldnames[6]:
		for val in l_AverageHouseholdSize:
			sum = sum + float(val)
		print sum / len(l_AverageHouseholdSize)
		print "-------------------"
	else:
		print "Wrong Field!"
		print "-------------------"

def Search(field, value):
	first_pos = 0
	if field == d_csvfile.fieldnames[0]:
		for i in range(l_ZipCode.count(value)):
			new_list = l_ZipCode[first_pos:]
			next_pos = new_list.index(value) + 1
			location = first_pos + new_list.index(value)
			print "ZipCode:", l_ZipCode[location], "\nTotalPopulation:", l_TotalPopulation[location], "\nMedianAge:", l_MedianAge[location], "\nTotalMales:", l_TotalMales[location], "\nTotalFemales:", l_TotalFemales[location], "\nTotalHouseholds:", l_TotalHouseholds[location], "\nAverageHouseholdSize:", l_AverageHouseholdSize[location]
			print "-------------------"
			first_pos += next_pos
	if field == d_csvfile.fieldnames[1]:
		for i in range(l_TotalPopulation.count(value)):
			new_list = l_TotalPopulation[first_pos:]
			next_pos = new_list.index(value) + 1
			location = first_pos + new_list.index(value)
			print "ZipCode:", l_ZipCode[location], "\nTotalPopulation:", l_TotalPopulation[location], "\nMedianAge:", l_MedianAge[location], "\nTotalMales:", l_TotalMales[location], "\nTotalFemales:", l_TotalFemales[location], "\nTotalHouseholds:", l_TotalHouseholds[location], "\nAverageHouseholdSize:", l_AverageHouseholdSize[location]
			print "-------------------"
			first_pos += next_pos
	if field == d_csvfile.fieldnames[2]:
		for i in range(l_MedianAge.count(value)):
			new_list = l_MedianAge[first_pos:]
			next_pos = new_list.index(value) + 1
			location = first_pos + new_list.index(value)
			print "ZipCode:", l_ZipCode[location], "\nTotalPopulation:", l_TotalPopulation[location], "\nMedianAge:", l_MedianAge[location], "\nTotalMales:", l_TotalMales[location], "\nTotalFemales:", l_TotalFemales[location], "\nTotalHouseholds:", l_TotalHouseholds[location], "\nAverageHouseholdSize:", l_AverageHouseholdSize[location]
			print "-------------------"
			first_pos += next_pos
	if field == d_csvfile.fieldnames[3]:
		for i in range(l_TotalMales.count(value)):
			new_list = l_TotalMales[first_pos:]
			next_pos = new_list.index(value) + 1
			location = first_pos + new_list.index(value)
			print "ZipCode:", l_ZipCode[location], "\nTotalPopulation:", l_TotalPopulation[location], "\nMedianAge:", l_MedianAge[location], "\nTotalMales:", l_TotalMales[location], "\nTotalFemales:", l_TotalFemales[location], "\nTotalHouseholds:", l_TotalHouseholds[location], "\nAverageHouseholdSize:", l_AverageHouseholdSize[location]
			print "-------------------"
			first_pos += next_pos
	if field == d_csvfile.fieldnames[4]:
		for i in range(l_TotalFemales.count(value)):
			new_list = l_TotalFemales[first_pos:]
			next_pos = new_list.index(value) + 1
			location = first_pos + new_list.index(value)
			print "ZipCode:", l_ZipCode[location], "\nTotalPopulation:", l_TotalPopulation[location], "\nMedianAge:", l_MedianAge[location], "\nTotalMales:", l_TotalMales[location], "\nTotalFemales:", l_TotalFemales[location], "\nTotalHouseholds:", l_TotalHouseholds[location], "\nAverageHouseholdSize:", l_AverageHouseholdSize[location]
			print "-------------------"
			first_pos += next_pos
	if field == d_csvfile.fieldnames[5]:
		for i in range(l_TotalHouseholds.count(value)):
			new_list = l_TotalHouseholds[first_pos:]
			next_pos = new_list.index(value) + 1
			location = first_pos + new_list.index(value)
			print "ZipCode:", l_ZipCode[location], "\nTotalPopulation:", l_TotalPopulation[location], "\nMedianAge:", l_MedianAge[location], "\nTotalMales:", l_TotalMales[location], "\nTotalFemales:", l_TotalFemales[location], "\nTotalHouseholds:", l_TotalHouseholds[location], "\nAverageHouseholdSize:", l_AverageHouseholdSize[location]
			print "-------------------"
			first_pos += next_pos
	if field == d_csvfile.fieldnames[6]:
		for i in range(l_AverageHouseholdSize.count(value)):
			new_list = l_AverageHouseholdSize[first_pos:]
			next_pos = new_list.index(value) + 1
			location = first_pos + new_list.index(value)
			print "ZipCode:", l_ZipCode[location], "\nTotalPopulation:", l_TotalPopulation[location], "\nMedianAge:", l_MedianAge[location], "\nTotalMales:", l_TotalMales[location], "\nTotalFemales:", l_TotalFemales[location], "\nTotalHouseholds:", l_TotalHouseholds[location], "\nAverageHouseholdSize:", l_AverageHouseholdSize[location]
			print "-------------------"
			first_pos += next_pos

def Range(field, range_min, range_max):
	new_list = list()
	if field == d_csvfile.fieldnames[0]:
		range_min = int(range_min)
		range_max = int(range_max)
		for value in l_ZipCode:
			if int(value) >= range_min and int(value) <= range_max:
				new_list.append(int(value))
		new_list.sort()
		for val in new_list:
			Search(field, str(val))
	if field == d_csvfile.fieldnames[1]:
		range_min = int(range_min)
		range_max = int(range_max)
		for value in l_TotalPopulation:
			if int(value) >= range_min and int(value) <= range_max:
				new_list.append(int(value))
		new_list.sort()
		for val in new_list:
			Search(field, str(val))
	if field == d_csvfile.fieldnames[2]:
		range_min = float(range_min)
		range_max = float(range_max)
		for value in l_MedianAge:
			if float(value) >= range_min and float(value) <= range_max:
				new_list.append(float(value))
		new_list.sort()
		for val in new_list:
			Search(field, str(val))
	if field == d_csvfile.fieldnames[3]:
		range_min = int(range_min)
		range_max = int(range_max)
		for value in l_TotalMales:
			if int(value) >= range_min and int(value) <= range_max:
				new_list.append(int(value))
		new_list.sort()
		for val in new_list:
			Search(field, str(val))
	if field == d_csvfile.fieldnames[4]:
		range_min = int(range_min)
		range_max = int(range_max)
		for value in l_TotalFemales:
			if int(value) >= range_min and int(value) <= range_max:
				new_list.append(int(value))
		new_list.sort()
		for val in new_list:
			Search(field, str(val))
	if field == d_csvfile.fieldnames[5]:
		range_min = int(range_min)
		range_max = int(range_max)
		for value in l_TotalHouseholds:
			if int(value) >= range_min and int(value) <= range_max:
				new_list.append(int(value))
		new_list.sort()
		for val in new_list:
			Search(field, str(val))
	if field == d_csvfile.fieldnames[6]:
		range_min = float(range_min)
		range_max = float(range_max)
		for value in l_AverageHouseholdSize:
			if float(value) >= range_min and float(value) <= range_max:
				new_list.append(float(value))
		new_list.sort()
		for val in new_list:
			Search(field, str(val))

filename = raw_input("Please Enter the File Name:")
file = open(filename, "r")
l_csvfile = csv.reader(file)
d_csvfile = csv.DictReader(file)
print "-------------------"
print "Field:", d_csvfile.fieldnames[0], d_csvfile.fieldnames[1], d_csvfile.fieldnames[2], d_csvfile.fieldnames[3], d_csvfile.fieldnames[4], d_csvfile.fieldnames[5], d_csvfile.fieldnames[6]
print "-------------------"
print "Function: min <field>, max <field>, avg <field>, search <field> <value>, range <field> <min> <max>, quit"
print "-------------------"



l_ZipCode = list()
l_TotalPopulation = list()
l_MedianAge = list()
l_TotalMales = list()
l_TotalFemales = list()
l_TotalHouseholds = list()
l_AverageHouseholdSize = list()

for row in l_csvfile:
	l_ZipCode.append(row[0])
	l_TotalPopulation.append(row[1])
	l_MedianAge.append(row[2])
	l_TotalMales.append(row[3])
	l_TotalFemales.append(row[4])
	l_TotalHouseholds.append(row[5])
	l_AverageHouseholdSize.append(row[6])

while True:
	try:
		function_field = raw_input("Enter Function and Field:")
		if function_field == "quit":
			break
		else:
			function_field = function_field.split()
			function = function_field[0]
			field = function_field[1]
			if function == "min":
				Min(field)
			elif function == "max":
				Max(field)
			elif function == "avg":
				Avg(field)
			elif function == "search":
				value = function_field[2]
				Search(field, value)
			elif function == "range":
				range_min = function_field[2]
				range_max = function_field[3]
				Range(field, range_min, range_max)
	except:
		print "There's no such function!"
file.close()