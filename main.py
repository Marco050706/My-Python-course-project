from machine import Pin
from time import sleep

segmentos = [Pin(pin, Pin.OUT) for pin in [2, 4, 5, 18, 22, 21]]
boton = Pin(33, Pin.IN, Pin.PULL_UP)
boton_2 = Pin(32, Pin.IN, Pin.PULL_UP)
led = Pin(23, Pin.OUT)

numero_actual = 0

boton_1_prev = 1
boton_2_prev = 1
    
def mostrar_numero(num):
    numeros_segmentos = {
        
        1: [0,1,1,0,0,0], # 1
        2: [1,1,0,1,0,1], # 2
        3: [1,1,1,1,0,1], # 3
        4: [0,1,1,0,1,1], # 4
        5: [1, 0, 1, 1, 1, 1],  # 5 
        6: [1, 0, 1, 1, 1, 1],  # 6 
        7: [1, 1, 1, 0, 0, 0],  # 7 
        8: [1, 1, 1, 1, 1, 1],  # 8
        9: [1, 1, 1, 1, 1, 1],  # 9
        
    }
    patron  = numeros_segmentos.get(num, [0,0,0,0,0,0])
    for x in range(len(segmentos)):
        segmentos[x].value(patron[x])
    
numeros_invalidos = [0, 2, 6, 8]

while True:
    if boton.value() == 0 and boton_2.value() == 0:
        numero_actual = 1

    elif boton_1_prev == 1 and boton.value() == 0:
        numero_actual += 1
        # Saltar números inválidos subiendo
        while numero_actual in numeros_invalidos:
            numero_actual += 1
        if numero_actual > 9:
            numero_actual = 1  # Vuelve a 1 si pasa de 9

    elif boton_2_prev == 1 and boton_2.value() == 0:
        numero_actual -= 1
        # Saltar números inválidos bajando
        while numero_actual in numeros_invalidos:
            numero_actual -= 1
        if numero_actual < 1:
            numero_actual = 9  # Vuelve a 9 si baja de 1
        
    mostrar_numero(numero_actual)

    boton_1_prev = boton.value()
    boton_2_prev = boton_2.value()

    if boton_2.value() == 0 and boton.value() == 0:
        led.value(1)
    else:
        led.value(0)

    sleep(0.1)
