class Carte:
    def __init__(self, id_carte, titlu, descriere, autor):
        self.__id_carte = id_carte
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor

    def get_idcarte(self):
        return self.__id_carte

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_autor(self):
        return self.__autor

    # ------------------------------------------getteri
    def set_id_carte(self, id_nou):
        self.__id_carte = id_nou

    def set_titlu(self, titlu_nou):
        self.__titlu = titlu_nou

    def set_descriere(self, descriere_noua):
        self.__descriere = descriere_noua

    def set_autor(self, autor_nou):
        self.__autor = autor_nou

    # -------------------------------------------setteri

    def __str__(self):
        return "Carte: " + str(
            self.get_idcarte()) + "\nTitlu: " + self.get_titlu() + "\nDescriere: " + self.get_descriere() + "\nAutor: " + self.get_autor() + "\n"
