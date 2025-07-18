import time

t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
hour = int(input("enter the hour: "))
print(hour)
if(hour >= 0 and hour < 12):
    print("good morning uth ja ")
elif(hour >= 12 and hour < 17):
    print("good afternoon kaam kar le thoda")
elif(hour >=17 and hour < 0):
    print("good night so ja jake")