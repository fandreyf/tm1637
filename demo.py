from time import sleep
from wiringpi import wiringPiSetup, GPIO, pinMode, digitalRead, digitalWrite, wiringPiISR
import tm1637

CLK = 1
DIO = 0
DELAY = 0.5


tm = tm1637.TM1637(clk=CLK, dio=DIO)
msg ='test'

while True:
    tm.show(msg)
    sleep(DELAY)
    tm.show('    ')
    sleep(DELAY)
