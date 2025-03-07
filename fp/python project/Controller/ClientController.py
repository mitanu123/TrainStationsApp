from Domeniu.Client import Client
class ClientController:
    def __init__(self,repository):
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def adauga(self,id_client,nume,cnp):
        client = Client(id_client,nume,cnp)
        self.__repository.adauga(client)

    def sterge(self,id_client):
        self.__repository.sterge(id_client)

    def modifica(self,id_client,nume_nou,cnp_nou):
        self.__repository.modifica(id_client,nume_nou,cnp_nou)