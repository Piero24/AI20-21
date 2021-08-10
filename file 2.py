import networkx as nx


# Esercizio 1
#
# Sviluppare la funzione diam_graph(grafo) che dato come
# parametro un grafo di tipo networkx restituisce il diametro del
# grafo. Usare le funzioni disponibili nel modulo networkx.


def diam_graph(grafo):

    if type(grafo) is not type(nx.Graph()) or len(grafo.nodes()) == 0 or len(grafo.edges()) == 0:

        return -1

    else:

        return nx.diameter(grafo)


# Esercizio 2
#
# Sviluppare la funzione max_degree(grafo) che dato come
# parametro un grafo di tipo networkx restituisce la lista dei nodi con
# grado maggiore. Usare le funzioni disponibili nel modulo networkx.


def max_degree(grafo):

    st_dg = 0
    list_graf = []

    if type(grafo) is not type(nx.Graph()) or len(grafo.nodes()) == 0 or len(grafo.edges()) == 0:

        return list_graf

    for index in grafo:

        if grafo.degree(index) > st_dg:

            st_dg = grafo.degree(index)

    for index in grafo:

        if grafo.degree(index) == st_dg:

            list_graf.append(index)

    return list_graf


# Esercizio 3
#
# Sviluppare la ricerca in ampiezza in una funzione ampiezza(grafo, start, end) dati:
# Il grafo di tipo networkx
# Start, il nome di un nodo di partenza
# End, il nome del nodo di arrivo
#
# restituisce la lista dei nodi visitati per andare dal nodo start al nodo end, compresi
# start e end.
# Prestare attenzione al tipo di ritorno nel caso di grafo nullo. Gestire l’eventuale
# passaggio di nodi non appartenenti al grafo, anche in questo caso prestate
# attenzione al tipo restituito dalla funzione.
# NON UTILIZZARE FUNZIONI PREDEFINITE DEL MODULO NETWORKX PER
# SVILUPPARE L’ALGORITMO DI RICERCA.


def ampiezza(grafo, start, end):

    frontier = []
    explored = []
    dictionary = {}

    if type(grafo) is not type(nx.Graph()) or start not in grafo.nodes() or end not in grafo.nodes() or len(grafo.nodes()) == 0 or len(grafo.edges()) == 0:

        return []

    frontier.append(start)

    while len(frontier) > 0:

        node = frontier.pop()
        explored.append(node)

        if node not in dictionary:

            dictionary[node] = []

        dictionary[node] = dictionary[node] + [node]

        for near in grafo.neighbors(node):

            if node == end:

                return dictionary[node]

            if near not in explored:

                explored.append(near)
                dictionary[near] = dictionary[node]
                frontier.append(near)
    return []
