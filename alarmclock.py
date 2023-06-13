from datetime import datetime
# from playsound import playsound

alarm_time= input("Alarm Time in HH:MM:SS AM/PM format: ")


def time_validity(alarm_time):
    if len(alarm_time)!=11: 
        print("Invalid alarm time. Try again")
    else:
        if int(alarm_time[0:2])>12 :
            return("Invalid hour time. Try again")
        elif int(alarm_time[3:5])>59:
            return("Invalid minute time. Try again") 
        elif int(alarm_time[6:8])>59:
            return("Invalid second time. Try again")
        elif str(alarm_time[9:11]) not in ["am","pm","AM","PM","aM","Am","pM","Pm"]: 
            return("Invalid AM/PM Format. Try again")
        else:
            return("Ok!")

while True: 
    validate= time_validity(alarm_time)
    if validate=="Ok!":
        print(f"Setting the alarm for {alarm_time}")
        break
    else: 
        print(validate)
    
while True:
    current_time= datetime.now()

    current_hour_old= current_time.hour
    if current_hour_old>12:
        current_hour= current_hour_old-12
        current_period= "PM"
    else:
        current_hour= current_hour_old
        current_period="AM"
    current_minute=current_time.minute
    current_second=current_time.second

    alarm_hour= int(alarm_time[0:2])
    alarm_minute= int(alarm_time[3:5])
    alarm_second= int(alarm_time[6:8])
    alarm_period= alarm_time[9:11]

    if alarm_hour==current_hour and alarm_minute==current_minute and alarm_second==current_second and alarm_period==current_period:
        print("WAKEEEE UPPPPP!!!")
        # playsound("D:\PythonProjects\alarm-clock\alarm.mp3") 
        break
        


                    
