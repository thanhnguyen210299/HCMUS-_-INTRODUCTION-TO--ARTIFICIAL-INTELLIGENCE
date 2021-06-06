'''******************** PL-RESOLUTION ********************'''
from copy import deepcopy
from helper_functions import removeLiteral, negateAlpha, createNewClause, isUseless, combine

'''
    Calculate the set of all possible clauses by resolving its two inputs
        Input: clause 1 and clause 2
        Output: Parameters: The set of all possible clauses obtained by resolving its two inputs.
'''
def pl_resolve(clause1: str, clause2: str) -> set:
	
	clauses = set()
	literals_in_c1 = [literal for literal in clause1.split(' ') if literal != 'OR']
	literals_in_c2 = [literal for literal in clause2.split(' ') if literal != 'OR']	

	for i in literals_in_c1:
		for j in literals_in_c2:
			if i == '-' + j or \
                           j == '-' + i:
				
				new_i = removeLiteral(literals_in_c1, i)
				new_j = removeLiteral(literals_in_c2, j)

				new_clause = createNewClause(new_i, new_j)

				if not isUseless(new_clause):
					new_clause = combine(new_clause)
					clauses.update({new_clause})
	return clauses

'''
    A simple resolution algorithm for propositional logic
        Input: + KB: the knowledge base
               + alpha: the query
               + list_of_clauses: 
               + number_of_clauses:
        Output: true if KB |= alpha, false otherwise
'''
def pl_resolution(KB: list, alpha: str, list_clauses_step: list, number_clauses_step: list) -> bool:
	"Init"
	flag_empty_resolvents = False;
	new_clauses = set()
	previous_clauses = set()
	
	"The set of clauses in the CNF representation of KB ∧ negative alpha"
	clauses = deepcopy(KB)
	clauses.extend(negateAlpha(alpha))
	print(clauses)

	while True:

                count_steps = 0
                n = len(clauses)
                count = 0

                pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]

                for clause1, clause2 in pairs:
                        resolvents = pl_resolve(clause1, clause2)
			
                        "If resolvents contains the empty clause then turn flag on"
                        if ('' in resolvents):
                                flag_empty_resolvents = True
			
                        "Compute new clause = new clause V resolvents"
                        for res in resolvents:
                                if (res not in new_clauses):
                                        new_clauses.add(res)
                                        print('Step', count, ': (', clause1, ') AND (', clause2,')')
                                        if (res == ''):
                                                print('{}')
                                        else:
                                                print(res)
                                        count = count + 1
		
                "If new_clause is a subset of clauses then return false"
                clauses_set = set(clauses)
                if new_clauses <= clauses_set:
                        return False;
		
                "Compute clauses = clauses V new_clause"
                for clause in new_clauses:
                        if (clause not in clauses):
                                count_steps = count_steps + 1
                                if clause == '':
                                        list_clauses_step.append('{}')
                                else:
                                        list_clauses_step.append(clause)
                                clauses.append(clause)
                number_clauses_step.append(count_steps)

                "If flag is on then return True"
                if (flag_empty_resolvents):
                        return True;

                new_clauses = set()
                print('######################3')
