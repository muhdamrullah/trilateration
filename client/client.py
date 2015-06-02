import json
import requests
from urlparse import urlparse
from triangulate import triangulate
import time

signalPower = 0

#Load JSON data from API
def pullApi(macAddress, ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/'
    target = urlparse(http + ipAddress + uri + macAddress) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    response = requests.get(url)
    data = response.json
    rawData =  data['Face']['power']
    return rawData

#Process the Signal data from API
def enterMAC(str, ipstr):
    rawData = pullApi(str, ipstr) 
    SignalStrength = 80 + int(rawData)
    SignalPower = "{0:0.1f}".format(SignalStrength)
    return SignalPower
   
#Change the 3 Signal data into a float
def get Coordinates():
    SignalPower = enterMAC(MAC_default, IP_first)
    Signal1 = float(SignalPower)
    SignalPower = enterMAC(MAC_default, IP_second)
    Signal2 = float(SignalPower)
    SignalPower = enterMAC(MAC_default, IP_third)
    Signal3 = float(SignalPower)
    coordinates = triangulate([(0.0, 0.0, Signal1), (40.0, 70.0, Signal2), (90.0, 0.0, Signal3)])
    print Signal1
    print Signal2
    print Signal3
    print coordinates
    
"""PART II: GUI"""

import turtle
t = turtle.Turtle()
tMobile = turtle.Turtle()

#User-defined coordinate system to shift screen
turtle.setworldcoordinates(-40, -40, 400, 400)

#Adding Icon Shapes
screen = turtle.Screen()
screen.addshape("MobileSignal.gif")
t.Mobile.shape("MobileSignal.gif")

#Drawing speeds
t.speed(100)
tMobile.speed(100)

def drawBoard():
    """draw grid board"""
    length = int(raw_input("Enter the place's length (metres): "))
    width = int(raw_input("Enter the place's width (metres): "))
    
    t.hideturtle()          #starts from middle
    t.goto(0,0)
    for i in range(2):      #draws frame
        t.down()
        t.forward(40*length)
        t.lt(90)
        t.forward(40*width)
        t.lt(90)
        t.up()
        
    for i in range(1, width):   #draws horizontal lines (y-axis)
        t.goto(0,40*i)
        t.down()
        t.forward(40*length)
        t.up()
        
    t.lt(90)
    
    for i in range(1,width):    #draws vertical lines (x-axis)
        t.goto(40*i,0)
        t.down()
        t.forward(40*width)
        t.up()
        
def trackSignal(x,y,MAC):
    tMobile.up()
    tMobile.goto( (40*x)/float(10), (40*y)/float(10) )
    tMobile.write(MAC, font=("Arial", 8, "bold"))
    
"""PART III: INTEGRATION"""
#FINAL COMMANDS

if __name__ == '__main__':
    MAC_default = raw_input("Enter the MAC Address: ");
    IP_first = raw_input("Enter the 1st IP Address: ");
    IP_second = raw_input("Enter the 2nd IP Address: ");
    IP_third = raw_input("Enter the 3rd IP Address: ");
    #Draw the grid board
    drawBoard()
    #Get coordinates via API every 10 secs and plot it
    while True:
        getCoordinates()
        trackSignal(x,y,MAC_default)
        time.sleep(10)
        
turtle.done
