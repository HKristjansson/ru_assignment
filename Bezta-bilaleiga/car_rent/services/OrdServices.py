from repositories.OrdRepository import OrdRepository

class OrdService:
    def __init__(self):
        self.__Ord_repo = OrdRepository()

    def add_Ord(self, Ord):
        if self.is_valid_Ord(Ord):
            self.__Ord_repo.add_Ord_csv(Ord)
            
    def is_valid_Ord(self, Ord):
        #here should be some code to 
        #validate the Ord
        #self.__license_plate = license_plate
        #lic_no = Order.get_license_plate_no()        
        return True

    def get_order_no(self):
        return self.__Ord_repo.get_Ord()

    def get_order_status_change(self,param):        
        return self.__Ord_repo.order_status_change(param)

    def get_order_by_number(self, order_number):
        return self.__Ord_repo.get_ord_by_number(order_number)

    def get_vehicle_history(self,plate_numb):
        return self.__Ord_repo.get_vehicle_history(plate_numb)
    
    def get_customer_history(self,customer_id):
        return self.__Ord_repo.get_customer_history(customer_id)




    