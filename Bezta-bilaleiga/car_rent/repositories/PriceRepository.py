import csv
from models.Price import Price
#import time # for status bar
import datetime # for clock
import os # for the cls function
#import winsound

now = datetime.datetime.now()
def cls(pm):   #######################################################################Daði, this function is also in the Salesman_UI.py program. - How do we put it in one place only, and refer it from here, an from salesmanUI?
    if pm == 'end':
        input('Ýttu á Enter til að að fara aftur í aðalval')  
    os.system('cls' if os.name=='nt' else 'clear')


class PriceRepository:
    def __init__(self):
        self.__Price = []
    
    def get_Price(self):
        cls("")
        if self.__Price == []:
            with open("data/car_class.csv", "r", encoding="UTF-8", newline = "") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=";") 
                print("╔════════════════════════════════════════════════════════════════════════════════════════╗")
                print("║Bílaleigukerfið Zúber:       Yfirlit yfir verð prentað út    ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S")                       ,   "    ║") 
                print("╠════════════════════════════════════════════════════════════════════════════════════════╣")                   
                print("║{:<30}{:<30}".format("Flokkur","Verð"),         "║") 
                print("╠════════════════════════════════════════════════════════════════════════════════════════╣")
                for line in csv_reader:
                    print("║{:<30}{:<30}".format(line[0],line[1]),"║")
                
                print("╚════════════════════════════════════════════════════════════════════════════════════════╝")  

        return self.__Price