from ui.SalesmanUi import SalesmanUi
from ui.login import Login
def main():
        #preparation = False
        success = Login()        
        could_log_in = success.main_menu()
        if could_log_in:        
                ui = SalesmanUi()
                ui.main_menu()     
main()

