import machine
from machine import Pin
from microWebSrv import MicroWebSrv
import json
from time import sleep

def cb_receive_text(webSocket, msg) :
    print("WS RECV TEXT : %s" % msg)
    dict=json.loads(msg)
    print(dict)
    if (dict['method']=="LED"):
        pv=machine.Pin(int(dict['Pin']), Pin.OUT)
        if (dict['cmd']=="on"):
            pv.on()
        else:
            pv.off() 
    else:
       print("cmd not implemented")

#    webSocket.SendText("Reply for %s" % dict['Pin'])

def cb_receive_binary(webSocket, data) :
    print("WS RECV DATA : %s" % data)

def cb_closed(webSocket) :
    print("WS CLOSED")

def cb_timer(timer, websocket):
    dict = {}  # Store data in dict
    dict['temp'] = 'ere'  # Poll temperature sensor
    print(dict['temp'])
    dict['internal'] = 'internal'  # Read ESP32 internal temp
    dict['time'] = 'wewe'  # Record current time
    websocket.SendText(json.dumps(dict))  # Convert data to JSON and send
    
def cb_accept_ws(webSocket, httpClient) :
    print("WS ACCEPT")
    webSocket.RecvTextCallback   = cb_receive_text
    webSocket.RecvBinaryCallback = cb_receive_binary
    webSocket.ClosedCallback 	 = cb_closed
#    cb = lambda timer: cb_timer(timer, webSocket)  # Use lambda to inject websocket
#    tm.init(period=3000, callback=cb)  # Init and start timer to poll temperature sensor

mws = MicroWebSrv()                 # TCP port 80 and files in /flash/www
mws.MaxWebSocketRecvLen     = 256   # Default is set to 1024
mws.WebSocketThreaded       = True  # WebSockets with new threads
mws.WebSocketStackSize      = 4096
mws.AcceptWebSocketCallback = cb_accept_ws # Function to receive WebSockets
mws.Start(threaded=False)  # Blocking call (CTRL-C to exit)

print('Cleaning up and exiting.')
mws.Stop()
#tm.deinit()
