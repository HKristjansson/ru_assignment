
from repositories.SetupRepository import SetupRepo
class SetupService:
    def __init__(self):
        self.__Setup_repo = SetupRepo()

    def add_Setup(self, Setup):
        if self.is_valid_Setup(Setup):
            self.__Setup_repo.add_Setup_csv(Setup)
            
    def is_valid_Setup(self, Setup):
        #here should be some code to 
        #validate the Setup
        #self.__license_plate = license_plate
        #lic_no = Setuper.get_license_plate_no()
        
        
        return True
    
    def get_Setup_No(self):
        return self.__Setup_repo.get_Setup()
            

    