#run in command prompt only
#Because in python default IDE... \r isn't working
import time

print("Enter countdown time (enter zero(0) if nothing)")
try:        #to take input
    h = abs(int(input("Hours: ")))
    m = abs(int(input("Minutes: ")))
    s = abs(int(input("Seconds: ")))
    stop = h*3600 + m*60 + s
except:     #if type conversion fails
    print("Not a number!")
print("\n")
while stop > 0:   #loop to start countdown
    m, s = divmod(stop, 60) 
    h, m = divmod(m, 60)
    time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    print(time_left + "\r", end="") #print countdown every second
    time.sleep(1)
    stop -= 1
print("You were Deceived!")
