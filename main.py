
#      EL CONVERSOR RURAL - CÓDIGO FINAL

# CONFIGURACIÓN Y PRECIOS
LISTA_COSAS  = ["gallina", "patata", "cabra", "huevos", "caballo", "Salir"]
PRECIOS_LEÑA = [6,         1.33,     5,       0.25,     12,        0]

mi_leña = 0  # mochila de leña

# Variables para saber qué está pasando
estoy_cerca_vecino = False
estoy_cerca_arbol  = False

# Definimos el tipo explícitamente para evitar errores
arbol_cercano: Sprite = None

# ACCIONES DEL JUEGO (FUNCIONES)

def calcular_leña_necesaria(cosa_que_quieres: str, cantidad: number):
    # Buscamos el precio en la lista
    precio_unitario = 0
    encontrado = False
    
    index = 0
    while index < len(LISTA_COSAS):
        if LISTA_COSAS[index] == cosa_que_quieres:
            precio_unitario = PRECIOS_LEÑA[index]
            encontrado = True
            break
        index += 1
        
    if not encontrado:
        game.splash("¡Esa cosa no existe!")
        return -1

    # Calculamos el total
    total_leña = cantidad * precio_unitario
    
    # Redondeamos a 2 decimales
    total_leña = Math.round(total_leña * 100) / 100
    return total_leña

def abrir_tienda():
    global mi_leña
    # Paramos al jugador para que no se mueva mientras compra
    controller.move_sprite(jugador, 0, 0)
    
    # Creamos el texto del menú
    texto_menu = ""
    k = 0
    while k < len(LISTA_COSAS):
        texto_menu = texto_menu + LISTA_COSAS[k]
        if k < len(LISTA_COSAS) - 1:
            texto_menu = texto_menu + ", "
        k += 1
        
    # Preguntamos al jugador
    eleccion = game.ask_for_string("¿Qué quieres? (" + texto_menu + ")")
    
    if eleccion:
        if eleccion == "Salir" or eleccion == "salir":
            game.splash("¡Hasta luego!")
        else:
            cuantos = game.ask_for_number("¿Cuántas unidades de " + eleccion + "?")
            
            # Regla de logica , los animales no se venden por trozos
            es_animal = (eleccion == "gallina" or eleccion == "cabra" or eleccion == "caballo")
            
            if es_animal and (cuantos % 1 != 0):
                game.splash("¡Error! Los animales deben", "estar vivos y enteros.")
            elif cuantos < 0:
                game.splash("No puedes pedir negativos.")
            else:
                # Si todo está bien, calculamos
                coste_total = calcular_leña_necesaria(eleccion, cuantos)
                
                if coste_total != -1:
                    # Mostramos la cuenta
                    game.splash("Cuesta " + str(coste_total) + " kg.", "Tienes: " + str(mi_leña) + " kg")
                    
                    if mi_leña >= coste_total:
                        mi_leña = mi_leña - coste_total
                        game.splash("¡Trato hecho!", "Te sobran " + str(mi_leña) + " kg.")
                    else:
                        game.splash("Te falta leña para pagar.")

    # Devolvemos el control al jugador
    controller.move_sprite(jugador, 80, 80)

# PREPARACIÓN DEL MUNDO

# Crear al Jugador
jugador = sprites.create(assets.image("""nena-front"""), SpriteKind.player)
jugador.set_position(130, 155)
jugador.z = 10
scene.camera_follow_sprite(jugador)
controller.move_sprite(jugador, 80, 80)

# Crear al Vecino
vecino = sprites.create(img("""
    . . . . f f f f . . . . .
    . . f f f f f f f f . . .
    . f f f f f f c f f f . .
    f f f f f f c c f f f c .
    f f f c f f f f f f f c .
    c c c f f f e e f f c c .
    f f f f f e e f f c c f .
    f f f b f e e f b f f f .
    . f 4 1 f 4 4 f 1 4 f . .
    . f e 4 4 4 4 4 4 e f . .
    . f f f e e e e f f f . .
    f e f b 7 7 7 7 b f e f .
    e 4 f 7 7 7 7 7 7 f 4 e .
    e e f 6 6 6 6 6 6 f e e .
    . . . f f f f f f . . . .
    . . . f f . . f f . . . .
"""), SpriteKind.player)
vecino.set_position(140, 140)

# Crear el Mercado
decorado_mercado = sprites.create(img("""
    ....................e2e22e2e....................
    .................222eee22e2e222.................
    ..............222e22e2e22eee22e222..............
    ...........e22e22eeee2e22e2eeee22e22e...........
    ........eeee22e22e22e2e22e2e22e22e22eeee........
    .....222e22e22eeee22e2e22e2e22eeee22e22e222.....
    ...22eeee22e22e22e22eee22eee22e22e22e22eeee22...
    4cc22e22e22eeee22e22e2e22e2e22e22eeee22e22e22cc4
    6c6eee22e22e22e22e22e2e22e2e22e22e22e22e22eee6c6
    46622e22eeee22e22eeee2e22e2eeee22e22eeee22e22664
    46622e22e22e22eeee22e2e22e2e22eeee22e22e22e22664
    4cc22eeee22e22e22e22eee22eee22e22e22e22eeee22cc4
    6c622e22e22eeee22e22e2e22e2e22e22eeee22e22e226c6
    466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
    46622e22eeee22e22e22e2e22e2e22e22e22eeee22e22664
    4cc22e22e22e22e22eeee2e22e2eeee22e22e22e22e22cc4
    6c622eeee22e22eeee22eee22eee22eeee22e22eeee226c6
    46622e22e22eeee22e22e2e22e2e22e22eeee22e22e22664
    466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
    4cc22e22eeee22e22e22e2e22e2e22e22e22eeee22e22cc4
    6c622e22e22e22e22e22eee22eee22e22e22e22e22e226c6
    46622eeee22e22e22eeecc6666cceee22e22e22eeee22664
    46622e22e22e22eeecc6666666666cceee22e22e22e22664
    4cceee22e22eeecc66666cccccc66666cceee22e22eeecc4
    6c622e22eeecc66666cc64444446cc66666cceee22e226c6
    46622e22cc66666cc64444444444446cc66666cc22e22664
    46622cc6666ccc64444444444444444446ccc6666cc22664
    4ccc6666ccc6444bcc666666666666ccb4446ccc6666ccc4
    cccccccc6666666cb44444444444444bc6666666cccccccc
    64444444444446c444444444444444444c64444444444446
    66cb444444444cb411111111111111114bc444444444bc66
    666cccccccccccd166666666666666661dccccccccccc666
    6666444444444c116eeeeeeeeeeeeee611c4444444446666
    666e2222222e4c16e4e44e44e44e44ee61c4e2222222e666
    666eeeeeeeee4c16e4e44e44e44e44ee61c4eeeeeeeee666
    666eddddddde4c66f4e4effffffe44ee66c4eddddddde666
    666edffdffde4c66f4effffffffff4ee66c4edffdffde666
    666edccdccde4c66f4effffffffffeee66c4edccdccde666
    666eddddddde4c66f4eeeeeeeeeeeeee66c4eddddddde666
    c66edffdffde4c66e4e44e44e44e44ee66c4edffdffde66c
    c66edccdccde4c66e4e44e44e44e44ee66c4edccdccde66c
    cc66666666664c66e4e44e44e44feeee66c46666666666cc
    .c66444444444c66e4e44e44e44ffffe66c44444444466c.
    ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee4c..
    ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
    ....644444444c66f4e44e44e44e44ee66c444444446....
    .....64eee444c66f4e44e44e44e44ee66c444eee46.....
    ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
"""), SpriteKind.player)
decorado_mercado.set_position(130, 115)

# PLANTAR ÁRBOLES
# imagen arbol
imagen_arbol = assets.image("forestTree0")
# posion de los arboles
posiciones_arboles = [
    [20, 20], [50, 20], [20, 50], [40, 40],
    [235, 20], [205, 20], [235, 50], [215, 40],
    [20, 235], [50, 235], [20, 205], [40, 215],
    [235, 235], [205, 235], [235, 205], [215, 215]
]
# for para plantarlos
for pos in posiciones_arboles:
    nuevo_arbol = sprites.create(imagen_arbol, SpriteKind.food)
    nuevo_arbol.set_position(pos[0], pos[1])

# Cargar Mapa
tiles.set_current_tilemap(tilemap("""nivel3"""))

# CONTROLES Y ANIMACIONES

def animar_abajo():
    animation.run_image_animation(jugador, assets.animation("""myAnim"""), 150, False)
controller.down.on_event(ControllerButtonEvent.PRESSED, animar_abajo)

def animar_derecha():
    animation.run_image_animation(jugador, assets.animation("""myAnim1"""), 150, False)
controller.right.on_event(ControllerButtonEvent.PRESSED, animar_derecha)

def animar_izquierda():
    animation.run_image_animation(jugador, assets.animation("""myAnim2"""), 150, False)
controller.left.on_event(ControllerButtonEvent.PRESSED, animar_izquierda)

def animar_arriba():
    animation.run_image_animation(jugador, assets.animation("""myAnim0"""), 150, False)
controller.up.on_event(ControllerButtonEvent.PRESSED, animar_arriba)

# ACCIÓN BOTÓN A
def interactuar():
    global mi_leña, arbol_cercano
    
    # 1. Si estás con el vecino, abrimos tienda
    if estoy_cerca_vecino:
        abrir_tienda()
        
    # 2. Si estás con un árbol, lo talamos
    elif estoy_cerca_arbol and arbol_cercano:
        if game.ask("¿Talar este árbol?"):
            arbol_cercano.destroy()
            mi_leña = mi_leña + 10
            game.splash("¡Ganaste 10 kg de leña!", "Tienes: " + str(mi_leña))

controller.A.on_event(ControllerButtonEvent.PRESSED, interactuar)

# BUCLE PRINCIPAL

def vigilar_entorno():
    global estoy_cerca_vecino, estoy_cerca_arbol, arbol_cercano
    
    # MEDIR DISTANCIA AL VECINO
    dist_x = jugador.x - vecino.x
    dist_y = jugador.y - vecino.y
    distancia_vecino = dist_x * dist_x + dist_y * dist_y
    
    if distancia_vecino < 1600:
        if not estoy_cerca_vecino:
            jugador.say_text("A: Comerciar", 500, False)
            estoy_cerca_vecino = True
        
        # Si hablas con el vecino, ignoras árboles
        estoy_cerca_arbol = False
        arbol_cercano = None
        
    else:
        estoy_cerca_vecino = False
        
        # BUSCAR ÁRBOLES CERCANOS
        todos_los_arboles = sprites.all_of_kind(SpriteKind.food)
        encontrado_uno = False
        
        for arbol in todos_los_arboles:
            dist_x_arbol = jugador.x - arbol.x
            dist_y_arbol = jugador.y - arbol.y
            distancia_arbol = dist_x_arbol * dist_x_arbol + dist_y_arbol * dist_y_arbol
            
            # Si estás cerca 
            if distancia_arbol < 900:
                arbol_cercano = arbol
                encontrado_uno = True
                
                if not estoy_cerca_arbol:
                    jugador.say_text("A: Talar", 500, False)
                    estoy_cerca_arbol = True
                break 
        
        # Si no hay ninguno cerca
        if not encontrado_uno:
            estoy_cerca_arbol = False
            arbol_cercano = None

# Activamos el bucle para que se repita siempre
game.on_update_interval(100, vigilar_entorno)