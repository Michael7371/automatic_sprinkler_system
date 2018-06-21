from flask import Flask, Response, render_template,request, send_from_directory,redirect,url_for
import sys
sys.path.insert(0,'../HVLib')
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

Zone1 = 3
Zone2 = 5
Zone3 = 7
Zone4 = 8

GPIO.setup(Zone1, GPIO.OUT, initial=1)
GPIO.setup(Zone2, GPIO.OUT, initial=1)
GPIO.setup(Zone3, GPIO.OUT, initial=1)
GPIO.setup(Zone4, GPIO.OUT, initial=1)

global sliderValue
sliderValue = 0

#create webpage
app = Flask(__name__)

#routing pictures
@app.route('/Sprinkler_Page', methods=['GET', 'POST'])
def picture(): 
    return render_template('Sprinkler_Page.html')

#default route
@app.route('/')
def index():
   # return render_template('test.html')
   return render_template('Sprinkler_Page.html')

#special route that allows for the feed to be streamed
@app.route('/updateValues')
def updateValues():
    global sliderValue
    sliderValue = request.args.get('sliderValue',-1,type=int)
    print(sliderValue)
    return ('',204) 

@app.route('/button_update')
def button_update():
    buttonvalue1 = request.args.get('buttonvalue1',1,type=int)
    print(buttonvalue1)
    Zones(buttonvalue1)
    return ('',204) 

def Zones(buttonvalue1):
    if buttonvalue1 == 1:
        print("Zone 1")
        clearZones()
        GPIO.output(Zone1, 0)
        print("complete")
    if buttonvalue1 == 2:
        print("Zone 2")
        clearZones()
        GPIO.output(Zone2, 0)
        print("complete")
    if buttonvalue1 == 3:
        print("Zone 3")
        clearZones()
        GPIO.output(Zone3, 0)
        print("complete")
    if buttonvalue1 == 4:
        print("Zone 4")
        clearZones()
        GPIO.output(Zone4, 0)
        print("complete")

def clearZones():
    GPIO.output(Zone1, 1)
    GPIO.output(Zone2, 1)
    GPIO.output(Zone3, 1)
    GPIO.output(Zone4, 1)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5800,threaded = True)