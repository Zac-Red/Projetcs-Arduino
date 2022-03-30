
import matplotlib.pyplot as pit
import matplotlib.animation as animation
import threading 
import numpy as np
import serial

#from mpl_toolkits.mplot3d import Axes3D

serialData = []
serialData.append([0.0])
serialData.append([0.0])


def optenerdatos(out_dato):
    with serial.Serial("COM3", 9600) as arduino:
        while True:
            val = arduino.readline().decode('ascii')
            try:
                out_dato[1].append(float(val))
                if len(out_dato[1]) > 200:
                    out_dato[1].pop(0)
                    print(out_dato[1])
            except:
                pass

dataColector = threading.Thread(target = optenerdatos, args = (serialData,))
dataColector.start()

def actualizar(num, hl, data):
    dx = np.array(range(len(data[1])))
    dy = np.array(data[1])
    hl.set_data(dx, dy)
    return hl,


fig = pit.figure()
hl, = pit.plot(serialData[0], serialData[1])
pit.ylim(-7, 7)
pit.xlim(0, 200)

line_ani = animation.FuncAnimation(fig, actualizar, fargs=(hl, serialData), interval = 50, blit= False)

pit.show()
dataColector.join()

