from Domeniu.Carte import Carte
from Repository.CarteRepository import CarteRepository

class CarteFileRepository(CarteRepository):

    def __init__(self,nume_fisier):
        super().__init__()
        self.__nume_fisier = nume_fisier
        self.citeste_din_fisier()
        self.scrie_in_fisier()

    def adauga(self,carte):
        super().adauga(carte)
        self.scrie_in_fisier()

    def modifica(self,id_carte, tiltu_nou, descriere_noua, autor_nou):
        super().modifica(id_carte, tiltu_nou, descriere_noua, autor_nou)
        self.scrie_in_fisier()

    def sterge(self,id_carte):
        super().sterge(id_carte)
        self.scrie_in_fisier()

    def citeste_din_fisier(self):
        try:
            with open(self.__nume_fisier, "r") as f:
                for linie in f:
                    lista_atribute = linie.strip("\n").split(",")
                    id = int(lista_atribute[0])
                    titlu = lista_atribute[1]
                    descriere = lista_atribute[2]
                    autor = lista_atribute[3]
                    carte = Carte(id, titlu, descriere, autor)
                    super().adauga(carte)
        except IOError:
            raise IOError("Eroare la descchiderea fisierului " + self.__nume_fisier)

    def scrie_in_fisier(self):
        try:
            with open(self.__nume_fisier, "w") as f:
                lista_carti = super().get_all()
                for carte in lista_carti:
                    id = carte.get_idcarte()
                    titlu = carte.get_titlu()
                    descriere = carte.get_descriere()
                    autor = carte.get_autor()
                    linie = str(id) + "," + titlu + "," + descriere + "," + autor + "\n"
                    f.write(linie)
        except IOError:
            raise IOError("Eroare la deschiderea fisierului " + self.__nume_fisier)