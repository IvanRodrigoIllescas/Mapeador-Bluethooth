import keyboard, mouse

def on_press(event):
    print(event.name)

    match event.name:

        case "volume up":
            mouse.move(100,100)

        case "volume down":
            print("bajando volumen")

        case "next track":
            keyboard.send("flecha derecha")
        case "previous track":
            keyboard.send("flecha izquierda")

        case "play/pause media":
            print("play/pause")




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
