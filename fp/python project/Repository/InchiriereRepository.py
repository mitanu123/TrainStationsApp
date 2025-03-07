class InchiriereRepository:
    def __init__(self,carte_repository,client_repository):
        self.__lista_inchirieri = []
        self.__carte_repository = carte_repository
        self.__client_repository = client_repository

    def get_all(self):
        return self.__lista_inchirieri

    def adauga(self,inchiriere):
        id=inchiriere.get_id()
        if self.gaseste_inchiriere_dupa_id(id) != -1:
            raise KeyError("Inchirierea cu acest ID exista deja !")
        else:
            id_carte = inchiriere.get_id_carte()
            id_client = inchiriere.get_id_client()
            if self.__carte_repository.gaseste_carte_dupa_id(id_carte) == -1 or self.__client_repository.gaseste_client_dupa_id(id_client) == -1:
                raise KeyError("Cartea sau clientul inchirierii nu exista !")
            elif self.gaseste_inchiriere_dupa_carte_id_si_client_id(id_client,id_carte) != -1:
                raise KeyError("Cartea cu acest id este deja inchiriata!")
            else:
                self.__lista_inchirieri.append(inchiriere)

    def scoate(self,id_carte,id_client):
        for i in  range(len(self.__lista_inchirieri)-1,-1,-1):
            inchiriere_curenta = self.__lista_inchirieri[i]
            if inchiriere_curenta.get_id_carte() == id_carte and inchiriere_curenta.get_id_client() == id_client:
                self.__lista_inchirieri.remove(inchiriere_curenta)



    def gaseste_inchiriere_dupa_id(self,id):
        for i in range(0,len(self.__lista_inchirieri)):
            inchiriere_curenta = self.__lista_inchirieri[0]
            if inchiriere_curenta.get_id() == id:
                return i
        return -1

    def gaseste_inchiriere_dupa_carte_id_si_client_id(self,id_client,id_carte):
        for i in range(0,len(self.__lista_inchirieri)):
            inchiriere_curenta = self.__lista_inchirieri[i]
            if inchiriere_curenta.get_id_carte() == id_carte and inchiriere_curenta.get_id_client() == id_client:
                return i
        return -1

    def exista_inchiriere_carte(self,id_carte):
        for i in range(0, len(self.__lista_inchirieri)):
            inchiriere_curenta = self.__lista_inchirieri[i]
            if inchiriere_curenta.get_id_carte() == id_carte:
                return True
        return False

    def gaseste_client_dupa_id(self, id_client):
        for i in range(0, len(self.__lista_clienti)):
            client_curent = self.__lista_clienti[i]
            if client_curent.get_id_client() == id_client:
                return client_curent
        return -1
