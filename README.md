# esp32_websocket
You will need to install ampy which is used to upload files to esp32
```
sudo pip3 install adafruit-ampy
```

Once you have ampy, please verify that you have the serial port connected to esp32. Generally, the port on MacOS is
/dev/cu.SLAB_USBtoUART
```
 cd esp32/
 ampy microWebSocket.py
 ampy microWebTemplate.py
 ampy microWebSrv.py
 ampy ws.py
```
