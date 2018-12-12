import datetime
def date_valid(ds):
#     inp_d = input('     Dagur: ')
#     inp_month = input("     Mánuður : ")
#     inp_year = input("    Ár: ")
#     date_string = inp_d + "." + inp_month + "."+ inp_year
    date_format = '%d.%m.%Y'
    #output_date_string
    try:
        dayoutput = ''
        dayoutput = datetime.datetime.strptime(ds, date_format)
        print(date_string)
        print(dayoutput)

        #return(date_string)
        #return true,date_string
    except ValueError:
        print("Óleyfileg dagsetning slegin inn, reyndu aftur: ")
        date_valid()

dateinvalid = True
while dateinvalid==True:
        inp_d = input('     Dagur: ')
        inp_month = input("     Mánuður : ")
        inp_year = input("    Ár: ")
        date_string = inp_d + "." + inp_month + "."+ inp_year
        date_valid(date_string)
        print(date_valid)

        