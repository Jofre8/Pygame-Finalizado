import time
import threading

bateria = 100

def iniciar_hilo_bateria(referencia_juego):
    """
    Recibe un diccionario o un objeto para poder leer 'estado' y 'activa'
    desde el código principal en tiempo real.
    """
    def loop_bateria():
        global bateria
        while True:
            time.sleep(3)
            
            consumo = 1
            if referencia_juego['abierta'] == 0:
                consumo = 2
                
            bateria -= consumo
            if bateria < 0:
                bateria = 0


    hilo = threading.Thread(target=loop_bateria, daemon=True)
    hilo.start()

def obtener_bateria():
    global bateria
    return bateria