'''******************** HELPER FUNCTIONS ********************'''
from copy import deepcopy

"Remove a literal from a clause"
def removeLiteral(clause: list, literal_need_remove: str) -> list:

	temp = deepcopy(clause)
	for literal in clause:
		if (literal == literal_need_remove):
			temp.remove(literal)
	return temp

"Split a clause to list"
def negateAlpha(alpha: str) -> list:

	temp = []
	tokens = alpha.split(' ')
	for word in tokens:
		if (word == 'OR'):
			continue
		elif (word == 'AND'):
			temp.append('OR')
		elif ('-' in word):
			temp.append(word[1:])
		else:
			temp.append('-' + word)
	return temp

"Create a new clause by connect 2 clauses"
def createNewClause(clause1: list, clause2:list) -> list:

	clause1.extend(clause2)
	
	new_clause = list(set(clause1))
	new_clause = [literal for literal in new_clause if literal != '']

	return new_clause


def isUseless(clause: list) -> bool:
	
	temp = deepcopy(clause)

	if (len(temp) == 1):
		return False
	else:
		while (temp != []):
			literal = temp.pop()
			if ('-' + literal in temp) or (literal[1:] in temp):
				return True
	return False

"Connect list to a clause"
def combine(clause: list) -> str:

	def abs_key(n):
                if (n[0] == '-'):
                        return n[1:]
                return n
        
	clause.sort(key = abs_key)
	for literal in clause:
		if literal == '':
			clause.remove('')
	return ' OR '.join(clause)
