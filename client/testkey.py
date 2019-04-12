import sys, select, termios, tty
from websocket import create_connection
import json
import sys



speedBindings={
        's':(0.15,0),
        'w':(0.20,0),
        'x':(0.10,0),
        'a':(0.01,0),
        'd':(-0.01,0),
        'r':(0.01,0),
        'l':(-0.01,0),
        't':(0.15,0),

    }

def setspeed(ws, pin, sped):
#    ws = create_connection('ws://172.24.1.108')
    dict = {}  # Store data in dict
    dict['method'] = 'PWM'  # Poll temperature sensor
    dict['Pin'] = pin  # Read ESP32 internal temp
    dict['freq'] = 100  # Recor
    dict['duty']=sped

    ws.send(json.dumps(dict))

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    ws = create_connection('ws://172.24.1.108')
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0
    sped =0.15
    angle=0.15
    try:
        while(1):
            key = getKey()
            print (key)
            if key in speedBindings.keys():
                if (key=='a' or key=='d'):
                    pin =12
                    sped=sped+speedBindings[key][0]
                elif (key=='r' or key=='l'):
                    pin =13
                    angle=angle+speedBindings[key][0]
		elif (key=='w' or key=='x' or key=='s' ):
                    pin =12
                    sped=speedBindings[key][0]
                elif (key=='t'):
                    pin =13
                    angle=speedBindings[key][0]
                else:
		    sped=speedBindings[key][0]
                print(sped)
                if (pin==12):
	            setspeed(ws, pin, sped)
                elif (pin==13):
                    setspeed(ws, pin, angle) 
            else:
                if (key == '\x03'):
                    break
    except Exception as e:
        print(e)

    finally:

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	ws.close()
