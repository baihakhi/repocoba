import Adafruit_AMG88xx
from time import sleep
from firebase import firebase

url = 'https://.com'
realDB = firebase.FirebaseApplication(url, none)
while True:
    #receive value from GPIO

    #upload to firebase DB
    result = firebase.patch('sensor/amg/', {'temp': temp,'time': time})

    sleep(2)
    print("uploading data...")
    sleep(2)
    print("upload sukses")

    #get data from firebase
    result = firebase.get('sensor/amg/temp',none)
    print(result)

    result = firebase.get('sensor/amg/time',none)
    print(result)