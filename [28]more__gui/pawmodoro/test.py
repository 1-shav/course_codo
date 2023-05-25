import time
#making a timer script
def timerstart():
    timerstart=int(input("How long would you like the timer to be?(In Minutes) "))
    timeinmin= timerstart*60
    timeinsec= timerstart//60
    time.sleep(timerstart)
    print("Your Timer For ",timeinmin," Has Finished")
print(timerstart())