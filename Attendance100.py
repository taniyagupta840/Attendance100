from datetime import datetime
import time
import sys
import csv
import os

def find_next_class(timetable_location, day):
    current_time = datetime.now().strftime("%H:%M")
    curr_time = time.strptime(current_time, "%H:%M")
    
    with open(timetable_location, 'r') as timetable:
        reader = csv.reader(timetable)
        for row in reader:
            class_time = time.strptime(str(row[0]), "%H:%M")
            
            if class_time >= curr_time and row[day+1] == "exit":
                print("No more classes for today.")
                exit()
            elif class_time >= curr_time and row[day+1] != "":
                print("Next Class at " + row[0])
                return class_time, row[day+1]
    
    print("Classes already over.")
    exit()

def attend_class(timetable_location):
    Weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    day = datetime.today().weekday()
    print(Weekdays[day])

    while True:
        class_time, link = find_next_class(timetable_location, day) 
        while True:
            current_time = datetime.now().strftime("%H:%M")
            curr_time = time.strptime(current_time, "%H:%M")
            print("Current Time : " + current_time)

            if class_time == curr_time:
                print("Class at " + current_time)
                os.system("start "" " + link)
                print("Joined class at link : " + link)
                time.sleep(60)
                break

            time.sleep(60)

attend_class(sys.argv[1])
