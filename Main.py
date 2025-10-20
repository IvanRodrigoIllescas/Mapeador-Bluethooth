import keyboard, mouse

diccionario1 = {
    "volume up":"volume up",
    "volume down":"volume down",
    "previous track":"flecha izquierda",
    "next track":"flecha derecha",
    "play/pause media":"play/pause media",
    "browser start and home":""
}

diccionario2 = {
    "volume up":[0,-10],
    "volume down":[0,10],
    "previous track":[-10,0],
    "next track":[10,0],
    "play/pause media":"play/pause media",
    "browser start and home":""
}

diccionario3 = {
    "volume up":"volume up",
    "volume down":"volume down",
    "previous track":"flecha izquierda",
    "next track":"flecha derecha",
    "play/pause media":"play/pause media",
    "browser start and home":""
}


diccionario = diccionario2


def on_press(event):
    print(event.name)

    hacerAccion(diccionario[event.name])
    #
    # match event.name:
    #
    #     case "volume up":
    #         keyboard.send(diccionario["volume up"])
    #
    #     case "volume down":
    #         keyboard.send(diccionario["volume down"])
    #
    #     case "previous track":
    #         keyboard.send(diccionario["previous track"])
    #
    #     case "next track":
    #         keyboard.send(diccionario["next track"])
    #
    #     case "play/pause media":
    #         keyboard.send(diccionario["play/pause media"])
    #

def hacerAccion(accion: str):
    keyboard.send(accion)

def hacerAccion(coordenadas: list[int]):
    mouse.move(*coordenadas, absolute=False)








keyboard.on_press(on_press, suppress=True)

keyboard.wait('esc')


















#Modo 1 - Normal
#arriba-subir volumen
#abajo-bajar volumen
#izquierda-flecha izquieda
#derecha-flecha derecha
#
#
#Modo2 - Ratón
#
#Modo3 - scrolear
#
#
#
#
#
#
#
#
