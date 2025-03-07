import unittest
from Domeniu.Carte import Carte
from Domeniu.Client import Client
from Domeniu.Inchiriere import Inchiriere
from Repository.ClientRepository import ClientRepository
from Repository.CarteRepository import CarteRepository
from Repository.InchiriereRepository import InchiriereRepository
from Controller.CarteController import CarteController
from Controller.ClientController import ClientController
from Controller.InchiriereController import InchiriereController

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.carte_repository = CarteRepository()
        self.client_repository = ClientRepository()
        self.inchiriere_repository = InchiriereRepository(self.carte_repository, self.client_repository)
        self.carte_controller = CarteController(self.carte_repository)
        self.client_controller = ClientController(self.client_repository)
        self.inchiriere_controller = InchiriereController(self.inchiriere_repository, self.carte_repository, self.client_repository)

    def test_adauga_carte(self):
        # Testare adăugare carte
        carte = Carte(1, "Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.assertEqual(len(self.carte_repository.get_all()), 0)
        self.carte_repository.adauga(carte)
        id_carte = carte.get_idcarte()
        self.assertEqual(self.carte_repository.get_carte_byid(id_carte), carte)
        self.assertEqual(carte.get_titlu(), "Harry Potter")
        self.assertEqual(carte.get_descriere(), "Fantasy masterpiece")
        self.assertEqual(carte.get_autor(), "J.K.Rrowling")
        self.assertEqual(len(self.carte_repository.get_all()), 1)

    def test_sterge_carte(self):
        # Testare ștergere carte
        carte = Carte(1, "Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        self.carte_repository.sterge(1)
        self.assertEqual(len(self.carte_repository.get_all()), 0)

    def test_modifica_carte(self):
        # Testare modificare carte
        carte = Carte(1, "Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        self.carte_repository.modifica(carte.get_idcarte(), "Harry Potter 2", "Fantasy sequel 2", "J.K.Rowling 2")
        self.assertEqual(carte.get_titlu(), "Harry Potter 2")
        self.assertEqual(carte.get_descriere(), "Fantasy sequel 2")
        self.assertEqual(carte.get_autor(), "J.K.Rowling 2")

    def test_adauga_client(self):
        # Testare adaugare client
        client = Client(1, "John Doe", "1234567890")
        self.client_repository.adauga(client)
        self.assertEqual(client.get_nume(), "John Doe")
        self.assertEqual(client.get_cnp(), "1234567890")
        self.assertEqual(len(self.client_repository.get_all()), 1)

    def test_sterge_client(self):
        # Testare ștergere client
        client = Client(1,"Mario","594282980321")
        self.client_repository.adauga(client)
        self.client_repository.sterge(1)
        self.assertEqual(len(self.client_repository.get_all()), 0)

    def test_modifica_client(self):
        # Testare modificare client
        client = Client(1, "John Doe", "1234567890")
        self.client_repository.adauga(client)
        self.client_repository.modifica(client.get_id_client(), "Jane Doe", "9876543210")
        self.assertEqual(client.get_nume(), "Jane Doe")
        self.assertEqual(client.get_cnp(), "9876543210")

    def test_inchiriere_carte(self):
        carte = Carte(1, "Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        client = Client(1, "John Doe", "1234567890")
        self.client_repository.adauga(client)
        inchiriere = Inchiriere(1, 1, 1)
        self.inchiriere_repository.adauga(inchiriere)
        self.assertEqual(len(self.inchiriere_repository.get_all()), 1)

    def test_returnare_carte(self):
        # Testare returnare carte
        self.inchiriere_repository.scoate(1, 1)
        self.assertEqual(len(self.inchiriere_repository.get_all()), 0)

    def test_cele_mai_inchiriate_carti(self):
        carte = Carte(1, "Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        client = Client(1, "John Doe", "1234567890")
        self.client_repository.adauga(client)
        inchiriere1 = Inchiriere(1, 1, 1)
        inchiriere_repository = InchiriereRepository(self.carte_repository, self.client_repository)
        inchiriere_repository.adauga(inchiriere1)
        inchiriere_controller = InchiriereController(inchiriere_repository, self.carte_repository, self.client_repository)

        dictionar_carte_client_sortat = inchiriere_controller.cele_mai_inchiriate_carti()
        self.assertEqual(dictionar_carte_client_sortat, [("Harry Potter", 1)])

    def test_clienti_cu_carti_inchiriate_ordonat(self):
        carte = Carte(1, "Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        client = Client(1, "John Doe", "1234567890")
        self.client_repository.adauga(client)
        carte = Carte(5, "Harry Potter 3", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        inchiriere = Inchiriere(1, 5, 1)
        self.inchiriere_repository.adauga(inchiriere)
        inchiriere_controller = InchiriereController(self.inchiriere_repository, self.carte_repository, self.client_repository)
        dictionar = inchiriere_controller.returneaza_clienti_cu_carti_inchiriate()
        self.assertEqual(dictionar, [("Harry Potter", 0), ("Harry Potter 3", 1)])

    def test_primii20_cei_mai_activi(self):
        carte = Carte(1, "Harry Potter", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        client = Client(1, "John Doe", "1234567890")
        self.client_repository.adauga(client)
        carte = Carte(5, "Harry Potter 3", "Fantasy masterpiece", "J.K.Rrowling")
        self.carte_repository.adauga(carte)
        inchiriere = Inchiriere(1, 5, 1)
        self.inchiriere_repository.adauga(inchiriere)
        inchiriere_controller = InchiriereController(self.inchiriere_repository, self.carte_repository, self.client_repository)
        dictionar = inchiriere_controller.primele10_cele_mai_putin()
        self.assertEqual(dictionar, [("Harry Potter", 0), ("Harry Potter 3", 1)])


