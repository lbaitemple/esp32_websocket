from websocket import create_connection
import json
import sys

ws = create_connection('ws://micropython.local.')

dict = {}  # Store data in dict
dict['method'] = 'PWM'  # Poll temperature sensor
dict['Pin'] = 12  # Read ESP32 internal temp
dict['freq'] = 100  # Recor
dict['duty']=0.20

ws.send(json.dumps(dict))
