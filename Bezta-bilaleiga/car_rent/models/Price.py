class Price:
    def __init__(self, bilaflokkur, price):
        self.__bila_flokkur = Price_dict["BILA_FLOKKUR"]
        self.__price = Price_dict["VERÐ"]
    
    def __str__(self):
        return "{},{}".format(self.__bila_flokkur,self.__price)
    
    def __repr__(self):
        return self.__str__()
    
    def get_bila_flokkur(self):
        return self.__bila_flokkur()
    
    def get_price(self):
        return self.__price