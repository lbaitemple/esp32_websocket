import struct
import machine
import time as time_mo




#
#
def main():

    # initialize the connection
    #
    motor = conn(17, 16)

    id = 3

    # set_id
    #
    set_id(motor, id)

    while True:
        move(motor, id, 1000, 200)
        time_mo.sleep(2)
        move(motor, id, 0, 200)
        time_mo.sleep(2)


#
#
def conn(TX, RX):
    return machine.UART(2, baudrate=115200, rx=RX, tx=TX, timeout=10)


#
#
def set_id(motor, ID):


    # initialize the packet
    #
    buf = [0] * 7

    # setup the packet
    #
    buf[0] = b'\x55'
    buf[1] = b'\x55'
    buf[2] = b'\xFE'
    buf[3] = b'\x04'
    buf[4] = b'\x0D'
    buf[5] = bytes([ID])

    # calculate the checksum then assign it to the
    # TODO: make two lines ?
    #
    checksum_num = [checksum(buf, len(buf)-1)]
    checksum_byte = bytes(checksum_num)
    buf[6] = checksum_byte

    # this print is for debuging purpose
    #
    print(buf)

    # send the packet to the motor
    #
    for i in range(0, len(buf)):
        motor.write(buf[i])


#
#
# TODO: maybe no need to pass the motor if daisychain ?
#
def move(motor, ID, position, time):

    start = time_mo.time()
    # initialize the packet
    #
    buf = [0] * 10

    # get the high and low bytes for both time and position
    #
    (pos_high, pos_low) = high_low_byte(position)
    (time_high, time_low) = high_low_byte(time)

    # setup the packet
    #
    buf[0] = b'\x55'
    buf[1] = b'\x55'
    buf[2] = bytes([ID])
    buf[3] = b'\x07'
    buf[4] = b'\x01'
    buf[5] = bytes([int(pos_low)])
    buf[6] = bytes([int(pos_high)])
    buf[7] = bytes([int(time_low)])
    buf[8] = bytes([int(time_high)])

    # calculate the checksum then assign it to the
    # TODO: make two lines ?
    #
    checksum_num = [checksum(buf, len(buf)-1)]
    checksum_byte = bytes(checksum_num)
    buf[9] = checksum_byte

    # this print is for debuging purpose
    #
    print(buf)

    # send the packet to the motor
    #
    for i in range(0, len(buf)):
        motor.write(buf[i])

    end = time_mo.time()

    print(end - start)


# calculate the checksum for the packet
# sums all bytes from [3: LAST-1]
# then takes the ones comp to assign it to the last byte in the packet
#
def checksum(ibuf, maxindx):

    # initialize the sum
    #
    sum = 0

    # sum the bytes except the fries two
    #
    for i in range(2, maxindx):
        byte = struct.unpack('>H', bytearray(b'\x00'+ibuf[i]))[0]
        sum += byte

    # take the one's comp of the sum and assign it to the last byte
    #
    ibuf[maxindx] = ones_comp(sum)
    return ibuf[maxindx]


# get ones comp of an 8bit number by getting the byte
# then XOR with 0xFF
#
def ones_comp(num):
    byte = struct.pack('<H', num)
    return (byte[0]^0xFF)


# take a 16bit number and return a tuple of two bytes as high and low
#
def high_low_byte(num):
    byte = struct.pack('<H', num)
    return (hex(byte[1]), hex(byte[0]))

# start main
#
if __name__ == '__main__':
    main()
