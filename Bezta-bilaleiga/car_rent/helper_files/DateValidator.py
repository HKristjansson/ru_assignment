# The purpose of this py program is to be able to call a validation of day input, from various places in the UI.
import datetime
class DateValidator:
    def __init__(self):
    
        """ self.__Vehicle_service = VehicleService()
        self.__Customer_service = CustomerService()
        self.__Ord_service = OrdService()
        self.__Setup_service = SetupService()
        self.__Vehicle_service = VehicleService()
         """
        #self.__Setup_service = SetupService()
        





    def date_valid(self):
        inp_d = input('Dagur: ')
        inp_month = input("Mánuður : ")
        inp_year = input("Ár: ")
        #date_string = '2017-12-31'
        #date_string = inp_year + '-' + inp_month + '-' + inp_d
        date_string = inp_d + "." + inp_month + "."+ inp_year
        #date_format = '%Y-%m-%d'
        date_format = '%d.%m.%Y'
        try:
            date_obj = datetime.datetime.strptime(date_string, date_format)
            print(date_obj)
        except ValueError:
            print("Óleyfileg dagsetning slegin inn, reyndu aftur: ")
            date_valid(self)

    date_valid(self)
