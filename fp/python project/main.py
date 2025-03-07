from Repository.CarteRepository import CarteRepository
from Repository.ClientRepository import ClientRepository
from Repository.InchiriereRepository import InchiriereRepository
from Controller.CarteController import CarteController
from Controller.ClientController import ClientController
from Controller.InchiriereController import InchiriereController
from Repository.CarteFileRepository import CarteFileRepository
from Repository.ClientFileRepository import ClientFileRepository
from UI.UI import UI

carte_repository = CarteFileRepository("carti.txt")
client_repository = ClientFileRepository("clienti.txt")
inchiriere_repository = InchiriereRepository(carte_repository,client_repository)

carte_controller = CarteController(carte_repository)
client_controller = ClientController(client_repository)
inchiriere_controller = InchiriereController(inchiriere_repository,carte_repository,client_repository)

ui = UI(carte_controller,client_controller,inchiriere_controller,carte_repository,client_repository)

ui.main()