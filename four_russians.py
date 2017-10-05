import sys
import csv

arguments = sys.argv
matrix_dict = {}

def length_check(matrixes):
	length = 0;
	for matrix in matrixes:
		if len(matrixes[matrix]) == length or length == 0:
			length = len(matrixes[matrix])
		elif len(matrixes[matrix]) != length:
			raise Exception('Matrixes must be of same size')
	return length

def partition_matrixes(matrixes):
	length = length_check(matrixes)
	division_size = get_log(length, 2)
	division_size = round_number(length/division_size, 'up')
	new_matrixes = {}
	for matrix in matrixes:
		current_matrix = matrixes[matrix]
		new_matrix = []
		while len(current_matrix) > 0:
			divided_list = []
			for x in xrange(0,division_size):
				if len(current_matrix) > 0:
					divided_list.append(current_matrix.pop(0))
				else:
					divided_list.append(create_list(length, 0))
			new_matrix.append(divided_list)
		new_matrixes[matrix] = new_matrix
	return new_matrixes

def power_of(number, power):
	if power == 0:
		return 1
	product = number
	counter = 1;
	while counter < power:
		product *= number
		counter += 1
	return product

def round_number(number, direction = None):
	float_part = number % int(number)
	if float_part > 0.5 or direction == 'up':
		return int(number) + 1
	else:
		return int(number)

def get_log(number, power):
	power = float(power)
	accumulative_power = 0
	quotient = number
	if power == 0:
		raise Exception('Cannot find log with base power zero')
	elif power == 1:
		return 0
	while(quotient > power):
		quotient /= power
		accumulative_power += 1
	log = accumulative_power + (quotient/power)
	return log

def create_list(row_size = 0, column_size = 0):
	if row_size == 0:
		if column_size == 0:
			return [0]
	else:
		if row_size != 0:
			if column_size != 0:
				row = []
				for x in range(row_size):
					column = []
					for z in range(column_size):
						column.append(0)	
					row.append(column)
			else:
				row = []
				for x in range(row_size):
					row.append(0)
	return row


def row_from_bottom(matrix, row_index):
	print(matrix)
	return matrix[len(matrix) - (row_index + 1)]

def add_boolean(matrix_1, matrix_2):
	matrixes = {'matrix_1':matrix_1, 'matrix_2':matrix_2}
	length = length_check(matrixes)
	resulting_matrix = []
	for index in range(0, length):
		sum = int(matrix_1[index]) + int(matrix_2[index])
		if sum >= 1:
			resulting_matrix.append(1)
		elif sum <= 0:
			resulting_matrix.append(0)
	return resulting_matrix

def number_of_row(first_matrix, row):
	for row_index, row_value in enumerate(first_matrix):
		if row_value == first_matrix[row]:
			return row_index
	raise Exception('Could not find the row of first matrix')

def four_russians(matrix_dict, partitioned_matrixes, length):
	length = length
	division_size = get_log(length, 2)
	final_list = create_list(length, length)
	iterations = int(round_number(length/division_size, 'up'))
	for i in range(0, iterations):
		row_sum = create_list(length, length)
		powers_of_two_num = 1
		row_index = 0
		for j in range(0, length):
			row_sum[j] = add_boolean(row_sum[j - int(power_of(2, row_index))], row_from_bottom(partitioned_matrixes['matrix_1'][i], row_index))
			if powers_of_two_num == 1:
				powers_of_two_num = j + 1
				row_index += 1
			else:
				powers_of_two_num -= 1
		list_to_add = create_list(length, length)
		for j in range(0, length):
			list_to_add[j] = row_sum[number_of_row(matrix_dict['matrix_0'], j)]
		for index, row in enumerate(final_list):
			final_list[index] = add_boolean(row, list_to_add[index])
	return final_list

def pretty_print(matrix):
	csv_writer = csv.writer(sys.stdout)
	for row in matrix:
		csv_writer.writerow(row)

try:
	matrixes_copy = {}
	contents_to_copy = []
	for argument_index in range(len(arguments)):
		if argument_index == 0:
			continue
		matrix_name = 'matrix_'+str(argument_index-1)
		matrix_dict[matrix_name] = []
		with open(arguments[argument_index]) as csv_file:
			reader = csv.reader(csv_file);
			for row in reader:
				matrix_dict[matrix_name].append(row)
				contents_to_copy.append(row)
		matrixes_copy.update({matrix_name:contents_to_copy})
	if len(matrix_dict) == 2:
		length = length_check(matrix_dict)
		partitioned_matrixes = partition_matrixes(matrix_dict)
		matrixes_product = four_russians(matrixes_copy, partitioned_matrixes, length)
		print(matrixes_product)
	elif len(matrix_dict) == 1:
		# raise Exception('Graph solution not yet implemented.')
		length = len(matrix_dict['matrix_0']) + 1
		adjacency_matrix = create_list(length, length)
		nodes_to_connect = []
		for row_value in matrix_dict['matrix_0']:
			node_1, node_2 = row_value[0].split()
			for adj_row_index, adj_row_value in enumerate(adjacency_matrix):
				for ajd_column_index, adj_column_value in enumerate(adj_row_value):
					node_1 = int(node_1)
					node_2 = int(node_2)
					if ((node_1 == adj_row_index and node_2 == ajd_column_index) or (adj_row_index == ajd_column_index)):
						nodes_to_connect.append([adj_row_index, ajd_column_index])
		for nodes in nodes_to_connect:
			adjacency_matrix[nodes[0]][nodes[1]] = 1
		for x in range(length - 1):
			matrixes_product = four_russians(adjacency_matrix)
		#Create 2 matrixes and partioned ones to use for four russians
	else:
		raise Exception('Number of arguments passed is not correct. Please try again with one(1) or two(2) files.')
	pretty_print(matrixes_product)
except Exception as e:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	print(exc_tb.tb_lineno, e)
	sys.exit()
