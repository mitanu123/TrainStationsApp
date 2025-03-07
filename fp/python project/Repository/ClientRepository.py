class ClientRepository:
    def __init__(self):
        self.__lista_clienti = []

    def get_all(self):
        return self.__lista_clienti

    def adauga(self,client):
        if self.gaseste_client_dupa_id(client.get_id_client()) != -1:
            raise KeyError ("Exista deja un client cu acest ID !")
        else:
            self.__lista_clienti.append(client)

    def sterge(self,id):
        if self.gaseste_client_dupa_id(id) == -1:
            raise KeyError("Nu exista un client cu acest ID !")
        else:
            client=self.gaseste_client_dupa_id(id)
            self.__lista_clienti.remove(client)

    def modifica(self,id,nume_nou,cnp_nou):
        if self.gaseste_client_dupa_id(id) == -1:
            raise KeyError("Nu exista client cu acest ID !")
        else:
            client = self.gaseste_client_dupa_id(id)
            client.set_nume(nume_nou)
            client.set_cnp(cnp_nou)


    def gaseste_client_dupa_nume(self,nume_client):
        for i in range(0,len(self.__lista_clienti)):
            client_curent=self.__lista_clienti[i]
            if client_curent.get_nume()==nume_client:
                return client_curent
        return -1

    def gaseste_client_dupa_id(self,id):
        for i in range(0,len(self.__lista_clienti)):
            client_curent=self.__lista_clienti[i]
            if client_curent.get_id_client()==id:
                return client_curent
        return -1




    def gaseste_client_dupa_id1(self,id):
        for i in range(0,len(self.__lista_clienti)):
            client_curent=self.__lista_clienti[i]
            if client_curent.get_id_client()==id:
                return client_curent
        return -1
