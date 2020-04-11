## Code to Automatically open Zoom program to join a meeting and record meeting is required

#####################################

## Please read through the read me to understand how this works to implement it for your set up

#####################################

## You need the pyautogui library, best way to install is using 'pip install pyautogui'
## in essence this script uses your keyboard and mouse to automatically open zoom from start menu and click and enter meeting id
## some settings of zoom itself needs to be changed for this script to work correctly

## documentation for pyautogui

########################################################

## https://pyautogui.readthedocs.io/en/latest/index.html

########################################################

## Created by Rohit Kannachel
## Not liable if this causes any issues.

# importing libraries
import pyautogui
import time


#####   Joining Zoom Meeting   ###################

#######################################################################################
#Enter the meeting id as a string here *important that it is in string format
meet_id = '5309464011'
#esc clicked to ensure that the win key will open up correctly in the next step
pyautogui.press('esc',interval=0.1)

time.sleep(0.2)

#these lines are simulating starting up zoom by pressing windows key and typing zoom to open program
pyautogui.press('win',interval=0.1)
pyautogui.write('zoom')
pyautogui.press('enter',interval=0.5)

#this part is important and may need to be altered to your needs according
#this part simulates clicking join meeting, entering meeting id and pressing enter to join
##x and y coordinates are pixel coordinates to click the join meeting button on your screen when zoom comes up, x increases as you go --> and y increases as you go down
## with a little trial and error you can match the coordinates for your system, this was done for a 1920x1080 (1080p) screen
pyautogui.click(x=830,y=430)
pyautogui.press('enter',interval=1)
## the interval of 1 second is important, if not there, then the meeting id will not be inputted
pyautogui.write(meet_id)
pyautogui.press('enter',interval=1)

##################################################################################


###### Recording meeting using Windows Game Bar  #############################


#######################################################################################


## this time buffer is added so that it accounts for the time taken to load into the meeting 
## a good buffer time is around 10-20 seconds before recording starts to ensure you're in the meeting


time.sleep(5)


## opening up windows game bar overlay
pyautogui.hotkey('win','g')
time.sleep(1)
## commencing screen recording
pyautogui.hotkey('win','alt','r')
time.sleep(1)
## closing windows game bar overlay
pyautogui.hotkey('win','g')


#### recording time amount
## however long you want, enter the time here in seconds, i.e. 30 minutes is 60*30 = 1800 seconds
## in windows game bar the default setting for time limit for recording is 2 hours,
## make sure to change this as you need
time.sleep(25)


## ending screen recording
pyautogui.hotkey('win','alt','r')
time.sleep(2)
## By default, screen captures are sent to a folder called captures in "videos" in "this PC"

## closing Zoom
pyautogui.hotkey('alt','f4')
time.sleep(0.5)
pyautogui.hotkey('alt','f4')

############################################################################################