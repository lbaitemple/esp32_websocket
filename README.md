# esp32_websocket
You will need to install ampy which is used to upload files to esp32
```
sudo pip3 install adafruit-ampy
```

Once you have ampy, please verify that you have the serial port connected to esp32. Generally, the port on MacOS is
/dev/cu.SLAB_USBtoUART
```
 git clone https://github.com/lbaitemple/esp32_websocket
 cd esp32_websocket/
 cd esp32
 ampy microWebSocket.py
 ampy microWebTemplate.py
 ampy microWebSrv.py
 ampy ws.py
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
sudo pip install websocket-client
cd esp32_websocket/
cd client
python onPi.py
```
