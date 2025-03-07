from Domeniu.Carte import Carte
class CarteController:
    def __init__(self,repository):
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def adauga(self,id_carte,titlu,descriere,autor):
        carte=Carte(id_carte,titlu,descriere,autor)
        self.__repository.adauga(carte)

    def sterge(self,id_carte):
        self.__repository.sterge(id_carte)

    def modifica(self,id_carte,titlu,descriere,autor):
        carte = Carte(id_carte,titlu,descriere,autor)
        self.__repository.modifica(id_carte,titlu,descriere,autor)