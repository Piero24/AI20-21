from constraint import *
import networkx as nx

# Esercizio 1
#
# Scrivere una funzione sistema3() che modella e risolve il
# seguente problema usando il modulo python-constraint. La
# funzione non necessita di parametri e restituisce solamente
# la prima soluzione trovata dal solver.
# X = {x, y, z}
# Dx = [10,20,30]
# Dy = [40,50,16]
# Dz = [4,5,16]
# x < y
# x + y + z < 65


def sistema3():

    problem = Problem()

    problem.addVariable("x", [10,20,30])
    problem.addVariable("y", [40,50,16])
    problem.addVariable("z", [4,5,16])

    problem.addConstraint(lambda a,b : a < b, ("x","y"))
    problem.addConstraint(lambda a,b,c : a + b + c < 65, ("x","y","z"))

    solution = problem.getSolution()

    if not solution:

    	return {}

    return solution


# Esercizio 2
#
# Scrivere una funzione grafo_vincoli(grafo). Si supponga
# che il grafo rappresenti un problema di colorazione di una
# mappa. La funzione deve risolvere il problema di
# colorazione della mappa rappresentata dal grafo dei
# vincoli passato come parametro. La funzione restituisce, se
# esiste, solamente la prima soluzione trovata dal solver.


def grafo_vincoli(grafo):

    problem = Problem()
    list = []

    domain = ["RED", "GREEN", "BLUE"]

    for element in grafo.nodes():

        list.append(element)
        problem.addVariable(element,domain)

    while len(list) > 0:

        cont = []
        index = list.pop(0)

        for element in grafo[index]:

            cont.append(element)

        for element in cont:

            problem.addConstraint(lambda a,b : a != b,[index, element])


    solution = problem.getSolution()

    if not solution:

    	return {}

    return solution


# Esercizo 3
#
# Scrivere una funzione nqueen(n) che modella e risolve il
# problema delle n regine su una scacchiera senza che
# nessuna risulti essere sotto attacco. La funzione riceve
# come parametro il numero di regine e restituisce
# solamente la prima soluzione trovata dal solver.


def nqueen(n):

	problem = Problem()
	domain = [index for index in range(0,n)]
	queen = [index for index in range(0,n)]
	problem.addVariables(domain, queen)

	for queen_index in queen:

		problem.addConstraint(AllDifferentConstraint())

		for domain_index in domain:

			if domain_index != queen_index :

				problem.addConstraint(lambda row1, row2, column1 = queen_index, column2 = domain_index : abs(row1 - row2) != abs(column1 - column2) and row1 != row2, (queen_index, domain_index))

	solution = problem.getSolutions()

	if not solution:

		return {}

	return solution[0]
