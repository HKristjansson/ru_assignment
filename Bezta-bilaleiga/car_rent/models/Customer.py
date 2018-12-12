class Customer:

    def __init__(self, customer_dict):
        self.__kennitala = customer_dict["KENNITALA"]
        self.__name = customer_dict["NAME"]
        self.__address = customer_dict["ADDRESS"]
        self.__post_number = customer_dict["POST_NUMBER"]
        self.__phone_number = customer_dict["PHONE_NUMBER"]
        self.__email_address = customer_dict["EMAIL_ADDRESS"]
        self.__status =customer_dict["STATUS"]
       #self.__email_address = customer_dict["EMAIL_ADDRESS"]
#Starfsmaður - customer 
#Kennitala 
#Fullt Nafn
#Heimilisfang
#Póstnúmer
#Símanúmer
#Tölvupóstfang



    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.__kennitala,self.__name,self.__address,self.__post_number,self.__phone_number,self.__email_address,self.__status)
    
    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.__name
    
    def get_kennitala(self):
        return self.__kennitala
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_address(self):
        return self.__address
    
    
    def get_post_number(self):
        return self.__post_number
    
    def get_email_address(self):
        return self.__email_address

    def get_status(self):
        return self.__status

    