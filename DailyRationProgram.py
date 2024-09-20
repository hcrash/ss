from datetime import datetime
from termcolor import colored
### day
today = datetime.today()
day = today.strftime('%A')
### color
def color(sub):
    return colored(sub,'light_cyan')
###Subjects
ph = " physics "
his = " history "
isl = " islamic "
eng = " english "
ch = " chemistry "
ma = " math "
ar = " arabic "
pc = " computer "
bio =" Biology "
Ea = " Earth sciences "
###.....
sh = colored("Your subjects tomorow is : ",'light_green')
### Daily Subjects
sun = [ eng, pc, pc, his, isl, ma, ar ]
mon =  [ma, isl, ph, eng, ar, ch, isl]
tues = [ eng, ma, ch, isl, ar, his ]
wednes = [ ph, isl, his, eng, ar, ar ]
thurs= [ ar, isl, eng, ma, Ea, bio ]
### dd
print("Today is : ",day)
### done
if day == "Saturday":
    print(sh,color(sun))
elif day == "Sunday" or "Friday" or "Thursday":
    print(sh,color(mon))
elif day == "Monday":
    print(sh,color(tues))
elif day == "Tuesday":
    print(sh,color(wednes))
elif day == "Wednseday":
    print(sh,color(thurs))
print(colored("Programed By : H21" ,'light_red'))
input()
### This Program Is For The DailyRationProgram
