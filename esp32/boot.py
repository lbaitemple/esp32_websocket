#import webrepl
#webrepl.start()

def connect():
    import network
#    import slimDNS
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Pi3-AP', 'robotseverywhere')
#        sta_if.connect('TUMiFiFAC', 'roboboat')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)


connect()

