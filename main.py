# --- CÓDIGO INICIAL DEL USUARIO A CONTINUACIÓN ---
# ANIMACIONES

def on_down_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim
        """), 150, False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_right_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim1
        """), 150, False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim2
        """), 150, False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

# Manejador del botón A: solo llama al menú si está cerca del mercado

def on_a_pressed():
    if cerca_del_mercado:
        menu_intercambio()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_up_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim0
        """), 150, False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

# --- FUNCIONES DE LÓGICA DE NEGOCIO ---
def calcular_lena_necesaria(producto_str: str, cantidad: number):
    global tasa, encontrado, i, total_lena
    if cantidad <= 0:
        game.splash("La cantidad debe ser mayor a cero.")
        return -1
    while i <= len(PRODUCTOS) - 1:
        if PRODUCTOS[i] == producto_str:
            tasa = TASAS_VALORES[i]
            encontrado = True
            break
        i += 1
    if not (encontrado):
        game.splash("Producto no válido.")
        return -1
    if ["gallina", "cabra", "caballo", "patata", "huevos"].index_of(producto_str) >= 0:
        pass
    total_lena = cantidad * tasa
    return total_lena
def menu_intercambio():
    global opciones_str, j, mensaje_pregunta_1, eleccion_str, mensaje_pregunta_2, cantidad2, resultado, mensaje_resultado
    controller.move_sprite(noi, 0, 0)
    while j <= len(PRODUCTOS) - 1:
        opciones_str = "" + opciones_str + PRODUCTOS[j]
        if j < len(PRODUCTOS) - 1:
            opciones_str = "" + opciones_str + ", "
        j += 1
    mensaje_pregunta_1 = "¿Qué quieres? (" + opciones_str + ")"
    # Si el usuario pulsa B aquí, sale de la función automáticamente
    eleccion_str = game.ask_for_string(mensaje_pregunta_1)
    if eleccion_str:
        mensaje_pregunta_2 = "¿Cuántas unidades de " + eleccion_str + "?"
        cantidad2 = game.ask_for_number(mensaje_pregunta_2)
        resultado = calcular_lena_necesaria(eleccion_str, cantidad2)
        if resultado != -1:
            mensaje_resultado = "Necesitas " + ("" + str(resultado)) + " kg de leña de pino."
            game.splash(mensaje_resultado)
    game.splash("¡Gracias por comerciar!")
    # Reactiva el movimiento del jugador al salir del menú
    controller.move_sprite(noi, 80, 80)
distancia_cuadrada = 0
dy = 0
dx = 0
mensaje_resultado = ""
resultado = 0
cantidad2 = 0
mensaje_pregunta_2 = ""
eleccion_str = ""
mensaje_pregunta_1 = ""
opciones_str = ""
j = 0
total_lena = 0
encontrado = False
tasa = 0
i = 0
cerca_del_mercado = False
noi: Sprite = None
TASAS_VALORES: List[number] = []
PRODUCTOS: List[str] = []
# --- DEFINICIÓN DE TASAS DE CONVERSIÓN ---
PRODUCTOS = ["gallina", "patata", "cabra", "huevos", "caballo"]
TASAS_VALORES = [6, 1.33, 5, 3, 12]
# CREAR PERSONAJES y OBJETO
noi = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
mercado = sprites.create(img("""
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
        ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee46c..
        ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
        ....644444444c66f4e44e44e44e44ee66c444444446....
        .....64eee444c66f4e44e44e44e44ee66c444eee46.....
        ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
        """),
    SpriteKind.player)
# POSICIÓN DE LOS OBJETOS
noi.set_position(130, 155)
mercado.set_position(130, 115)
noi.z = 10
# CARGAR EL TILEMAP (EL BOSQUE)
tiles.set_current_tilemap(tilemap("""
    nivel3
    """))
# LA CÁMARA SIGUE AL PERSONAJE
scene.camera_follow_sprite(noi)
# MOVIMIENTO SOLO HORIZONTAL
controller.move_sprite(noi, 80, 80)
# --- MANEJADORES DE EVENTOS ---

def on_update_interval():
    global dx, dy, distancia_cuadrada, cerca_del_mercado
    dx = noi.x - mercado.x
    dy = noi.y - mercado.y
    distancia_cuadrada = dx * dx + dy * dy
    if distancia_cuadrada < 40 * 40:
        # Usamos un radio de 40 píxeles
        if not (cerca_del_mercado):
            game.splash("¡Pulsa A para comerciar!",
                "Al presionar luego seguidamente vuelvelo a presionar")
            cerca_del_mercado = True
    else:
        cerca_del_mercado = False
game.on_update_interval(100, on_update_interval)
