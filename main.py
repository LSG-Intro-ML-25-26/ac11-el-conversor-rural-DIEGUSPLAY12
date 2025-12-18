def on_down_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim
        """), 150, True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

# ANIMACIONES

def on_right_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim1
        """), 150, True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim2
        """), 150, True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_up_pressed():
    animation.run_image_animation(noi, assets.animation("""
        myAnim0
        """), 150, True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

noi: Sprite = None
# CREAR PERSONAJE
noi = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
# POSICIÓN INICIAL
noi.set_position(77, 57)
# CARGAR EL TILEMAP (EL BOSQUE)
tiles.set_current_tilemap(tilemap("""
    nivel3
    """))
# LA CÁMARA SIGUE AL PERSONAJE
scene.camera_follow_sprite(noi)
# MOVIMIENTO SOLO HORIZONTAL
controller.move_sprite(noi, 80, 0)
# MANTENER AL PERSONAJE EN EL SUELO

def on_on_update():
    if noi.y < 20:
        noi.y = 20
game.on_update(on_on_update)
