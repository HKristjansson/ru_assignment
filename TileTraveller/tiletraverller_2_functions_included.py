#1. Which implementation was easier and why?
#2. Which implementation is more readable and why?
#3. Which problems in the first implementations were you able to solve with the latter implementation?

#replies to questions:
#1. - to be honest; the one without functions was easier for me; simply cause I couldn't really find a way to use functions in a smart way in this excercise. - However, - I used them, but my code is sooo many lines. Don't get me
#   wrong; I know using functions is the right thing. - For one thing I overvcomplicated my function, sending too many parameters into it, and expecting ... well, just too much of it.
#2. because I feel my function program isn't good enough, then I say that the one without functions is easiear to read. (Should be the other way around though)
#3. Well, to point something out, I could use the same functionality for tiles 1.1 and 2.1  (only move north), and 2.2 and 3.3. However, the cost of this benefit was huge... :/


#Hannes Kristjánsson 18. sept 2018

#path to github repository is:
#https://github.com/HKristjansson/ru_assignment
import string

#forritið mun geyma í sér gildi, og hægt verður að ferðast um hnitakerfi frá 1,1 í 3,3 ( ferkantað hnitakerfi)
# það er "völundarhús" á leiðinni, þannig að til að ná í "Victory" þá þarf að ferðast alveg í norður
# og svo austur og suður. - Sé það ekki gert, þá lendir notandi á vegg... (en getur farið út úr völundarhúsinu aftur)

# Now for my new, function oriented program
# I'm go_li to reuse the same logic for cells 1.1 and 2.1 (only allowing north)
# and reuse 2.2 and 3.3 as they also should have the same return values
lastinputwrong = False
stop_the_program = False
went_ok = False
errortxt = 'Not a valid direction!'
northonly = 'You can travel: (N)orth.'
nes = 'You can travel: (N)orth or (E)ast or (S)outh.'
e_or_s = 'You can travel: (E)ast or (S)outh.'
e_or_w = 'You can travel: (E)ast or (W)est.'
w_or_s = 'You can travel: (S)outh or (W)est.'
n_or_s = 'You can travel: (N)orth or (S)outh.'
new_location = 0.0
current_location = round(1.1,1)

#def location_mover(n_pm,e_pm,s_pm,w_pm):
    

def reaction(n_pm,e_pm,s_pm,w_pm,loc_pm,linpwrong_pm):
    try:
        if n_pm == 1 and e_pm == 0 and s_pm ==0 and w_pm ==0:
            if linpwrong_pm == False:
                print(northonly)
            go_li = str.lower(input('Direction: ' ))
            if go_li == 'n':
                if loc_pm ==1.1:
                    loc_pm = 1.2
                elif loc_pm ==2.1:
                    loc_pm = 2.2
                return(True,round(loc_pm,1))
            else:
                return(False,round(loc_pm,1))

        if n_pm ==1 and e_pm ==1 and s_pm ==1 and w_pm ==0:
            if linpwrong_pm == False:
                print(nes)
            go_li = str.lower(input('Direction: ' ))
            if go_li == 'n':
                loc_pm += .1
                return(True,round(loc_pm,1))
            elif go_li =='s':
                loc_pm -= .1
                return(True,round(loc_pm,1))
            elif go_li =='e':
                loc_pm += 1
                return(True,round(loc_pm,1))

            
            else:
                return(False,round(loc_pm,1))
        
        if n_pm ==0 and e_pm ==1 and s_pm ==1 and w_pm ==0:
            if linpwrong_pm == False:
                print(e_or_s)
                
            go_li = str.lower(input('Direction: ' ))
            if go_li =='e':
                loc_pm +=1
                return(True,round(loc_pm,1))
            elif go_li =='s':
                loc_pm -= .1
                return(True,round(loc_pm,1))

            
            else:
                return(False,round(loc_pm,1))

        if n_pm ==0 and e_pm ==1 and s_pm==0 and w_pm==1:
            if linpwrong_pm == False:
                print(e_or_w)
                
            go_li = str.lower(input('Direction: ' ))
            if go_li =='e':
                loc_pm +=1
                return(True,round(loc_pm,1))
            elif go_li =='w':
                loc_pm -=1
                return(True,round(loc_pm,1))
                
            
            else:
                return(False,round(loc_pm,1))

        if n_pm ==0 and e_pm ==0 and s_pm==1 and w_pm==1:
            if linpwrong_pm == False:
                print(w_or_s)
                
            go_li = str.lower(input('Direction: ' ))
            if go_li =='s':
                loc_pm -= .1
                return(True,round(loc_pm,1))
            elif go_li =='w':
                loc_pm -=1
                return(True,round(loc_pm,1))
            
            else:
                return(False,round(loc_pm,1))

        if n_pm ==1 and e_pm ==0 and s_pm==1 and w_pm==0:
            if linpwrong_pm == False:
                print(n_or_s)
                
            go_li = str.lower(input('Direction: ' ))
            if go_li =='s':
                loc_pm -= .1
                return(True,round(loc_pm,1))
            elif go_li =='n':
                loc_pm +=.1
                return(True,round(loc_pm,1))
            else:
                return(False,round(loc_pm,1))            

    
    except Exception: 
        print("Please enter valid input")
        return(False,loc_pm)
        #else:
        #    (False,round(loc_pm,1))

            

location = 1.1

while stop_the_program == False:
    if location == 1.1 or location == 2.1:

        went_ok,location = reaction(1,0,0,0,location,lastinputwrong)
        if went_ok ==True:
            lastinputwrong = False
            
            #print(str(location))
        else:
            print(errortxt)
            lastinputwrong = True

    if location == 1.2:
        went_ok,location = reaction(1,1,1,0,location,lastinputwrong)
        if went_ok ==True:
            lastinputwrong = False
            #print(str(location))
        
        else:
            print(errortxt) 
            lastinputwrong = True           

    if location == 1.3:
        went_ok,location = reaction(0,1,1,0,location,lastinputwrong)
        if went_ok == True:
            #print(str(location))
            lastinputwrong = False
        else:
            print(errortxt)
            lastinputwrong = True

    if location == 2.3:
        went_ok,location = reaction(0,1,0,1,location,lastinputwrong)
        if went_ok == True:
            #print(str(location))
            lastinputwrong = False
        else:
            print(errortxt)
            lastinputwrong = True

    if location == 3.3 or location == 2.2:
        went_ok,location = reaction(0,0,1,1,location,lastinputwrong)
        if went_ok == True:
            #print(str(location))
            lastinputwrong = False
        else:
            print(errortxt)   
            lastinputwrong = True         

    if location ==3.2:
        went_ok,location = reaction(1,0,1,0,location,lastinputwrong)        
        if went_ok == True:
            #print(str(location))
            lastinputwrong = False
        else:
            print(errortxt)
            lastinputwrong = True
    
    if location ==3.1:
        print('Victory!')
        stop_the_program = True
        #reaction(0,0,0,0,location)

    

