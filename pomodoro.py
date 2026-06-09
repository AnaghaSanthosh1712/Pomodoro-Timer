import time
import winsound
streak= 0
def count(x):
    global streak
    while (x>0):
        min=x//60
        sec=x%60
        print(f"                         {min:02d}:{sec:02d}",end="\r"    )
        time.sleep(1)
        x=x-1
    winsound.PlaySound("alarm.wav",winsound.SND_FILENAME)
    streak+=1
    value=int(input("What To Do Next:- \n 1)Take A Short Break(5 min) \n 2)Take a Long Break(15 min) \n 3)Continue the Work \n 4)Exit \n Enter a option (in numbers as 1,2,3,4):- "))   
    if(value==1):
        count(300)
    elif (value==2):
        count(900)
    elif(value==3):
        total=int(input("Enter the Time limit Upto Which you are studying(in minutes):- "))
        total=total*60
        count(total)
    else:
        print(f"Nice Job!!You are Exiting with  {streak} Streak")
        exit()
    

print("POMODORO TIMER⏳ ")
print("----------------  ")

total=int(input("Enter the Time limit Upto Which you are studying(in minutes):- "))
total=total*60
count(total)


