import datetime
def is_date_valid():
    try:
        date = input('Dagur: ')
        month = input("Mánuður: ")
        year = input("Ár: ")
        #x = datetime.datetime(2020, 5, 17)
        valid_date = datetime.datetime(year,month,date)
        return(valid_date)
        # return dagsetn
    except TypeError:
        is_date_valid()
def date_valid():
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
        date_valid()

date_valid()


#is_date_valid()
#import dateutil
#dateutil.parser import parse
def validate():
    date_text = datetime
    try:
        
        inp_d = int(input('Dagur: '))
        inp_month = int(input("Mánuður: "))
        inp_year = int(input("Ár: "))
 
        #parse("2003-09-25")
        #date_text = datetime.datetime(inp_year, inp_month, inp_d, 0, 0):
            #raise ValueError

        #if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
        #    raise ValueError
        return True
    except ValueError:
        return False


#validate()


def ssn_check(self,kt_l):
        print('keyrir')
        text001	= 'Kennitala er of löng'
        text002	= 'Kennitala er of stutt'
        text003	= 'Skil ekki form kennitölu'
        tested_kt = ''    
        notification = ''
        if (len(kt_l) > 11) :
            notification = text001
        elif (len(kt_l) < 10):
            notification = text002
        elif (len(kt_l)== 11) and (kt_l[6] != '-'):
            notification = text003
        elif (len(kt_l) == 10 and (kt_l[6]=='-')):
            notification = text003
        elif (len(kt_l) == 10):
            tested_kt = kt_l[0:6] + '-' + kt_l[6:11]
        elif (len(kt_l)== 11) and (kt_l[6] == '-'):
            tested_kt = kt_l[0:6]  + kt_l[6:11]
        else:
            print('Þessi skilaboð ættu ekki að koma upp; villa númer 1, hafðu samband við þjónustuaðila kerfis')
        #ktx_l = tested_kt[0:6]  + tested_kt[7:11]
        #################### and now for returns
        if notification != '':
            ret_value = 'false'

        else: 
            ret_value = tested_kt
                
        return ret_value
        
    #kt_test = input('Sláðu inn kennitölu ')

    #kt = ssn_check(kt_test)
    #print('útkoman', kt)
        def ssn_(self,kt_l):

#          while True:
# ...     try:
# ...         x = int(input("Please enter a number: "))
# ...         break
# ...     except ValueError:
# ...         print("Oops!  That was no valid number.  Try again...")

            issue = False
            while issue !=True: 
                try:
                
                    text001	= 'Kennitala er of löng'
                    text002	= 'Kennitala er of stutt'
                    text003	= 'Skil ekki form kennitölu'
                    tested_kt = ''    
                    notification = ''
                    if (len(kt_l) > 11) :
                        notification = text001
                        issue = True
                    elif (len(kt_l) < 10):
                        notification = text002
                        issue = True
                    elif (len(kt_l)== 11) and (kt_l[6] != '-'):
                        notification = text003
                        issue = True
                    elif (len(kt_l) == 10 and (kt_l[6]=='-')):
                        notification = text003
                        issue = True
                    #######################below, modifing string    
                    elif (len(kt_l) == 10):
                        tested_kt = kt_l[0:6] + '-' + kt_l[6:11]
                    elif (len(kt_l)== 11) and (kt_l[6] == '-'):
                        tested_kt = kt_l[0:6]  + kt_l[6:11]
                    else:
                        print('Þessi skilaboð ættu ekki að koma upp; villa númer 1, hafðu samband við þjónustuaðila kerfis')
                    #############################
                    print('issue',issue)
                    if notification != '':
                        ret_value = 'false'
                    else: 
                        ret_value = tested_kt
                except ValueError:
                        a = x
                    #return ret_value
                    