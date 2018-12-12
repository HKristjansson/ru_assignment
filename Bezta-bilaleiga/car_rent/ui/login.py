from models.Setup import Setup
from services.SetupService import SetupService
import os

import csv
def cls(pm):
    if pm == 'end':
        input('Ýttu á Enter til að að fara aftur í aðalval')  
    os.system('cls' if os.name=='nt' else 'clear')

class Login:
    def __init__(self):
    
        """ self.__Vehicle_service = VehicleService()
        self.__Customer_service = CustomerService()
        self.__Ord_service = OrdService()
        self.__Setup_service = SetupService()
        self.__Vehicle_service = VehicleService()
         """
        self.__Setup_service = SetupService()



    def main_menu(self):
        action = ''
        #quitting = ''
        cls("")
        while(action != "h"):



            print("╔════════════════════════════════════════════════════════════════════════════════════╗")
            print("║----------------------------Bílaleigukerfið Zúber:----------------------------------║")
            print("╚════════════════════════════════════════════════════════════════════════════════════╝") 
            username = input("Sláðu inn notendanafn: ")
            password = input("Sláðu inn lykilorð: ")
            
            """     #for line in open("./data/access.txt", "r",encoding = "UTF-8-SIG", newline = '').readlines(): # Read the lines
            for line in open("./data/access.csv", "r",encoding = "UTF-8-SIG", newline = '').readlines(): # Read the lines
                login_info = line.split(";") # Split on the space, and store the results in a list of two strings
                if username == login_info[0] and password == login_info[1]:
                    print("Innskráning tókst")
                    return True
            print("Rangt notendanafn eða lykilorð")
            return False """
            with open('./data/access.csv','r',encoding = "UTF-8-SIG",newline = "") as setup_file:
                        csv_reader = csv.reader(setup_file,delimiter =";")
                        for line in csv_reader:
                            #print(line)
                            if (line[0] == username and line[1]== password):
                                print("Innskráning tókst")
                                print("Velkomin(n) {:<20}".format(line[3]))
                                return True

                            

                        print("Rangt notendanafn eða lykilorð")    
                        action = input("Ýttu á enter til að reyna aftur, 'h' til að hætta ")
                        if action =='h':
                          return False
                        else:
                            cls('')
                            
                