import pygame
import os
import rulet
import time
import bateria_engine  # <--- Importamos el archivo de la batería
import tempios

pygame.init()
pygame.mixer.init()

activa = 0
datos_compartidos = {"estado": "principal", "activa": activa}

bateria_engine.iniciar_hilo_bateria(datos_compartidos)
# -----------------------------------------

pantalla = pygame.display.set_mode((1280, 720))             #Pon 1920x1080 para la pantalla completa y 1280x720 para la ventana
pygame.display.set_caption("Regla: Solo cambiar desde principal")
fuente = pygame.font.Font(None, 50)



# Cargar imágenes
ruta = "py"
img_principal = pygame.image.load(os.path.join(ruta, "../fotos/PantallaD.jpg"))
PuertaAbiertaBien = pygame.image.load(os.path.join(ruta, "../fotos/PuertaAbiertaD.jpg"))
PuertaAbiertaMal = pygame.image.load(os.path.join(ruta, "../fotos/PuertaAbiertaBichoD.jpg"))
PuertaCerradaBien = pygame.image.load(os.path.join(ruta, "../fotos/PuertaCerradaD.jpg"))
PuertaCerradaMal = pygame.image.load(os.path.join(ruta, "../fotos/PuertaCerradaD.jpg"))
Ventana12 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana12.png"))
Ventana1 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana1.png"))
Ventana2 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana2.png"))
Ventana3 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana3.png"))
Ventana4 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana4.png"))
Ventana5 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana5.png"))


Victoria = pygame.image.load(os.path.join(ruta, "../fotos/Victoria.png"))
Derrota = pygame.image.load(os.path.join(ruta, "../fotos/Derrota.png"))

PasilloPuertaPrincipal = pygame.image.load(os.path.join(ruta, "../fotos/CamaraPasilloPuertaD.jpg"))
PasilloPuertaPrincipalBicho = pygame.image.load(os.path.join(ruta, "../fotos/CamaraPasilloPuertaBichoD.jpg"))
Comedor = pygame.image.load(os.path.join(ruta, "../fotos/ComedorD.jpg"))
ComedorBicho = pygame.image.load(os.path.join(ruta, "../fotos/ComedorBichoD.jpg"))
Cocina = pygame.image.load(os.path.join(ruta, "../fotos/CocinaD.jpg"))
CocinaBicho = pygame.image.load(os.path.join(ruta, "../fotos/CocinaBichoD.jpg"))
Pasillo4 = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo4D.jpg"))
Pasillo4Bicho = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo4BichoD.jpg"))
Pasillo5A = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo5AbiertoD.jpg"))
Pasillo5C = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo5CerradoD.jpg"))
Pasillo5BichoA = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo5BichoAbiertoD.jpg"))
Pasillo5BichoC = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo5BichoCerradoD.jpg"))


CamaraRuido = pygame.mixer.Sound(os.path.join(ruta, "../audio/Camara_Ruido.mp3"))
CerrarPuerta = pygame.mixer.Sound(os.path.join(ruta, "../audio/Cerrar_Puerta.mp3"))
AbrirPuerta = pygame.mixer.Sound(os.path.join(ruta, "../audio/Abrir_Puerta.mp3"))


# Estado actual
estado = "principal"
conhora = 0
abierta = 1
puer = 0
perdido = 0

def obtener_imagen(estado):
    if estado == "principal":
        return img_principal
    if estado == "victoria":
        return Victoria
    if estado == "derrota":
        return Derrota
    elif estado == "1":
        return PuertaAbiertaBien
    elif estado == "12":
        return PuertaAbiertaMal
    elif estado == "13":
        return PuertaCerradaBien
    elif estado == "14":
        return PuertaCerradaMal
    elif estado == "3":             #12
        return Ventana12
    elif estado == "31":             #1
        return Ventana1        
    elif estado == "32":             #2
        return Ventana2
    elif estado == "33":             #3
        return Ventana3
    elif estado == "34":             #4
        return Ventana4
    elif estado == "35":             #5
        return Ventana5
    elif estado == "4":
        return PasilloPuertaPrincipal
    elif estado == "5":
        return Cocina
    elif estado == "6":
        return Comedor
    elif estado == "7":
        return Pasillo4
    elif estado == "8":
        return Pasillo5A
    elif estado == "9":
        return Pasillo5C
    elif estado == "41":
        return PasilloPuertaPrincipalBicho
    elif estado == "51":
        return CocinaBicho
    elif estado == "61":
        return ComedorBicho
    elif estado == "71":
        return Pasillo4Bicho    
    elif estado == "81":
        return Pasillo5BichoA
    elif estado == "82":
        return Pasillo5BichoC

tempios.iniciar_conteo()

    
corriendo = True
while corriendo:
    datos_compartidos["estado"] = estado
    datos_compartidos["abierta"] = abierta
    valor_bat = bateria_engine.obtener_bateria()
    valor_tiempo = tempios.obtener_tiempo()

    if valor_tiempo == 0:
        estado = "victoria"



    if valor_tiempo != 0:
        conhora = 1

        tiempo_restante = valor_tiempo
        if perdido == 1:
                estado = "derrota"
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if estado == "principal":
                    if rulet.numero_actual == 1:
                        if evento.key == pygame.K_w:
                            estado = "41"
                    if rulet.numero_actual != 1:
                        if evento.key == pygame.K_w:
                            estado = "4"
                    if evento.key == pygame.K_d:
                        if conhora == 2:
                            if tempios.tiempo_restante <= 200 and tempios.tiempo_restante >= 167:
                                estado = "3"        #12
                            elif tempios.tiempo_restante <= 166 and tempios.tiempo_restante >= 134:
                                estado = "31"       #1
                            elif tempios.tiempo_restante <= 133 and tempios.tiempo_restante >= 101:
                                estado = "32"       #2
                            elif tempios.tiempo_restante <= 100 and tempios.tiempo_restante >= 67:
                                estado = "33"       #3
                            elif tempios.tiempo_restante <= 66 and tempios.tiempo_restante >= 34:
                                estado = "34"       #4
                            elif tempios.tiempo_restante <= 33 and tempios.tiempo_restante >= 0:
                                estado = "33"       #5
                    if evento.key == pygame.K_a:
                        if valor_bat == 0:
                            abierta = 1
                        puer = 1
                        if (rulet.numero_actual != 5 and rulet.numero_actual != 6) or (rulet.numero_actual != 6 and rulet.numero_actual != 5):            #AAAA
                            if valor_bat != 0:
                                if abierta == 1:
                                    estado = "1"
                                else:
                                    estado = "13"
                            else:
                                estado = "1"
                            if valor_bat != 0:
                                if abierta == 0:
                                    estado = "13"
                                else:
                                    estado = "1"
                            else:
                                estado = "1"
                        if (rulet.numero_actual == 5 and rulet.numero_actual != 6) or (rulet.numero_actual == 6 and rulet.numero_actual != 5):            #AAAA
                            if valor_bat != 0:
                                if abierta == 1:
                                    estado = "12"
                                else:
                                    estado = "14"
                            else:
                                estado = "12"
                            if valor_bat != 0:
                                if abierta == 0:
                                    estado = "14"
                                else:
                                    estado = "12"
                            else:
                                estado = "12"

                elif puer == 1:
                    if (rulet.numero_actual != 5 and rulet.numero_actual != 6) or (rulet.numero_actual != 6 and rulet.numero_actual != 5):           #AAAA
                        if valor_bat == 0:
                            abierta = 1
                        enemigo = 1
                        if enemigo == 1:
                            if abierta == 1:
                                estado = "1"
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                
                                # PARTE FALTANTE CON LA BATERIA
                                if evento.key == pygame.K_SPACE and valor_bat != 0: 
                                    enemigo = 1
                                    estado = "13"
                                    abierta = 0
                                    CerrarPuerta.play()
                                
                                elif evento.key == pygame.K_SPACE:
                                    enemigo = 1
                                    estado = "1"
                                    abierta = 1
                                    AbrirPuerta.play()

                            elif abierta == 0:
                                estado = "13"
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 1
                                    estado = "1"
                                    abierta = 1
                                    AbrirPuerta.play()
                            elif estado == "13":
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 1
                                    estado = "1"
                                    abierta = 1

                    elif (rulet.numero_actual == 5 and rulet.numero_actual != 6) or (rulet.numero_actual == 6 and rulet.numero_actual != 5):          #AAAA
                        if valor_bat == 0:
                            abierta = 1
                        enemigo = 2
                        if enemigo == 2:
                            if abierta == 1:
                                estado = "12"
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                    
                                    
                                
                                if evento.key == pygame.K_SPACE and valor_bat != 0:
                                    enemigo = 2
                                    estado = "14"
                                    abierta = 0
                                    CerrarPuerta.play()

                            elif abierta == 0:
                                if valor_bat > 0:
                                    estado = "14"
                                else:
                                    estado = "12"
                                    abierta = 1
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 2
                                    estado = "12"
                                    abierta = 1
                                    AbrirPuerta.play()
                            elif estado == "14":
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 2
                                    estado = "12"

                else:
                    if evento.key == pygame.K_s:
                        estado = "principal"
                        puer = 0
                        if valor_bat == 0:
                            abierta = 1
                    else:
                        if valor_bat == 0:
                            abierta = 1
                        if evento.type == pygame.KEYDOWN:
                # ----------- Cambios permitidos de la camara 5 ------------
                            if estado == "8" or estado == "9":
                                if evento.key == pygame.K_5:
                                    if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                        if abierta == 1:
                                            estado = "81"
                                            enemigo = 0
                                        elif abierta == 0:
                                            estado = "82"
                                            enemigo = 0
                                    elif rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                        if abierta == 1:
                                            estado = "81"
                                            enemigo = 0
                                        elif abierta == 0:
                                            estado = "82"
                                            enemigo = 0
                                    elif rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                        if abierta == 1:
                                            estado = "8"
                                            enemigo = 0
                                        elif abierta == 0:
                                            estado = "9"
                                            enemigo = 0
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()
                # ----------- Cambios permitidos de la camara 5 ------------
                            if estado == "81" or estado == "82":
                                if evento.key == pygame.K_5:
                                    if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                        if abierta == 1:
                                            estado = "81"
                                            enemigo = 1
                                        elif abierta == 0:
                                            estado = "82"
                                            enemigo = 1
                                    elif rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                        if abierta == 1:
                                            estado = "81"
                                        elif abierta == 0:
                                            estado = "82"
                                    elif rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                        if abierta == 1:
                                            estado = "8"
                                            enemigo = 1
                                        elif abierta == 0:
                                            estado = "9"
                                            enemigo = 1
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()

                # ----------- Cambios permitidos de la camara 1 ------------
                            if estado == "4":
                                if evento.key == pygame.K_1:
                                    if rulet.numero_actual == 1:
                                        estado = "41"
                                    elif rulet.numero_actual != 1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()
                # ----------- Cambios permitidos de la camara 1 ------------
                            if estado == "41":
                                if evento.key == pygame.K_1:
                                    if rulet.numero_actual == 1:
                                        estado = "41"
                                    elif rulet.numero_actual != 1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()

                # ----------- Cambios permitidos de la camara 2 ------------
                            if estado == "5":
                                if evento.key == pygame.K_2:
                                    if rulet.numero_actual == 2:
                                        estado = "51"
                                    elif rulet.numero_actual != 2:
                                        estado = "5"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()
                # ----------- Cambios permitidos de la camara 2 ------------
                            if estado == "51":
                                if evento.key == pygame.K_2:
                                    if rulet.numero_actual == 2:
                                        estado = "51"
                                    elif rulet.numero_actual != 2:
                                        estado = "5"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()

                # ----------- Cambios permitidos de la camara 3 ------------
                            if estado == "6":
                                if evento.key == pygame.K_3:
                                    if rulet.numero_actual == 3:
                                        estado = "61"
                                    elif rulet.numero_actual != 3:
                                        estado = "6"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()
                # ----------- Cambios permitidos de la camara 3 ------------
                            if estado == "61":
                                if evento.key == pygame.K_3:
                                    if rulet.numero_actual == 3:
                                        estado = "61"
                                    elif rulet.numero_actual != 3:
                                        estado = "6"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()

                # ----------- Cambios permitidos de la camara 4 ------------
                            if estado == "7":
                                if evento.key == pygame.K_4:
                                    if rulet.numero_actual == 4:
                                        estado = "71"
                                    elif rulet.numero_actual != 4:
                                        estado = "7"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()
                # ----------- Cambios permitidos de la camara 4 ------------
                            if estado == "71":
                                if evento.key == pygame.K_4:
                                    if rulet.numero_actual == 4:
                                        estado = "71"
                                    elif rulet.numero_actual != 4:
                                        estado = "7"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                        CamaraRuido.play()
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                        CamaraRuido.play()
                                if rulet.numero_actual == 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "81"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "82"
                                            CamaraRuido.play()
                                if rulet.numero_actual != 5 and rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        if abierta == 1:
                                            estado = "8"
                                            CamaraRuido.play()
                                        elif abierta == 0:
                                            estado = "9"
                                            CamaraRuido.play()
                # ----------- Perdido ------------
        if rulet.numero_actual == 6:
            if valor_bat != 0:
                if abierta == 1:
                    perdido = 1

            else:
                if abierta == 1:
                    perdido = 1

                else:
                    perdido = 1

    bate = fuente.render(str(valor_bat) + "%", True, (255, 255, 255))
    minutos = valor_tiempo // 60
    seg_restantes = valor_tiempo % 60
    tiempo = f"{minutos:02}:{seg_restantes:02}"
    tiempoV = fuente.render(str(tiempo), True, (255, 255, 255))
    pantalla.blit(obtener_imagen(estado), (0, 0))       #Si es 1920x1080 poner (360,0), si es 1280x720 poner (0,0)
    pantalla.blit(bate, (10, 10))
    pantalla.blit(tiempoV, (1180, 10))
    if valor_bat == 0:
        abierta = 1
    print(abierta)
    pygame.display.update()
    if estado == "victoria" or estado == "derrota":
        time.sleep(5)
        pygame.quit()
        pygame.display.update()

pygame.quit()