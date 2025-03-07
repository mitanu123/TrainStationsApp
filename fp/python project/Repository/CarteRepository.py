class CarteRepository():
    def __init__(self):
        self.__lista_carti = []

    def get_all(self):
        return self.__lista_carti

    def get_carte_dupa_nume(self, nume_carte):
        for i in range(0, len(self._lista)):
            carte_curenta = self._lista[i]
            if carte_curenta.get_titlu() == nume_carte:
                return carte_curenta
        return None

    def gaseste_carte_dupa_id(self,id_carte):
        for i in range(0,len(self.__lista_carti)):
            carte_curenta = self.__lista_carti[i]
            if carte_curenta.get_idcarte() == id_carte:
                return i
        return -1

    def gaseste_carte_dupa_titlu(self,titlu_carte):
        for i in range(0,len(self.__lista_carti)):
            carte_curenta=self.__lista_carti[i]
            if carte_curenta.get_titlu()==titlu_carte:
                return carte_curenta
        return -1

    def gaseste_carte_dupa_id1(self,id_carte):
        for i in range(0,len(self.__lista_carti)):
            carte_curenta = self.__lista_carti[i]
            if carte_curenta.get_idcarte() == id_carte:
                return carte_curenta
        return -1


    def returneaza_carte(self, id_inchiriere):
        self.returneaza_carte(id_inchiriere)

    def get_carte_byid(self,id):
        carti = self.get_all()
        for carte in carti:
            if carte.get_idcarte() == id:
                return carte
        return None

    def sterge(self, id_carte):
        if self.gaseste_carte_dupa_id(id_carte) == -1:
            raise KeyError("Cartea cu acest ID nu exista !")
        else:
            index = self.gaseste_carte_dupa_id(id_carte)
            self.__lista_carti.pop(index)

    def adauga(self, carte):
        self.__adauga_recursiv(carte, 0, len(self.__lista_carti) - 1)

    def __adauga_recursiv(self, carte, inceput, sfarsit):
        if inceput > sfarsit:
            self.__lista_carti.insert(inceput, carte)
            return

        mijloc = (inceput + sfarsit) // 2
        carte_curenta = self.__lista_carti[mijloc]

        if carte.get_idcarte() < carte_curenta.get_idcarte():
            self.__adauga_recursiv(carte, inceput, mijloc - 1)
        elif carte.get_idcarte() > carte_curenta.get_idcarte():
            self.__adauga_recursiv(carte, mijloc + 1, sfarsit)
        else:
            raise KeyError("Exista deja o carte cu acest ID !")

    def modifica(self, id_carte, tiltu_nou, descriere_noua, autor_nou):
        self.__modifica_recursiv(id_carte, tiltu_nou, descriere_noua, autor_nou, 0, len(self.__lista_carti) - 1)

    def __modifica_recursiv(self, id_carte, tiltu_nou, descriere_noua, autor_nou, inceput, sfarsit):
        if inceput > sfarsit:
            raise KeyError("Cartea cu acest ID nu exista !")

        mijloc = (inceput + sfarsit) // 2
        carte_curenta = self.__lista_carti[mijloc]

        if id_carte < carte_curenta.get_idcarte():
            self.__modifica_recursiv(id_carte, tiltu_nou, descriere_noua, autor_nou, inceput, mijloc - 1)
        elif id_carte > carte_curenta.get_idcarte():
            self.__modifica_recursiv(id_carte, tiltu_nou, descriere_noua, autor_nou, mijloc + 1, sfarsit)
        else:
            carte_curenta.set_titlu(tiltu_nou)
            carte_curenta.set_descriere(descriere_noua)
            carte_curenta.set_autor(autor_nou)

    def gaseste_carte_dupa_id1_recursiv(self, id_carte, index=0):
        if index < len(self.__lista_carti):
            carte_curenta = self.__lista_carti[index]
            if carte_curenta.get_idcarte() == id_carte:
                return carte_curenta
            else:
                return self.gaseste_carte_dupa_id1_recursiv(id_carte, index + 1)
        else:
            return -1


"""
    def adauga(self,carte):
        id_carte = carte.get_idcarte()
        if self.gaseste_carte_dupa_id(id_carte) != -1:
            raise KeyError("Exista deja o carte cu acest ID !")
        else:
            self.__lista_carti.append(carte)

    def sterge(self,id_carte):
        if self.gaseste_carte_dupa_id(id_carte) == -1:
            raise KeyError("Cartea cu acest ID nu exista !")
        else:
            index=self.gaseste_carte_dupa_id(id_carte)
            self.__lista_carti.pop(index)

    def modifica(self,id_carte,tiltu_nou,descriere_noua,autor_nou):
        if self.gaseste_carte_dupa_id(id_carte) == -1:
            raise KeyError("Cartea cu acest ID nu exista !")
        else:
            index=self.gaseste_carte_dupa_id(id_carte)
            carte=self.__lista_carti[index]
            carte.set_titlu(tiltu_nou)
            carte.set_descriere(descriere_noua)
            carte.set_autor(autor_nou)
"""
