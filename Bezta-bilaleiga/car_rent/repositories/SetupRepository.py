from models.Setup import Setup
import csv

class SetupRepo:
    
    def __init__(self):
        self.__Setup = []   

    def add_Setup_csv(self, Setup):
        with open("./data/access.csv","a+",encoding = "UTF-8-SIG", newline = '') as o_file: 
            uid = Setup.get_user_id()
            pwd = Setup.get_pwd()
            ssn = Setup.get_ssn()
            name = Setup.get_name()
            addr = Setup.get_address()
            phone_no = Setup.get_phone_no()
            e_mail = Setup.get_e_mail()
            active = Setup.get_active()
            comment = Setup.get_comment()

            csv_writer = csv.writer(o_file,delimiter=";")
            csv_writer.writerow([uid,pwd,ssn,name,addr,phone_no,e_mail,active,comment])

    def get_Setup(self):
        if self.__Setup ==[]:
            with open('./data/access.csv','r',encoding = "UTF-8-SIG", newline = '') as Setup_file:
                csv_reader = csv.reader(Setup_file,delimiter =";")
                for line in csv_reader:
                    print(line)
        
        return self.__Setup



