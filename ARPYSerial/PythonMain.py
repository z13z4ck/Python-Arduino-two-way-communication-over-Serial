import threading
from Py2ArdComs import *
import time

a = 0

def Communications():
	coms.run()


if __name__ == '__main__':
	coms = Py2ArdComs()
	t1 = threading.Thread( target=Communications, args="" )
	t1.start()

	while a<100:
		time.sleep(0.1)
		a = a+1
		SerRecieve = coms.FromArduino()
		print SerRecieve


	print "Stopping the program"
	coms.stop()