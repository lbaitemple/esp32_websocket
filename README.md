# esp32_websocket
In this project, we will use a raspberry pi 3B+ to send websocket commands to an esp32 pin12 and pin13 with 100HZ PWM signals to control wheel steering and esc speed controller.  Install a rshell command
```
sudo pip3 install rshell
```
Once you have ampy, please verify that you have the serial port connected to esp32. Generally, the port on MacOS is
/dev/cu.SLAB_USBtoUART
```
 git clone https://github.com/lbaitemple/esp32_websocket
 cd esp32_websocket/esp32
 ampy microWebSocket.py
 ampy microWebTemplate.py
 ampy microWebSrv.py
 ampy ws.py
```

Now,  you can setup the wifi and let esp32 ipaddress as micropython.local. To do that
```
cd ..\network
nano -c boot.py
```

If you everything runs fine, you can use the following command to connect esp32 for REPL
```
screen /dev/cu.SLAB_USBtoUART 115200

```
It allows you to serially connect to esp32 (given you have wifi connection in boot.py), you will need to run
```
import ws
```

Open another terminal, you will need to do
```
cd client
python onPi.py
```
