import time

hour = int(input("Enter current hour: "))
minute = int(input("Enter current minute: "))
seccond = int(input("Enter current second: "))

def displayer():
    print(hour, ":", minute, ":", seccond)

def clock():
    global hour
    global minute
    global seccond

    seccond += 1
    if seccond >= 60:
        minute += 1
        seccond = 0
    
    if minute >= 60:
        hour += 1
        minute = 0
    
    if hour >= 24:
        hour = 0

    return hour, minute, seccond

while True:
    clock()
    displayer()
    time.sleep(1)

