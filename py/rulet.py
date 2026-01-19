import random
import time
import threading



ruleta = {
    1: [1, 1, 2, 2, 2, 4],
    2: [1, 2, 2, 3, 3, 3],
    3: [2, 3, 3, 4, 4, 4],
    4: [3, 3, 4, 4, 4, 5, 5, 5, 5, 1],
    5: [5, 5, 5, 5, 5, 6, 6, 6, 4],
    6: [5, 4, 3, 2, 1]
}

numero_actual = 5

def ruleta_en_segundo_plano():
    global numero_actual
    while True:
        time.sleep(5)
        numero_actual = random.choice(ruleta[numero_actual])



hilo = threading.Thread(target=ruleta_en_segundo_plano, daemon=True)
hilo.start()