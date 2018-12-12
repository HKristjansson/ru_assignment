import csv
from models.Vehicle import Vehicle
#import time # for status bar
import datetime # for clock
import os # for the cls function
#import winsound
now = datetime.datetime.now()
def cls(pm):   #######################################################################Daði, this function is also in the Salesman_UI.py program. - How do we put it in one place only, and refer it from here, an from salesmanUI?
    if pm == 'end':
        input('Ýttu á Enter til að að fara aftur í aðalval')  
    os.system('cls' if os.name=='nt' else 'clear')


class VehicleRepository:
    def __init__(self):
        self.__Vehicles = []
    def add_Vehicle_csv(self, Vehicle):
         with open("./data/vehicle.csv","a+", newline = '', encoding="UTF-8-SIG") as v_file:
             ##Bílnúmer,Framleiðandi,Týpuheiti,Flokkur,Árg.Laus dags,Staðsettur,Skilastaðsetning,Athugasemdir
            license_plate = Vehicle.get_license_plate()
            manufacturer = Vehicle.get_manufacturer()
            subtype = Vehicle.get_subtype()
            vec_class = Vehicle.get_vec_class()
            production_year = Vehicle.get_production_year()
            current_location = Vehicle.get_current_location()
            return_location = Vehicle.get_return_location()
            return_date = Vehicle.get_return_date()
            comments = Vehicle.get_comments()
            if comments == '':
                comments = 'NaN'
            csv_writer = csv.writer(v_file,delimiter=";")
            csv_writer.writerow([license_plate,manufacturer,subtype,vec_class,production_year,current_location,return_location,return_date,comments])

    def return_car(self,param):
        old = []
        #bilnumer = input("bilnumer: ")
        with open("data/vehicle.csv", "r", encoding="UTF-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            counter_i =0
            counter_x = 0
            for i in csv_reader:
                if i[0] != param:
                    old.append(i)
                    counter_i += 1
                else:
                    i.remove(i[7]) # if (line[7] == '0D' and line[3] ==vec_class):
                    i.insert(7, "0D")
                    old.append(i)
                    counter_x +=1
            if counter_x == 0:
                print('Bíll ',param,' fannst ekki á skrá, reyndu aftur. ')
            else:
                print('Bíl ',param, ' hefur verið skilað')
                
        with open("data/vehicle.csv", "w", encoding="UTF-8", newline = "") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerows(old)

                


    def get_Occupied_Vehicles(self):
        counter_i = 0
        cls("")
        if self.__Vehicles == []:
            with open('./data/vehicle.csv','r',encoding = "UTF-8-SIG", newline = '') as veh_file:
                csv_reader = csv.reader(veh_file,delimiter =";")                           
                print("╔════════════════════════════════════════════════════════════════════════════════════╗")
                print("║Bílaleigukerfið Zúber | Yfirlit: Útleigðir bílar | Prentað","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S") ,   "   ║") 
                print("║{:<9}{:<10}{:<10}{:<10}{:<10}{:<10}{:>25}".format('Nr.',"Framl.","Týpa","Flokkur","Leigður frá","Skilað","║"))
                print("╠════════════════════════════════════════════════════════════════════════════════════╣")
                for line in csv_reader:
                    if line[7] != '0D':
                        print("║{:<9}{:<10}{:<10}{:<10}{:<10}{:<10}{:>26}".format(line[0],line[1],line[2],line[3],line[5],line[6],"║"))
                        

                        counter_i +=1
                print("╠════════════════════════════════════════════════════════════════════════════════════╣")                        
                print("║Fjöldi útleigðra bíla= {:<10}{:>52}".format(counter_i,' ║'))
                print("╚════════════════════════════════════════════════════════════════════════════════════╝")      
                                                      
    def get_Available_Vehicles(self):
        counter_i = 0
        cls("")
        if self.__Vehicles == []:
            with open('./data/vehicle.csv','r',encoding = "UTF-8-SIG", newline = '') as veh_file:
                csv_reader = csv.reader(veh_file,delimiter =";")
                print("╔════════════════════════════════════════════════════════════════════════════════════╗")
                print("║ Bílaleigukerfið Zúber: Yfirlit: Lausir bílar prentað út: ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S") ,   "    ║") 
                print("║{:<9}{:<10}{:<10}{:<10}{:<10}{:>35}".format('Nr.',"Framl.","Týpa","Flokkur","Staðsetning","║"))
                print("╠════════════════════════════════════════════════════════════════════════════════════╣")
                for line in csv_reader:
                    if line[7] == '0D':
                        print("║{:<9}{:<10}{:<10}{:<10}{:<10}{:>36}".format(line[0],line[1],line[2],line[3],line[5],"║"))
                        counter_i +=1
                print("╠════════════════════════════════════════════════════════════════════════════════════╣")                        
                print("║Fjöldi lausra bíla=    {:<10}{:>52}".format(counter_i,'║'))
                print("╚════════════════════════════════════════════════════════════════════════════════════╝")                    

    def get_Available_Vehicles_by_Class(self,vec_class):
        counter_i = 0
        cls("")
        if self.__Vehicles == []:
            with open('./data/vehicle.csv','r',encoding = "UTF-8-SIG", newline = '') as veh_file:
                csv_reader = csv.reader(veh_file,delimiter =";")
                print("╔════════════════════════════════════════════════════════════════════════════════════╗")
                print("║ Bílaleigukerfið Zúber: Yfirlit: Lausir bílar prentað út: ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S") ,   "   ║") 
                print("║{:<9}{:<10}{:<10}{:<10}{:<10}{:>35}".format('Nr.',"Framl.","Týpa","Flokkur","Staðsetning","║"))
                print("╠════════════════════════════════════════════════════════════════════════════════════╣")
                for line in csv_reader:
                    if (line[7] == '0D' and line[3] ==vec_class):  
                        print("║{:<9}{:<10}{:<10}{:<10}{:<10}{:>36}".format(line[0],line[1],line[2],line[3],line[5],"║"))
                        

                        counter_i +=1
                print("╠════════════════════════════════════════════════════════════════════════════════════╣")                        
                print("║Fjöldi lausra bíla: {:<5} Flokkur: {:<10}{:>40}".format(counter_i,vec_class,'║'))
                print("╚════════════════════════════════════════════════════════════════════════════════════╝")            
            return self.__Vehicles  #-hk 12.12
