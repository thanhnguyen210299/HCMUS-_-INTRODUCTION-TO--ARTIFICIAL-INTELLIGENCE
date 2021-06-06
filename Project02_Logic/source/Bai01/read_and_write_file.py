'''******************** READ INPUT ********************''' 

'''
    Read input to a dictionary:
        + 'base knowledge': a list of clauses
        + 'query': alpha
	+ 'number of clauses': number of clauses
    Warning: There are more than one white space between literal and symbol (OR)
'''
def readInput(input_link: str) -> dict:

	input_file = {}
	input_file['base knowledge'] = []
	fi = open(input_link, 'r')
	
	for i, line in enumerate(fi):
		"Read a line then split it"
		line = line.strip().split(' ')
		tokens = [token for token in line if token != '' and token != 'OR']

		def abs_key(n):
			if (n[0] == '-'):
				return n[1:]
			return n

		tokens.sort(key = abs_key)

		res = ' OR '.join(tokens)

		if i == 0:
			input_file['query'] = res
		elif i == 1:
			input_file['number of clauses'] = int(res)
		else:
			input_file['base knowledge'].append(res)
        
	return input_file

'''******************** WRITE OUTPUT ********************'''

"Write to output file"
def writeOutput(output_link: str, list_clauses_step: list, number_clauses_step: list, KB: bool) -> dict:

	"Open file ouput"
	output_file = open(output_link, 'w')

	for i in range(1, len(number_clauses_step)):
		number_clauses_step[i] = number_clauses_step[i] + number_clauses_step[i - 1]

        
	for i in range(1, len(number_clauses_step)):

		temp = list_clauses_step[number_clauses_step[i-1]: number_clauses_step[i]]
		print(len(temp), file = output_file)

		for clause in temp:
			print(clause, file = output_file)
	
	if (KB == True):

		print('YES', file = output_file)

	else:

		print(0, file = output_file)

		print('NO', file = output_file)

	output_file.close()

