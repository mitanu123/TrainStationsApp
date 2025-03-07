from Domeniu.Client import Client
from Repository.ClientRepository import ClientRepository

class ClientFileRepository(ClientRepository):

    def __init__(self,nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()

    def adauga(self,client):
        super().adauga(client)
        self.scrie_in_fisier()

    def modifica(self,client):
        super().modifica(client)
        self.scrie_in_fisier()

    def sterge(self,id):
        super().sterge(id)
        self.scrie_in_fisier

    def citeste_din_fisier(self):
        try:
            with open(self.__nume_fisier, "r") as f:
                linie = f.readline().strip("\n")
                while linie != "":
                    lista_atribute = linie.split(",")
                    id = int(lista_atribute[0])
                    nume = lista_atribute[1]
                    cnp = lista_atribute[2]
                    client = Client(id, nume, cnp)
                    self.adauga(client)
                    linie = f.readline().strip("\n")
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__nume_fisier)

    def scrie_in_fisier(self):
        try:
            with open(self.__nume_fisier, "w") as f:
                lista_clienti = super().get_all()
                for client in lista_clienti:
                    id = client.get_id_client()
                    nume = client.get_nume()
                    cnp = client.get_cnp()
                    linie = str(id) + "," + nume + "," + str(cnp) + "\n"
                    f.write(linie)
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__nume_fisier)