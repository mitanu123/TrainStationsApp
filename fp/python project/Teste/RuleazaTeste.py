from Domeniu.Carte import Carte
from Domeniu.Client import Client
from Domeniu.Inchiriere import Inchiriere
from Repository.CarteRepository import CarteRepository
from Repository.ClientRepository import ClientRepository
from Repository.InchiriereRepository import InchiriereRepository
from Controller.ClientController import ClientController
from Controller.CarteController import CarteController
from Controller.InchiriereController import InchiriereController

class Test:
    def __init__(self):
        self.carte_repository = CarteRepository()
        self.client_repository = ClientRepository()
        self.inchiriere_repository = InchiriereRepository(self.carte_repository, self.client_repository)
        self.carte_controller = CarteController(self.carte_repository)
        self.client_controller = ClientController(self.client_repository)
        self.inchiriere_controller = InchiriereController(self.inchiriere_repository,self.carte_repository,self.client_repository)

    def test_adauga_carte(self):
        # Testare adăugare carte
        carte = Carte(1,"Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        assert len(self.carte_repository.get_all()) == 0
        self.carte_repository.adauga(carte)
        id_carte = carte.get_idcarte()
        assert self.carte_repository.get_carte_byid(id_carte) == carte
        assert carte.get_titlu() == "Harry Potter"
        assert carte.get_descriere() == "Fantasy masterpiece"
        assert carte.get_autor() == "J.K.Rrowling"
        assert len(self.carte_repository.get_all()) == 1

    def test_sterge_carte(self):
        # Testare ștergere carte
        self.carte_repository.sterge(1)
        assert len(self.carte_repository.get_all()) == 0


    def test_modifica_carte(self):
        # Testare modificare carte
        carte = Carte(1,"Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        self.carte_repository.modifica(carte.get_idcarte(), "Harry Potter 2", "Fantasy sequel 2", "J.K.Rowling 2")
        assert carte.get_titlu() == "Harry Potter 2"
        assert carte.get_descriere() == "Fantasy sequel 2"
        assert carte.get_autor() == "J.K.Rowling 2"


    def test_adauga_client(self):
        # Testare adaugare client
        client = Client(1,"John Doe", "1234567890")
        self.client_repository.adauga(client)
        assert client.get_nume() == "John Doe"
        assert client.get_cnp() == "1234567890"
        # Testare că lista de clienți s-a actualizat corespunzător
        assert len(self.client_repository.get_all()) == 1



    def test_sterge_client(self):
        # Testare ștergere client
        self.client_repository.sterge(1)
        assert len(self.client_repository.get_all()) == 0



    def test_modifica_client(self):
        # Testare modificare client
        client = Client(1,"John Doe", "1234567890")
        self.client_repository.adauga(client)

        self.client_repository.modifica(client.get_id_client(), "Jane Doe", "9876543210")
        assert client.get_nume() == "Jane Doe"
        assert client.get_cnp() == "9876543210"

    def test_inchiriere_carte(self):
        inchiriere = Inchiriere(1,1,1)
        self.inchiriere_repository.adauga(inchiriere)
        assert len(self.inchiriere_repository.get_all()) == 1


    def test_returnare_carte(self):
        # Testare returnare carte
        self.inchiriere_repository.scoate(1, 1)
        assert len(self.inchiriere_repository.get_all()) == 0

    def test_cele_mai_inchiriate_carti(self):
        inchiriere1 = Inchiriere(1,1, 1)
        inchiriere_repository = InchiriereRepository(self.carte_repository,self.client_repository)
        inchiriere_repository.adauga(inchiriere1)
        inchiriere_controller = InchiriereController(inchiriere_repository,self.carte_repository,self.client_repository)

        dictionar_carte_client_sortat = inchiriere_controller.cele_mai_inchiriate_carti_comb_sort()
        assert dictionar_carte_client_sortat == [("Harry Potter 2", 1)]

    def test_clienti_cu_carti_inchiriate_ordonat(self):
        carte = Carte(5,"Harry Potter 3", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        inchiriere = Inchiriere(1,5,1)
        self.inchiriere_repository.adauga(inchiriere)
        inchiriere_controller = InchiriereController(self.inchiriere_repository, self.carte_repository,self.client_repository)
        dictionar = inchiriere_controller.returneaza_clienti_cu_carti_inchiriate_insertion_sort()
        assert dictionar == [("Harry Potter 2",0),("Harry Potter 3",1)]

    def test_primii20_cei_mai_activi(self):
        inchiriere_controller = InchiriereController(self.inchiriere_repository, self.carte_repository,self.client_repository)
        dictionar = inchiriere_controller.primele10_cele_mai_putin_insertion_sort()
        assert dictionar == [("Harry Potter 2",0),("Harry Potter 3",1)]


def rulare_teste():

    test = Test()
    test.test_adauga_carte()
    test.test_sterge_carte()
    test.test_modifica_carte()
    test.test_adauga_client()
    test.test_sterge_client()
    test.test_modifica_client()
    test.test_inchiriere_carte()
    test.test_returnare_carte()
    test.test_cele_mai_inchiriate_carti()
    test.test_clienti_cu_carti_inchiriate_ordonat()
    test.test_primii20_cei_mai_activi()
    print("Testetele au trecut cu succes !")


rulare_teste()

