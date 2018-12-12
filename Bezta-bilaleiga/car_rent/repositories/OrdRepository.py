from models.Ord import Ord
import csv

import datetime # for clock
import os # for the cls function
now = datetime.datetime.now()

def cls(pm):
    if pm == 'end':
        input('Ýttu á Enter til að að fara aftur í aðalval')  
    os.system('cls' if os.name=='nt' else 'clear')

class OrdRepository:  
    def __init__(self):
        self.__Ord = []  

    def add_Ord_csv(self, order):
        last_no_used = 0
        def no_sequence(read_write,pm):
            if read_write == 'read':
                with open('./data/no_sequence.txt','r') as textfile:
                    for i in textfile:
                        return(i)
            elif read_write == 'write':
                 with open('./data/no_sequence.txt','w') as textfile:
                     str_pm =''
                     str_pm = (str(pm))
                     textfile.write(str_pm)
                     print(pm)  

        last_no_used  = int(no_sequence('read',''))
        
        last_no_used += 1
        with open("./data/ord.csv","a+",encoding = "UTF-8-SIG", newline = '') as o_file:  
            order_no = str(last_no_used)
            customer_no = order.get_customerno()
            lic_no = order.get_license_plate_no()
            loc_beg = order.get_start_location()
            loc_end = order.get_return_location()
            first_day_of_rent = order.get_first_day_of_rent()
            last_day_of_rent = order.get_last_day_of_rent()
            payment_type = order.get_payment_type()
            card_number = order.get_card_number()
            basic_insurance = order.get_basic_insurance()
            xtra_insurance = order.get_xtra_insurance()
            order_status = order.get_order_status()
            comments = order.get_comments() 
            csv_writer = csv.writer(o_file,delimiter=";")
            csv_writer.writerow([order_no,customer_no,lic_no,loc_beg,loc_end,first_day_of_rent,last_day_of_rent,payment_type,card_number,basic_insurance,xtra_insurance,order_status, comments])
            #Now we assume that the order was created successfully, thus we append the no series by 1
            no_sequence("write",last_no_used)
        #11.12.2018 - Below, we are writing to the file that reprents vehicles, to indicate that this vehicle is now occupied, as it has been rented out
        vehicle_reg_plate = lic_no
        old = []
        with open("data/vehicle.csv", "r", encoding="UTF-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            counter_i =0
            counter_x = 0
            for i in csv_reader:
                if i[0] != vehicle_reg_plate:
                    old.append(i)
                    counter_i += 1
                else:
                    i.remove(i[7]) 
                    i.insert(7, "0D")
                    old.append(i)
                    counter_x +=1
            if counter_x == 0:
                print('Bíll ',lic_no,' fannst ekki á skrá, reyndu aftur. ')
            else:
                print('Bíl ',lic_no, ' hefur verið leigður út, og pöntun númer',order_no,' stofnuð')
                
        with open("data/vehicle.csv", "w", encoding="UTF-8", newline = "") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerows(old) 

    # def get_Ord(self):   ## commented out 12.1.2018 byhannes - i think we dont used this function at all
    #     if self.__Ord ==[]:
    #         with open('./data/ord.csv','r',encoding = "UTF-8-SIG", newline = '') as ord_file:
    #             csv_reader = csv.reader(ord_file,delimiter =";")
    #             for line in csv_reader:
    #                 print(line)
                   
    #     return self.__Ord

    def order_status_change(self,param):
        old = []
        #bilnumer = input("bilnumer: ")
        with open("data/ord.csv", "r", encoding="UTF-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            counter_i =0
            counter_x = 0
            for i in csv_reader:
                if i[0] != param:
                    old.append(i)
                    counter_i += 1
                else:
                    i.remove(i[10]) 
                    i.insert(10, "CLOSED")
                    param_to_vehicle_repo = i
                    old.append(i)
                    counter_x +=1

            if counter_x == 0:
                print('Bíll ',param,' fannst ekki á skrá, reyndu aftur. ')
            else:
                print('Bíl ',param, ' hefur verið skilað')
                
        with open("data/ord.csv", "w", encoding="UTF-8", newline = "") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerows(old)
        

        #11.12.2018 - the rest of this funtion uses a parameter from the record in the customer csv file,
        #             and uses that parameter to update the car record
        vehicle_reg_plate = param_to_vehicle_repo[2]
        old = []
        with open("data/vehicle.csv", "r", encoding="UTF-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")
            counter_i =0
            counter_x = 0
            for i in csv_reader:
                if i[0] != vehicle_reg_plate:
                    old.append(i)
                    counter_i += 1
                else:
                    i.remove(i[7]) 
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
        
        return self.__Ord
    
    def get_ord_by_number(self,order_number):
        if self.__Ord == []:
            with open('./data/ord.csv', 'r',encoding = "UTF-8-SIG", newline = '') as ord_file:
                line_counter_i = 0
                csv_reader = csv.reader(ord_file,delimiter =";")
                print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
                print("║                 Bílaleigukerfið Zúber:                                             Yfirlit yfir pantanir prentaðar út            ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S")                       ,   "    ║") 
                print("║{:<12}{:<12}{:<12}{:<8}{:<8}{:<15}{:<10}{:<15}{:<15}{:>15}{:<12}{:<8}{:>4}".format('Pöntunarnr',"Kennitala","Bílnúmer","Byrj","End.","Útleigud.","Skilad.","Teg.greiðslu","Kortanr","Grunntr.","Aukatr.","Status","Ath"),"            ║")
                print("╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                   
                for line in csv_reader:
                    if (line[0] == order_number ):
                        line_counter_i +=1
                        print("║{:<12}{:<12}{:<12}{:<8}{:<8}{:<15}{:<15}{:<15}{:<15}{:>12}{:<12}{:<8}{:>4}".format(line[0],
                        line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]),"           ║")
                print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")            
                if line_counter_i == 0:
                    print('Þú slóst inn pöntunarnúmer: ',order_number,' engin pöntun fannst með því númeri')
        return self.__Ord
    
    def get_vehicle_history(self,plate_numb):
        if self.__Ord == []:
            with open('./data/ord.csv', 'r',encoding = "UTF-8-SIG", newline = '') as ord_file:
                csv_reader = csv.reader(ord_file,delimiter =";")
                print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
                print("║                 Bílaleigukerfið Zúber:                                             Yfirlit yfir pantanir prentaðar út            ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S")                       ,   "    ║") 
                print("║{:<12}{:<12}{:<12}{:<8}{:<8}{:<15}{:<10}{:<15}{:<15}{:>15}{:<12}{:<8}{:>4}".format('Pöntunarnr',"Kennitala","Bílnúmer","Byrj","End.","Útleigud.","Skilad.","Teg.greiðslu","Kortanr","Grunntr.","Aukatr.","Status","Ath"),"║")
                print("╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                   
               
                for line in csv_reader:
                    if (line[2] == plate_numb): 
                        print("║{:<12}{:<12}{:<12}{:<8}{:<8}{:<15}{:<15}{:<15}{:<15}{:>12}{:<12}{:<8}{:>4}".format(line[0],
                        line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]),"║")
                    else:
                        print("Pöntunarnúmer finnst ekki")
                    print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")            

        return self.__Ord 
                
    def get_customer_history(self,customer_id):
        if self.__Ord == []:
            with open('./data/ord.csv', 'r',encoding = "UTF-8-SIG", newline = '') as ord_file:
                csv_reader = csv.reader(ord_file,delimiter =";")
                print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
                print("║                 Bílaleigukerfið Zúber:                                             Yfirlit yfir viðskiptavin prentaðar út            ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S")                       ,   "    ║") 
                print("║{:<12}{:<12}{:<12}{:<8}{:<8}{:<15}{:<10}{:<15}{:<15}{:>15}{:<12}{:<8}{:>4}".format('Pöntunarnr',"Kennitala","Bílnúmer","Byrj","End.","Útleigud.","Skilad.","Teg.greiðslu","Kortanr","Grunntr.","Aukatr.","Status","Ath"),"║")
                print("╠═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                    
                
                for line in csv_reader:
                    if (line[1] == customer_id): 
                        print("║{:<12}{:<12}{:<12}{:<8}{:<8}{:<15}{:<15}{:<15}{:<15}{:>12}{:<12}{:<8}{:>4}".format(line[0],
                            line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]),"║")
                        print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")            
        
                return self.__Ord 


