import csv
from firstinput import info

def button1_event(Gender, Age, Activity, Name):
    userInfo = info(str(Gender), str(Age), str(Activity))
    with open('userinfo.csv', 'r+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([Name, userInfo])
        rows = csv.reader(csvfile)
        for row in rows:
            print(row)
    csvfile.close()