import psutil 
import tkinter
from tkinter import *
import schedule
import time

def alert():
	tk = Tk()
	var = StringVar()
	label = Label( tk, textvariable=var, relief=RAISED )
	 
	var.set("100 % charged, please remove your charger.")
	label.pack()
	#####Extras#####
	tk.geometry("300x35")#The size of the box
	tk.wm_title("Battery Full")#The name of it
	tk.mainloop()

def checkBattery():
	battery = psutil.sensors_battery()
	if battery.power_plugged == True:
		if battery.percent == 100:
			alert()
 
schedule.every(3).seconds.do(checkBattery)

while 1:
	schedule.run_pending()
	time.sleep(1)


  
