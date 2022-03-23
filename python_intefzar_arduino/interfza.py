
from tkinter import *
import serial, time, os, keyboard


arduino = serial.Serial("COM5", 9600)


def modo_analogo():
    os.system ("cls")
    starciclo = 1
    while starciclo != 0:
        val = arduino.readline()
        cad = int(val.decode('ascii'))
        if cad == 2:
            print("\nLed 1 Encendido")
        if cad == 3:
            print("\nLed 1 apagado")
        if cad == 5:
            print("\nLed 2 Encendido")
        if cad == 0:
            print("\nLed 2 apagado")
            starciclo = 0



def closeinterface():
    arduino.close()
    interfaz.destroy()


def encender_led():
    contador = int(lbl_valor["text"])
    lbl_valor["text"] = f"{contador + 1}"

    if contador == 2:
        arduino.write(b'1')
        time.sleep(1)
        
    if contador == 4:
        arduino.write(b'2')
        lbl_valor["text"] = 1
        time.sleep(1)


def Modo_consola():
    os.system ("cls")
    print("\nPara ocilar los leds presione la tecla A & L")
    iniciociclo = 1
    while iniciociclo != 0: 
        if  keyboard.is_pressed('a') and keyboard.is_pressed('L'):
            print("\nOcilando led 1 y led 2")
            arduino.write(b'a')
            time.sleep(1)
        if keyboard.is_pressed('b'):
            iniciociclo = 0
            print("\nApagando led 1 y led 2")
            arduino.write(b'b')
            time.sleep(1)



interfaz = Tk()
interfaz.geometry("600x200")
interfaz.title("encender leds")

titulo = Frame()
titulo.config(bg="gray", width="600", height = "80")
titulo.place(x = 0, y = 0)

titulolb = Label(titulo, text="Enceder leds desde python interface", bg="gray", fg="white", font=("Arial", 15))
titulolb.place(x = 110, y = 20)

botones = Frame()
botones.config(bg="red", width = "600", height = "120") 
botones.place(x = 0, y = 80)

btpower = Button(botones, text = "Power LED1", command= encender_led)
btpower.place(x = 70, y = 40)

lbl_title = Label(botones, text = "pulsos")
lbl_title.place(x = 150, y =40)

lbl_valor = Label(botones, text = 1)
lbl_valor.place(x = 200, y =40)


btoff = Button(botones, text = "Modo de consola", command= Modo_consola)
btoff.place(x = 350, y = 40)


btanalog = Button(botones, text = "Modo_analogo", command= modo_analogo)
btanalog.place(x = 150, y = 90)

btnclose = Button(botones, text = "Cerrar", command = closeinterface)
btnclose.place(x = 420, y = 90)


interfaz.mainloop()



