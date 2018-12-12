class Ord:
    #def __init__(self, orderno, customerno, license_plate,start_location,order_date,first_day_of_rent,return_location,last_day_of_rent,payment_method,card_number,basic_insurance,xtra_insurance,comments):
    def __init__(self, order_dict):
        self.__order_id = order_dict["ORDER_ID"]
        
        self.__customerno = order_dict["CUSTOMER_ID"]
        self.__license_plate_no = order_dict["LICENCE_PLATE_NUMBER"]
        self.__start_location = order_dict["CAR_LOCATION_START"]
        self.__return_location = order_dict["CAR_LOCATION_END"]
        self.__order_registration_date = order_dict["ORDER_REGISTRATION_DATE"]
        self.__first_day_of_rent = order_dict["FIRST_DAY_OF_RENT"]
        self.__last_day_of_rent = order_dict["LAST_DAY_OF_RENT"]
        self.__payment_type = order_dict["PAYMENT_TYPE"]
        self.__order_status = order_dict["ORDER_STATUS"]
        self.__comments = order_dict["COMMENTS"]
        self.__card_number = order_dict["CARD_NO"]
        self.__basic_insurance = order_dict["INSURANCE_BASIC"]
        self.__xtra_insurance = order_dict["INSURANCE_XTRA"]


    def __str__(self):
        #return "{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.__orderno, self.__customerno, self.__license_plate,self.__start_location,self.__order_date,self.__first_day_of_rent,self.__return_location,self.__last_day_of_rent,self.__payment_method,self.__card_number,self.__basic_insurance,self.__xtra_insurance,self.__comments)
        return "{},{},{}{},{},{},{},{},{},{},{},{},{},{}".format(self.__order_id,self.__customerno, self.__license_plate_no,
            self.__start_location,self.__return_location,self.__order_registration_date,
            self.__first_day_of_rent,self.__last_day_of_rent,self.__payment_type,
            self.__order_status,self.__comments,self.__card_number,self.__basic_insurance,
            self.__xtra_insurance)
        
    def __repr__(self):
        return self.__str__()
            

    def get_order_id(self):
        return self.__order_id
    
    def get_customerno(self):
        return self.__customerno
    
    def get_license_plate_no(self):
        return self.__license_plate_no

    def get_start_location(self):
        return self.__start_location

    def get_order_registration_date(self):
        return self.__order_registration_date

    def get_first_day_of_rent(self):
        return self.__first_day_of_rent

    def get_last_day_of_rent(self):
        return self.__last_day_of_rent

    def get_return_location(self):
        return self.__return_location

    def get_payment_type(self):
        return self.__payment_type   

    def get_card_number(self):
        return self.__card_number
    
    def get_basic_insurance(self):
        return self.__basic_insurance

    def get_xtra_insurance(self):
        return self.__xtra_insurance        

    def get_order_status(self):
        return self.__order_status

    def get_comments(self):
        return self.__comments    
    
   

 

    
    




