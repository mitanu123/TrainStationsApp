import random
import string

class UI:
    def __init__(self,carte_controller,client_controller,inchiriere_controller,carte_repository,client_repository):
        self.__carte_controller = carte_controller
        self.__client_controller = client_controller
        self.__inchiriere_controller = inchiriere_controller
        self.__carte_repository = carte_repository
        self.__client_repository = client_repository

    def returneaza_meniu(self):
        meniul_meu="\nMeniu:\n"
        meniul_meu+="1.Adauga carte\n"
        meniul_meu+="2.Adauga client\n"
        meniul_meu+="3.Afiseaza cartile\n"
        meniul_meu+="4.Afiseaza clientii\n"
        meniul_meu+="5.Sterge lista de carti\n"
        meniul_meu+="6.Sterge lista de clienti\n"
        meniul_meu+="7.Modifica lista de carti\n"
        meniul_meu+="8.Modifica lista de clienti\n"
        meniul_meu+="9.Cauta carte\n"
        meniul_meu+="10.Cauta client\n"
        meniul_meu+="11.Inchiriaza carte\n"
        meniul_meu+="12.Returneaza carte\n"
        meniul_meu+="13.Vezi clientii cu carti inchiriate ordonat\n"
        meniul_meu+="14.Afiseaza inchiriierile\n"
        meniul_meu+="15.Cele mai inchiriate carti\n"
        meniul_meu+="16.Primii 20% dintre cei mai activi clienti\n"
        meniul_meu+="17.Primele 10% cele mai putin inchiriate carti ordonate crescator dupa numarul de inchirieri si alfabetic dupa numele autorului\n"
        meniul_meu+="0.Iesire\n"
        return meniul_meu

    def main(self):
        ruleaza=True
        while ruleaza:
            meniul_meu = self.returneaza_meniu()
            print(meniul_meu)
            comanda = input("Introduceti comanda:")
            if comanda == "1":
                self.ui_adauga_carte()
            elif comanda == "2":
                self.ui_adauga_client()
            elif comanda == "3":
                self.ui_tipareste_carti()
            elif comanda == "4":
                self.ui_tipareste_clienti()
            elif comanda == "5":
                self.ui_sterge_carti()
            elif comanda == "6":
                self.ui_sterge_clienti()
            elif comanda == "7":
                self.ui_modifica_carte()
            elif comanda == "8":
                self.ui_modifica_client()
            elif comanda == "9":
                self.ui_cauta_carte()
            elif comanda == "10":
                self.ui_cauta_client()
            elif comanda == "11":
                self.ui_inchiriaza_carte()
            elif comanda == "12":
                self.ui_returneaza_carte()
            elif comanda == "13":
                self.ui_clienti_cu_carti_inchiriate()
            elif comanda == "14":
                self.ui_afiseaza_inchirieri()
            elif comanda == "15":
                self.ui_cele_mai_inchiriate_carti()
            elif comanda == "16":
                self.ui_primii_20()
            elif comanda == "17":
                self.ui_primele10_cele_mai_putin()
    def ui_afiseaza_inchirieri(self):
        lista_inchirieri = self.__inchiriere_controller.get_all()
        for i in lista_inchirieri:
            print(i)
    def ui_adauga_carte(self):
        try:
            #id = int(input("Introduceti ID-ul cartii:"))#self.ui_idgenerator
            #titlu = input("Introduceti titlul cartii:")
            #descriere = input("Introduceti descrierea cartii:")
            #autor = input("Introduceti autorul:")
            id = self.ui_id_generator()
            titlu = self.ui_nume_generator()
            descriere = self.ui_nume_generator()
            autor = self.ui_nume_generator()
            self.__carte_controller.adauga(id,titlu,descriere,autor)
        except ValueError:
            print("Date gresite! Reincercati!")
        #except DuplicateIDException as de:
         #   print(de)
        #except IOError as ioe:
         #   print(ioe)
        #except ValueError:
         #   print("Date gresite ! Reincercati !")
        #except KeyError as ke:
         #   print(ke)

    def ui_adauga_client(self):
        try:
            #id = int(input("Introduceti ID-ul clientului:"))
            #nume = input("Introduceti numele clientului:")
            #cnp = int(input("Introduceti cnp-ul clientului: "))
            id = self.ui_id_generator()
            nume = self.ui_nume_generator()
            cnp = self.ui_cnp_generator()
            self.__client_controller.adauga(id,nume,cnp)
        except ValueError:
            print("Date gresite ! Rincercati !")
        except KeyError as ke:
            print(ke)

    def ui_tipareste_carti(self):
        carti = self.__carte_controller.get_all()
        if len(carti) == 0:
            print("Lista de carti.txt este goala !")
        for carte in carti:
            print(carte)

    def ui_tipareste_clienti(self):
        clienti = self.__client_controller.get_all()
        if len(clienti) == 0:
            print("Lista de clienti este goala !")
        for client in clienti:
            print(client)

    def ui_sterge_carti(self):
        try:
            id = int(input("Introduceti id-ul cartii pe care doriti sa o stergeti:"))
            if self.__inchiriere_controller.exista_inchiriere_carte(id) == True:
                print("Exista deja o inchiriere ")
            else:
                self.__carte_controller.sterge(id)
        except ValueError:
            print("Date gresite ! Reincercati !")
        except KeyError as ke:
            print(ke)

    def ui_sterge_clienti(self):
        try:
            id = int(input("Introduceti id-ul clientului pe care doriti sa o stergeti:"))
            self.__client_controller.sterge(id)
        except ValueError:
            print("Date gresite ! Reincercati !")
        except KeyError as ke:
            print(ke)

    def ui_modifica_carte(self):
        try:
            id = int(input("Introduceti id-ul cartii pe care doriti sa o modificati:"))
            titlu_nou = input("Introduceti titlu nou:")
            descriere_noua = input("Introduceti descriere noua:")
            autor_nou = input("Introduceti noul autor:")
            self.__carte_controller.modifica(id,titlu_nou,descriere_noua,autor_nou)
        except ValueError:
            print("Date gresite ! Reincercati !")
        except KeyError as ke:
            print(ke)

    def ui_modifica_client(self):
        try:
            id = int(input("Introduceti id-ul clientului pe care doriti sa il modificati:"))
            nume_nou = input("Introduceti nume nou:")
            cnp_nou = input("Introduceti cnp-ul nou:")
            self.__client_controller.modifica(id,nume_nou,cnp_nou)
        except ValueError:
            print("Date gresite ! Reincercati !")
        except KeyError as ke:
            print(ke)

    def ui_clienti_cu_carti_inchiriate(self):
        try:
            carti = self.__inchiriere_controller.returneaza_clienti_cu_carti_inchiriate()
            print(carti)
        except ValueError:
            print("Date gresite ! Reincercati !")

    def ui_cauta_carte(self):
        try:
            id_carte = int(input("Introduceti ID-ul cartii pentru cautare: "))
            carte_gasita = self.__carte_repository.gaseste_carte_dupa_id1_recursiv(id_carte)

            if carte_gasita is not None:
                print("\nCarte gasita:\n", carte_gasita)
            else:
                print("\nNu s-a gasit nicio carte cu acest ID.")

        except ValueError:
            print("\nID-ul introdus nu este valid. Reincercati!")

    def ui_cauta_client(self):
        try:
            id_client = int(input("Introduceti ID-ul clientului pentru cautare: "))
            client_gasit = self.__client_repository.gaseste_client_dupa_id1(id_client)
            if client_gasit is not None:
                print("\nClient gasit:\n", client_gasit)
            else:
                print("\nNu s-a gasit niciun client cu acest ID.")

        except ValueError:
            print("\nID-ul introdus nu este valid. Reincercati!")

    def ui_inchiriaza_carte(self):
        try:
            id_inchiriere = int(input("Introduceti ID-ul inchirierii: "))
            id_carte = int(input("Introduceti ID-ul cartii: "))
            id_client = int(input("Introduceti ID-ul clientului: "))
            self.__inchiriere_controller.adauga(id_inchiriere, id_carte, id_client)
            print("Inchiriere realizata cu succes!")
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)

    def ui_returneaza_carte(self):
        try:
            id_carte = int(input("Introduceti ID-ul cartii pe care o returnati:"))
            id_client = int(input("Introduceti ID-ul clientului care returneaza cartea:"))
            self.__inchiriere_controller.scoate(id_carte,id_client)
            print("Carte returnata cu succes!")
        except ValueError:
            print("Date gresite! Reincercati!")
        except KeyError as ke:
            print(ke)

    def ui_cele_mai_inchiriate_carti(self):
        cele_mai_inchiriate_carti = self.__inchiriere_controller.cele_mai_inchiriate_carti() #comb_sort/insertion_sort
        print(cele_mai_inchiriate_carti)

    def ui_primii_20(self):
        try:
            numar_clienti = int(input("Introduceti numarul de clienti pe care doriti sa ii afisati:"))
            #numar_clienti = int(0.2 * len(self.__lista_clienti)
            carti = self.__inchiriere_controller.returneaza_clienti_cu_carti_inchiriate_comb_sort()#comb_sort/insertion_sort
            print(carti[:numar_clienti])
        except ValueError:
            print("Date gresite ! Reincercati !")

    def ui_nume_generator(self,size = 6,chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def ui_id_generator(self):
        id = random.randint(100,1000)
        return id

    def ui_cnp_generator(self):
        cnp = random.randint(3000000000000,5000000000000)
        return cnp

    def ui_primele10_cele_mai_putin(self):
        try:
            numar_carti = int(input("Introduceti numarul de carti.txt pe care doriti sa il afisati:"))
            #numar_carti = int(0.1*len(self.__lista.inchirieri))
            carti = self.__inchiriere_controller.primele10_cele_mai_putin_insertion_sort()#"_comb_sort"
            print(carti[:numar_carti])
        except ValueError:
            print("Date gresite. Reincercati !")