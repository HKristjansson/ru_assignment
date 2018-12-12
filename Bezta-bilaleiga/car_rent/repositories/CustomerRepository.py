from models.Customer import Customer

import csv
import datetime # for clock
import os # for the cls function
#import winsound
now = datetime.datetime.now()

class CustomerRepository:
    
    def __init__(self):
        self.__Customer = []

    def add_Customer_csv(self, Customer):
        with open("./data/customer.csv", "a+",newline = '', encoding = "UTF-8-SIG") as Customer_file:
            kennitala = Customer.get_kennitala()
            # x = Customer.get_kennitala()
            name = Customer.get_name()
            address = Customer.get_address()
            post_number = Customer.get_post_number()
            phone_number = Customer.get_phone_number()
            email_adress = Customer.get_email_address()
            status = Customer.get_status()

            #Customer_file.write("{},{},{}\n".format(name,kennitala,phone))
            csv_writer = csv.writer(Customer_file, delimiter =";")
            csv_writer.writerow([kennitala,name,address,post_number,phone_number,email_adress,status])

    def get_Customer(self):
        if self.__Customer == []:
            with open("./data/customer.csv", "r",encoding = "UTF-8-SIG") as Customer_file:
                csv_reader = csv.reader(Customer_file ,delimiter =";")
                print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
                print("║             Bílaleigukerfið Zúber:                        Yfirlit: Viðskiptavinir prentað út:                                         ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S") ,    "    ║") 
                print("╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                print("║{:<20}{:<30}{:<20}{:<20}{:<15}{:<35}{:<20}".format('Kennitala',"Nafn","Heimilisfang","Póstnúmer","Símanúmer","Tölvupóstfang","status")," ║")
                print("╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                for line in csv_reader:
                    try:
                        print("║""{:<20}{:<30}{:<20}{:<20}{:<15}{:<35}{:<20}".format(line[0],line[1],line[2],line[3],line[4],line[5],line[6])," ║")
                    except IndexError:
                        print("villa fanst, uppfærðu customer.csv")
                    print("╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                print("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝") 

                #     print("║""{:<20}{:<30}{:<30}{:<20}{:<20}{:<20}{:<20}".format(line[0],line[1],line[2],line[3],line[4],line[5],line[6]),"                                             ║")
                # print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝") 
                #for line in Customer_file.readlines():
                #    name,kennitala,phone = line.split(",")
                #    new_Customer = Customer(name,kennitala,phone)
                #    self.__Customer.append(new_Customer)    
            
        return self.__Customer

    def get_customer_by_kennitala(self,cust_kennitala):
        if self.__Customer == []:
            with open('./data/customer.csv', 'r',encoding = "UTF-8-SIG", newline = '') as ord_file:
                csv_reader = csv.reader(ord_file,delimiter =";")
                linecounter_i = 0
                print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
                print("║ Bílaleigukerfið Zúber:                        yfirlit yfir viðskiptavin eftir kennitölu                            ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S")                       ,   "    ║") 
                print("║{:<20}{:<30}{:<30}{:<20}{:<20}{:<20}".format("Kennitala","Nafn","Heimilisfang","Póstnúmer","Símanúmer","Tölvupóstfang"),"  ║")
                print("╠═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
                   
                for line in csv_reader:
                    if (line[0] == cust_kennitala ):
                        linecounter_i += 1
                        print("║{:<20}{:<30}{:<30}{:<20}{:<20}{:<20}".format(line[0],line[1],line[2],line[3],line[4],line[5]),"  ║")
                    
                print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝") 
                if linecounter_i ==0:
                    print('Þú slóst inn kennitölu: ',cust_kennitala,' - engin viðskiptavinur fannst með því númeri')
            
        return self.__Customer
