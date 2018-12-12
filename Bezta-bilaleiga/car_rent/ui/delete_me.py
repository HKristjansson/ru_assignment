from datetime import date  

myDate = date.today()    
#print(myDate) would output 2017-05-23 because that is today
#reassign the myDate variable to myDate = myDate.month 
#then you could print(myDate.month) and you would get 5 as an integer
dateStr = str(myDate.month)+ "/" + str(myDate.day) + "/" + str(myDate.year)    
# myDate.month is equal to 5 as an integer, i use str() to change it to a 
# string I add(+)the "/" so now I have "5/" then myDate.day is 23 as
# an integer i change it to a string with str() and it is added to the "5/"   
# to get "5/23" and then I add another "/" now we have "5/23/" next is the 
# year which is 2017 as an integer, I use the function str() to change it to 
# a string and add it to the rest of the string.  Now we have "5/23/2017" as 
# a string. The final line prints the string.

print(dateStr) 

from datetime import datetime
date_format = "%d.%m.%Y"
a = datetime.strptime('30.12.2018', date_format)
b = datetime.strptime('01.01.2019', date_format)
delta = b - a
print(delta.days) # that's it


import datetime
today = datetime.date.today()
someday = datetime.date(2008, 12, 25)
diff = someday - today
diff.days
