class Vehicle:

    def __init__(self, license_plate, manufacturer, subtype, vec_class, production_year,current_location,return_location,return_date,comments):
    
        #Bílnúmer,Framleiðandi,Týpuheiti,Flokkur,Árg.,Laus,Laus dags,Staðsettur,Skilastaðsetning,skiladags,Athugasemdir
        self.__license_plate = license_plate
        self.__manufacturer = manufacturer
        self.__subtype = subtype 
        self.__vec_class = vec_class
        self.__production_year = production_year
        self.__current_location = current_location
        self.__return_location = return_location
        self.__return_date = return_date
        self.__comments = comments

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.__license_plate,self.__manufacturer,self.__subtype, self.__vec_class ,self.__production_year,self.__current_location,self.__return_location,self.__return_date,self.__comments)
    
    def __repr__(self):
        return self.__str__()

    def get_license_plate(self):
        return self.__license_plate
    
    def get_manufacturer(self):
        return self.__manufacturer

    def get_subtype(self):
        return self.__subtype
    
    def get_vec_class(self):
        return self.__vec_class

    def get_production_year(self):
        return self.__production_year

    def get_current_location(self):
        return self.__current_location
    
    def get_return_location(self):
        return self.__return_location

    def get_return_date(self):
        return self.__return_date

    def get_comments(self):
        return self.__comments
