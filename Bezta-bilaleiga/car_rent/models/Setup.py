class Setup:
    #def __init__(self, Setuperno, customerno, license_plate,start_location,Setuper_date,start_date,return_location,return_date,payment_method,card_number,basic_insurance,xtra_insurance,comments):
    def __init__(self, setup_dict):
        self.__user_id = setup_dict["USER"]
        self.__pwd = setup_dict["PWD"]
        self.__ssn = setup_dict["SSN"]
        self.__name =setup_dict["NAME"]
        self.__address=  setup_dict["ADDRESS"]
        self.__phone_no = setup_dict["PHONE_NO"]
        self.__e_mail = setup_dict["E_MAIL"] 
        self.__active = setup_dict["ACTIVE"] 
        self.__comment = setup_dict["COMMENT"] 


    def __str__(self):
        #return "{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.__Setuperno, self.__customerno, self.__license_plate,self.__start_location,self.__Setuper_date,self.__start_date,self.__return_location,self.__return_date,self.__payment_method,self.__card_number,self.__basic_insurance,self.__xtra_insurance,self.__comments)
        return "{},{},{},{},{},{},{},{},{}".format(self.__user_id,self.__pwd, self.__ssn,self.__name,self.__address,self.__phone_no,self.__e_mail,self.__active,self.__comment)
        
    def __repr__(self):
        return self.__str__()
            

    def get_user_id(self):
        return self.__user_id
    
    def get_pwd(self):
        return self.__pwd
    
    def get_ssn(self):
        return self.__ssn

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_no(self):
        return self.__phone_no

    def get_e_mail(self):
        return self.__e_mail
    def get_active(self):
        return self.__active
    def get_comment(self):
        return self.__comment


        

