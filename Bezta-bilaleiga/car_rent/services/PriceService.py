from repositories.PriceRepository import PriceRepository

class PriceService:
    def __init__(self):
        self.__Price_repo = PriceRepository()
    
    def get_Price(self):
        return self.__Price_repo.get_Price()