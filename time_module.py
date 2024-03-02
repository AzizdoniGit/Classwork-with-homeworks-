import time
from datetime import datetime

hours = int(input("enter your hours: "))
minutes = int(input("enter your minutes: "))
seconds = int(input("enter your seconds: "))

while True:
    now = datetime.now()
    print(f"Alarm clock: {hours}:{minutes}:{seconds}")
    print(f"System clock: {now.hour}:{now.minute}:{now.second}")
    if (now.hour == hours and now.minute == minutes and now.second == seconds):
        print("Wake up u little shit")
        break
    else:
        print("----------")
        print("Waiting...")
        print("----------")

    time.sleep(1)
