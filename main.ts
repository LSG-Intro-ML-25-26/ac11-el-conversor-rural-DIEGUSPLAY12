controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    noi,
    assets.animation`myAnim`,
    150,
    true
    )
})
// ANIMACIONES
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    noi,
    assets.animation`myAnim1`,
    150,
    true
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    noi,
    assets.animation`myAnim2`,
    150,
    true
    )
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    noi,
    assets.animation`myAnim0`,
    150,
    true
    )
})
let noi: Sprite = null
// CREAR PERSONAJE
noi = sprites.create(assets.image`nena-front`, SpriteKind.Player)
// POSICIÓN INICIAL
noi.setPosition(77, 57)
// CARGAR EL TILEMAP (EL BOSQUE)
tiles.setCurrentTilemap(tilemap`nivel3`)
// LA CÁMARA SIGUE AL PERSONAJE
scene.cameraFollowSprite(noi)
// MOVIMIENTO SOLO HORIZONTAL
controller.moveSprite(noi, 80, 80)
