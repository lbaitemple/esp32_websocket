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
You can change the wifi access point and password in line 12. After that, you can copy two files into esp32

```
ampy slimDNS.py 
ampy boot.py

```

If you everything runs fine, you can use the following command to connect esp32 for REPL
```
screen /dev/cu.SLAB_USBtoUART 115200
import boot
```
To exit from screen, you can use ctrl-A and ctrl-\ to exit. If everything goes well, you will have a fixed ip addresss for esp32. You can pin the address using the command in a new terminal window.
```
ping micropython.local
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
You can also see the ip address in onPi.py is micropython.local.
