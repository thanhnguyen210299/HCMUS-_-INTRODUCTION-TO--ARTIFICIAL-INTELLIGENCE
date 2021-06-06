  
'''******************** MAIN ********************'''
from pl_resolution import pl_resolution
from read_and_write_file import readInput, writeOutput
from helper_functions import removeLiteral, createNewClause

def main():

	file_in = readInput('D:/input.txt')
	print(file_in)
	
	alpha = file_in['query']
	KB = file_in['base knowledge']

	list_clauses_step = []
	number_clauses_step = []
	number_clauses_step.append(0)
	
	result = pl_resolution(KB, alpha, list_clauses_step, number_clauses_step)
	print(result)

	writeOutput('D:/output.txt', list_clauses_step, number_clauses_step, result)
	
if __name__ == '__main__':
	main()






























