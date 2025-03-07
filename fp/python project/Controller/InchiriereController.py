from Domeniu.Inchiriere import Inchiriere
from functools import cmp_to_key
class InchiriereController:
    def __init__(self,inchiriere_repository,carte_repository,client_repository):
        self.__inchiriere_repository=inchiriere_repository
        self.__carte_repository=carte_repository
        self.__client_repository=client_repository


    def get_all(self):
        return self.__inchiriere_repository.get_all()

    def adauga(self,id,id_carte,id_client):
        inchiriere = Inchiriere(id,id_carte,id_client)
        self.__inchiriere_repository.adauga(inchiriere)

    def scoate(self,id_carte,id_client):
        self.__inchiriere_repository.scoate(id_carte,id_client)

    def exista_inchiriere_carte(self,id_carte):
        return self.__inchiriere_repository.exista_inchiriere_carte(id_carte)

    def returneaza_clienti_cu_carti_inchiriate(self):
        dictionar = {}
        inchirieri = self.get_all()
        carti = self.__carte_repository.get_all()
        for carte in carti:
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] = 0

        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] += 1

        dictionar_sortat = sorted(dictionar.items(), key=lambda d: (d[1], d[0]))
        return dictionar_sortat

    def returneaza_clienti_cu_carti_inchiriate_insertion_sort(self):
        dictionar = {}
        inchirieri = self.get_all()
        carti = self.__carte_repository.get_all()

        for carte in carti:
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] = 0

        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] += 1

        # Convert dictionary items to a list of tuples
        dictionar_items = list(dictionar.items())

        # Use the insertion_sort method to sort the list
        self.insertion_sort(dictionar_items, key=lambda d: (d[1], d[0]))

        return dictionar_items

    def returneaza_clienti_cu_carti_inchiriate_comb_sort(self):
        dictionar = {}
        inchirieri = self.get_all()
        carti = self.__carte_repository.get_all()

        for carte in carti:
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] = 0

        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] += 1

        # Convert dictionary items to a list of tuples
        dictionar_items = list(dictionar.items())

        # Use the comb_sort method to sort the list
        self.comb_sort(dictionar_items, key=lambda d: (d[1], d[0]))

        return dictionar_items

    def inchiriaza_carte(self, id_inchiriere, id_carte, id_client):
        if self.__carte_repository.gaseste_carte_dupa_id(id_carte) == -1 or self.__client_repository.gaseste_client_dupa_id(id_client) == -1:
            raise KeyError("Cartea sau clientul inchirierii nu exista!")
        elif self.exista_inchiriere_carte(id_carte):
            raise KeyError("Cartea este deja inchiriata!")
        else:
            self.__inchiriere_repository.inchiriaza_carte(id_inchiriere, id_carte, id_client)

    def returneaza_carte(self, id_inchiriere):
        self.__inchiriere_repository.returneaza_carte(id_inchiriere)



    def cele_mai_inchiriate_carti(self):
        dictionar_carte_client = {}
        inchirieri = self.get_all()

        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()

            if nume_carte not in dictionar_carte_client:
                dictionar_carte_client[nume_carte] = 1
            else:
                dictionar_carte_client[nume_carte] += 1

        def compare(x, y):
            if x[1] == y[1]:
                return 0
            elif x[1] < y[1]:
                return -1
            else:
                return 1

        dictionar_carte_client_sortat = sorted(dictionar_carte_client.items(),key=cmp_to_key(compare),reverse=True)
        return dictionar_carte_client_sortat



    def cele_mai_inchiriate_carti_comb_sort(self):
        dictionar_carte_client = {}
        inchirieri = self.get_all()
        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            if nume_carte not in dictionar_carte_client:
                dictionar_carte_client[nume_carte] = 1
            else:
                dictionar_carte_client[nume_carte] += 1

        # Convert dictionary items to a list of tuples
        dictionar_carte_client_items = list(dictionar_carte_client.items())

        def compare(x, y):
            if x[1] == y[1]:
                return 0
            elif x[1] < y[1]:
                return -1
            else:
                return 1
        # Use the comb_sort method to sort the list
        self.comb_sort(dictionar_carte_client_items, key=cmp_to_key(compare), reverse=True)

        return dictionar_carte_client_items

    def cele_mai_inchiriate_carti_insertion_sort(self):
        dictionar_carte_client = {}
        inchirieri = self.get_all()
        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            if nume_carte not in dictionar_carte_client:
                dictionar_carte_client[nume_carte] = 1
            else:
                dictionar_carte_client[nume_carte] += 1

        # Convert dictionary items to a list of tuples
        dictionar_carte_client_items = list(dictionar_carte_client.items())

        # Use the insertion_sort method to sort the list
        self.insertion_sort(dictionar_carte_client_items, key=lambda d: (d[1], d[0]), reverse=True)

        return dictionar_carte_client_items

    def primele10_cele_mai_putin(self):
        dictionar = {}
        inchirieri = self.get_all()
        carti = self.__carte_repository.get_all()

        for carte in carti:
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] = 0

        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] += 1

        dictionar_sortat = sorted(dictionar.items(), key=lambda d: (d[1], d[0]))
        return dictionar_sortat

    def primele10_cele_mai_putin_insertion_sort(self):
        dictionar = {}
        inchirieri = self.get_all()
        carti = self.__carte_repository.get_all()

        for carte in carti:
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] = 0

        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] += 1
        dictionar_items = list(dictionar.items())
        self.insertion_sort(dictionar_items, key=lambda d: (d[1], d[0]))
        primele_10_cele_mai_putin = dictionar_items[:10]
        return primele_10_cele_mai_putin


    def insertion_sort(self,lista, key=None, reverse=False):
        """
        Metoda de sortare "Insertion Sort".

        :param lista: Lista de elemente de sortat.
        :param key: Funcția cheie pentru extragerea valorii cheie pentru sortare (opțional).
        :param reverse: Indicator pentru sortare inversă (True pentru sortare descrescătoare, False pentru sortare crescătoare).
        """
        for i in range(1, len(lista)):
            valoare_curenta = lista[i]
            pozitie = i

            while pozitie > 0 and (key(valoare_curenta) if key else valoare_curenta) < (
            key(lista[pozitie - 1]) if key else lista[pozitie - 1]):
                lista[pozitie] = lista[pozitie - 1]
                pozitie -= 1

            lista[pozitie] = valoare_curenta

        if reverse:
            lista.reverse()

    def comb_sort(self,lista, key=None, reverse=False):
        """
        Metoda de sortare "Comb Sort".

        :param lista: Lista de elemente de sortat.
        :param key: Funcția cheie pentru extragerea valorii cheie pentru sortare (opțional).
        :param reverse: Indicator pentru sortare inversă (True pentru sortare descrescătoare, False pentru sortare crescătoare).
        """

        def get_gap(gap):
            # Funcție auxiliară pentru calculul intervalului (gap) în comb sort
            gap = (gap * 10) // 13
            return max(gap, 1)

        n = len(lista)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            gap = get_gap(gap)
            swapped = False

            for i in range(0, n - gap):
                if (key(lista[i]) if key else lista[i]) > (key(lista[i + gap]) if key else lista[i + gap]):
                    lista[i], lista[i + gap] = lista[i + gap], lista[i]
                    swapped = True

        if reverse:
            lista.reverse()

    def primele10_cele_mai_putin_comb_sort(self):
        dictionar = {}
        inchirieri = self.get_all()
        carti = self.__carte_repository.get_all()

        for carte in carti:
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] = 0

        for inchiriere in inchirieri:
            id_carte = inchiriere.get_id_carte()
            carte = self.__carte_repository.gaseste_carte_dupa_id1(id_carte)
            nume_carte = carte.get_titlu()
            dictionar[nume_carte] += 1

        # Convert dictionary items to a list of tuples
        dictionar_items = list(dictionar.items())

        # Use the comb_sort method to sort the list
        self.comb_sort(dictionar_items, key=lambda d: (d[1], d[0]))

        # Get the first 10 items (cele mai putin inchiriate)
        primele_10_cele_mai_putin_comb_sort = dictionar_items[:10]

        return primele_10_cele_mai_putin_comb_sort