# -@STARTECH.inc(jk that doesnt actudally exist)
# a simple program thats kinda useful so.. published
# read the readme file for more information

import pyautogui as pg
from datetime import datetime as dt
import os
import time as timer

loc = ""
#--config
file = open("configfile.txt")
config = []
for i in file:
    i = i.split()
    if i[0] == "Zoom_location:":
        loc = i[1]


def get_timetable(period):
    lis = []
    for x in period:
        lis.append(x.strip("\n").split())
    return lis

def get_timeings(timeings):
    lis = []
    for x in timeings:
        x = x.strip("\n")
        x = x.split()
        x[0] = int(x[0])
        x[1] = int(x[1])
        lis.append(x)
    return lis

def get_pmi(pmis):
    lis = []
    for x in pmis:
        x = x.strip("\n")
        x = x.split()
        lis.append(x)
    return lis

def currentperiod(t, h, m):
    p = 0
    for i in t:
        p += 1
        ph = i[0]
        pm = i[1]
        if ph > h:
            return p - 1
        elif ph == h:
            if pm >= m:
                return p -1 
        else:
            pass

def openmeeting(id, psswd):
    os.startfile(loc)
    timer.sleep(2)
    pg.press("enter")
    timer.sleep(2)
    pg.write(id)
    pg.press("enter")
    timer.sleep(2)
    pg.write(psswd)
    pg.press("enter")
    
timetable = open("timetable.txt")
timeings = open("timetable-timings.txt")
pmi = open("pmi.txt")
timetable = get_timetable(timetable)
timeings = get_timeings(timeings)
pmi = get_pmi(pmi)

#print(timetable) 
#print(time)
#sprint(pmi)
#uncomment to check the timetable, timeings and  pmi for troubleshooting

time = dt.now()
chour = time.hour
cminute = time.minute
periodnum = currentperiod(timeings, chour, cminute)
day = time.weekday()
ttimetable = timetable[day]
period = ttimetable[periodnum - 1]

#print(period)
#uncomment to check the calculated period for troubleshooting

for ip in pmi:
    name = ip[0]
    if name == period:
        print(ip[1], ip[2])
        fid = ip[1]
        fpsswd = ip[2]
        openmeeting(fid, fpsswd)

