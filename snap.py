import snap7
from implementation import cap
plc_ip = '192.168.0.1'
plc_rack = 0
plc_slot = 1

plc = snap7.client.Client()
plc.connect(plc_ip, plc_rack, plc_slot)

# Now you can perform operations on the PLC
state = plc.get_cpu_state()
print(f'CPU State: {state}')
def WriteBooltoDB(db_number, byte, size, bit,value):
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)
    snap7.util.set_bool(reading, 0, bit,value)
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading)



def WriteBooltoDB(db_number, byte, size, bit,value):
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)
    snap7.util.set_bool(reading, 0, bit,value)
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading)

WriteBooltoDB(1,0,1,0,c)
#n=ReadBoolFromInPut(0,1,2)
#h=c and n
#WriteBooltoInPut(0,1,0,n)
