#Hannes Kristjánsson 18. sept 2018

#path to github repository is:
#https://github.com/HKristjansson/ru_assignment
import string

#forritið mun geyma í sér gildi, og hægt verður að ferðast um hnitakerfi frá 1,1 í 3,3 ( ferkantað hnitakerfi)
# það er "völundarhús" á leiðinni, þannig að til að ná í "Victory" þá þarf að ferðast alveg í norður
lastinputwrong = False
errortxt = 'Not a valid direction!'
northonly = 'You can travel: (N)orth.'
nes = 'You can travel: (N)orth or (E)ast or (S)outh.'
e_or_s = 'You can travel: (E)ast or (S)outh.'
e_or_w = 'You can travel: (E)ast or (W)est.'
w_or_s = 'You can travel: (S)outh or (W)est.'
n_or_s = 'You can travel: (N)orth or (S)outh.'
new_location = 0.0

current_location = 1.1

#print(northonly)
#init_direction = (input('Direction: '))

while True:
    #init_direction = (input('Direction: '))

    if new_location != 0.0:
        current_location = new_location

    if current_location == 1.1:
        if not lastinputwrong:
            print(northonly)
        direction = str.lower((input('Direction: ')))
        if direction != 'n':
            print(errortxt)
            lastinputwrong = True
        else:
            new_location = 1.2
            lastinputwrong = False
            #print(nes)

    if current_location == 1.2:
        if not lastinputwrong:
            print(nes)            
        direction = str.lower((input('Direction: ')))
        if direction == 'n':
            new_location = 1.3
            lastinputwrong = False
            #print('1.3')
        elif direction == 's':
            new_location = 1.1
            lastinputwrong = False
            #print('1.1')
        elif direction == 'e':
            new_location = 2.2
            lastinputwrong = False
            #print('2.1')
        else:
            print(errortxt)
            lastinputwrong = True

    if current_location == 1.3:
        if not lastinputwrong:
            print(e_or_s)
        direction = str.lower((input('Direction: ')))
            #if direction != 'e' or direction != 's':
            #    print(errortxt)
            
        if direction == 's':
            new_location = 1.2
            lastinputwrong = False
            #print(1.2)
        elif direction == 'e':
            new_location = 2.3
            lastinputwrong = False
            #print(2.3)
        else:
            print(errortxt)
            lastinputwrong = True


    if current_location == 2.3:
        if not lastinputwrong:
            print(e_or_w)
        direction = str.lower((input('Direction: ')))
        if direction == 'w':
            new_location = 1.3
            lastinputwrong = False
            #print(1.3)
        elif direction == 'e':
            new_location = 3.3
            lastinputwrong = False
            #print(3.3)
        else:
            print(errortxt)
            

    if current_location == 3.3:
        print(w_or_s)
        direction = str.lower((input('Direction: ')))          
        if direction == 'w':
            new_location = 2.3
            #print(2.3)
        elif direction == 's':
            new_location = 3.2
            #print(3.2)
        else:
            lastinputwrong = True
            print(errortxt)

    if current_location == 3.2:
        if not lastinputwrong:
            print(n_or_s)
        direction = str.lower((input('Direction: ')))          
        if direction == 'n':
            new_location = 3.3
            lastinputwrong = False
            #print(2.3)
        elif direction == 's':
            new_location = 3.1
            lastinputwrong = False
            #print(3.2)
        else:
            print(errortxt)
            lastinputwrong = True

#-----------inni í völundarhúsinu BEGIN
    if current_location == 2.2:
        if not lastinputwrong:
            print(w_or_s)
        direction = str.lower((input('Direction: ')))          
        if direction == 'w':
            new_location = 1.2
            lastinputwrong = False
            #print(1.3)
        elif direction == 's':
            new_location = 2.1
            lastinputwrong = False
            #print(1.2)
        else:
            print(errortxt)
            lastinputwrong = True


    if current_location == 2.1:
        if not lastinputwrong:
            print(northonly)
        direction = str.lower((input('Direction: ')))         
        
        if direction == 'n':
            new_location = 2.2
            lastinputwrong = False
            #print(1.3)
        else:
            print(errortxt)
            lastinputwrong = True

#----------inni í völundarhúsinu END
    
    if current_location == 3.1:
        print('Victory!')
        exit()



  

    #print('current location - ' + str(new_location))
