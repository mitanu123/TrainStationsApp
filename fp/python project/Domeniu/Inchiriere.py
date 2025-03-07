class Inchiriere:
    def __init__(self,id,id_carte,id_client):
        self.__id=id
        self.__id_carte=id_carte
        self.__id_client=id_client

    def get_id(self):
        return self.__id

    def get_id_carte(self):
        return self.__id_carte

    def get_id_client(self):
        return self.__id_client

    def set_id(self,id_nou):
        self.__id=id_nou

    def set_id_carte(self,id_carte_nou):
        self.__id_carte=id_carte_nou

    def set_id_client(self,id_client_nou):
        self.__id_client=id_client_nou

    def __str__(self):
        return "Inchiriere: " + str(self.get_id()) + "\n" +\
            "ID Carte: " + str(self.get_id_carte()) + "\n" +\
            "ID Client: " + str(self.get_id_client()) + "\n"