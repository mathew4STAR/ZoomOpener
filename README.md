# Zoom-Meeting-Opener
-This is a program that when run, opens the right meeting(generally for school) based on time, timetable and pmi.

-The program works by checking the current time and based on a timetable provided at *timetable.txt* ,timing of classes provided at *timetable-timings.txt* and a list of pmi of all your classes in *pmi.txt* and opening the correct meeting with a set of keystrokes.

# Installation
1.to clone the repo type:
`git clone https://github.com/mathew4STAR/ZoomOpener`
in cmd or terminal.

2.change the directory
`cd ZoomOpener`

3.run the file 
`python3 main.py`

# Setup

1.Navigate to the right directory.

2.Opening the *configfile.txt* and edit the zoom Zoom_location to your zoom location, Save and Close the file.

3.Open the *pmi.txt* and replace *SUBJECT_1* and others with your subjects and id and password with their corresponding id's and password's, Save and Close the file.

4.Open the *timetable.txt* replace the example *SUBJECT* with your subjects, with the top row being Monday and last row being Friday. And each word in each sentence being differnet peiods.

5.Open the *timetable-timings.txt* and put in the timings of your classes.
# Usage

1.Open cmd or teminal and change the directory

2.Run the file
`python3 main.py`

3.Sitback and watch while it automatically opens the right meeting.

<p>&nbsp;</p>

`Note:It is prone to failing sometime you may also have to tweak the code a little.(Also make sure to undergo the setup process`

`Note: you can use the break keyword for no class in the timetable this will not open any meetings`

`Note: The amount of subjects in pmi should match with the amount of subject's in the timetable. Also the amount of periods in timetable should match with the amount of timings in timetable-timings`