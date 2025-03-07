class Client:

    def __init__(self,id_client,nume,cnp):
        self.__id_client=id_client
        self.__nume=nume
        self.__cnp=cnp

    def get_id_client(self):
        return self.__id_client
    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp
#-----------------------------------------getteri
    def set_id_client(self,id_nou):
        self.__id_client=id_nou

    def set_nume(self,nume_nou):
        self.__nume=nume_nou

    def set_cnp(self,cnp_nou):
        self.__cnp=cnp_nou
#-----------------------------------------setteri
    def __str__(self):
        return "Client " + str(self.get_id_client()) + "\nNume: " + self.get_nume() + "\nCNP: " + str(self.get_cnp()) + "\n"
