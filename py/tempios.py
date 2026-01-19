import time
import threading

tiempo_restante = 200

def iniciar_conteo():
    def loop_tiempo():
        global tiempo_restante
        while tiempo_restante > 0:
            time.sleep(1)
            tiempo_restante -= 1


    hilo = threading.Thread(target=loop_tiempo, daemon=True)
    hilo.start()

def obtener_tiempo():
    global tiempo_restante
    return tiempo_restante