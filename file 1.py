

# Esercizio 1
#
# Scrivere una funzione massimo(a,b) che prende due numeri come parametri e restituisce:
# 1 se a è più grande di b
# -1 se b è più grande di a
# 0 se sono uguali


def massimo(a = 0 ,b = 0):

    if type(a) == type("str") or type(b) == type("str"):

        print("Hai inserito una stringa. Devi inserire un numero")

    else:

        if a > b:

            return 1

        elif a < b:

            return -1

        elif a == b:

            return 0


# Esercizio 2
#
# Scrivi una funzione moltiplicatrice(lista_numeri) che data una lista di numeri,
# moltiplica tra loro tutti gli elementi della lista e ne restituisce il risultato.
# Se la lista è vuota restituisce 0.


def moltiplicatrice(lista_numeri = []):

    x = 0

    if type(lista_numeri) != type([]):

        return "Error: Il parametro inserito non è una lista!"

    else:

        if len(lista_numeri) == 0:

            return 0

        else:

            for index in range(len(lista_numeri)):

                x += lista_numeri[index]

            return x


# Esercizio 3
#
# Scrivi una funzione rovescia(stringa). La funzione accetta come parametro una stringa e restituisce la stringa
# dopo averla trasformato in minuscolo tutti i caratteri e in maiuscolo solo il primo carattere
# (ad esempio "abcd" diventa "dcbA"). Gestire anche il caso stringa vuota.


def rovescia(stringa = ""):

    x = ""

    if type(stringa) != type("str"):

        return "Error: Il parametro inserito non è una stringa!"

    else:

        if stringa == "":

            return "Error: Stringa vuota!"

        else:

            for index in reversed(range(len(stringa))):

                if index == 0:

                    x += stringa[index].upper()

                else:

                    x += stringa[index].lower()

            return x


# Esercizio 4
#
# Scrivi una funzione frequenza(stringa). La funzione riceve una stringa come parametro e restituisce un dizionario
# rappresentante la frequenza di ciascun carattere componente la stringa.
# Ad esempio, data una stringa "ababcc", la funzione restituisce in risultato {"a": 2, "b": 2, "c": 2}.


def frequenza(stringa = ""):

    dizionario = {}

    if type(stringa) != type("str"):

        return "Error: Il parametro inserito non è una stringa!"

    else:

        for index in range(len(stringa)):

            if stringa[index] not in dizionario:

                dizionario[stringa[index]] = 1

            else:

                dizionario[stringa[index]] += 1

        return dizionario
