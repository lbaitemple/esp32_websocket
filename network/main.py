#import webrepl
#webrepl.start()
import _thread

def connect():
    import network
    import slimDNS
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Pi3-AP-BAI', 'robotseverywhere')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    local_addr = sta_if.ifconfig()[0]
    server = slimDNS.SlimDNSServer(local_addr, "micropython")
    server.run_forever()

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)


_thread.start_new_thread(connect, ())

