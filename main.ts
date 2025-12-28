let nuevo_arbol: Sprite;
//       EL CONVERSOR RURAL - CÓDIGO FINAL
//  CONFIGURACIÓN Y PRECIOS
let LISTA_COSAS = ["gallina", "patata", "cabra", "huevos", "caballo", "Salir"]
let PRECIOS_LEÑA = [6, 1.33, 5, 0.25, 12, 0]
let mi_leña = 0
//  mochila de leña
//  Variables para saber qué está pasando
let estoy_cerca_vecino = false
let estoy_cerca_arbol = false
//  Definimos el tipo explícitamente para evitar errores
let arbol_cercano : Sprite = null
//  ACCIONES DEL JUEGO (FUNCIONES)
function calcular_leña_necesaria(cosa_que_quieres: string, cantidad: number): number {
    //  Buscamos el precio en la lista
    let precio_unitario = 0
    let encontrado = false
    let index = 0
    while (index < LISTA_COSAS.length) {
        if (LISTA_COSAS[index] == cosa_que_quieres) {
            precio_unitario = PRECIOS_LEÑA[index]
            encontrado = true
            break
        }
        
        index += 1
    }
    if (!encontrado) {
        game.splash("¡Esa cosa no existe!")
        return -1
    }
    
    //  Calculamos el total
    let total_leña = cantidad * precio_unitario
    //  Redondeamos a 2 decimales
    total_leña = Math.round(total_leña * 100) / 100
    return total_leña
}

function abrir_tienda() {
    let cuantos: number;
    let es_animal: any;
    let coste_total: number;
    
    //  Paramos al jugador para que no se mueva mientras compra
    controller.moveSprite(jugador, 0, 0)
    //  Creamos el texto del menú
    let texto_menu = ""
    let k = 0
    while (k < LISTA_COSAS.length) {
        texto_menu = texto_menu + LISTA_COSAS[k]
        if (k < LISTA_COSAS.length - 1) {
            texto_menu = texto_menu + ", "
        }
        
        k += 1
    }
    //  Preguntamos al jugador
    let eleccion = game.askForString("¿Qué quieres? (" + texto_menu + ")")
    if (eleccion) {
        if (eleccion == "Salir" || eleccion == "salir") {
            game.splash("¡Hasta luego!")
        } else {
            cuantos = game.askForNumber("¿Cuántas unidades de " + eleccion + "?")
            //  Regla de logica , los animales no se venden por trozos
            es_animal = eleccion == "gallina" || eleccion == "cabra" || eleccion == "caballo"
            if (es_animal && cuantos % 1 != 0) {
                game.splash("¡Error! Los animales deben", "estar vivos y enteros.")
            } else if (cuantos < 0) {
                game.splash("No puedes pedir negativos.")
            } else {
                //  Si todo está bien, calculamos
                coste_total = calcular_leña_necesaria(eleccion, cuantos)
                if (coste_total != -1) {
                    //  Mostramos la cuenta
                    game.splash("Cuesta " + ("" + coste_total) + " kg.", "Tienes: " + ("" + mi_leña) + " kg")
                    if (mi_leña >= coste_total) {
                        mi_leña = mi_leña - coste_total
                        game.splash("¡Trato hecho!", "Te sobran " + ("" + mi_leña) + " kg.")
                    } else {
                        game.splash("Te falta leña para pagar.")
                    }
                    
                }
                
            }
            
        }
        
    }
    
    //  Devolvemos el control al jugador
    controller.moveSprite(jugador, 80, 80)
}

//  PREPARACIÓN DEL MUNDO
//  Crear al Jugador
let jugador = sprites.create(assets.image`nena-front`, SpriteKind.Player)
jugador.setPosition(130, 155)
jugador.z = 10
scene.cameraFollowSprite(jugador)
controller.moveSprite(jugador, 80, 80)
//  Crear al Vecino
let vecino = sprites.create(img`
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
`, SpriteKind.Player)
vecino.setPosition(140, 140)
//  Crear el Mercado
let decorado_mercado = sprites.create(img`
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
`, SpriteKind.Player)
decorado_mercado.setPosition(130, 115)
//  PLANTAR ÁRBOLES
//  imagen arbol
let imagen_arbol = assets.image`forestTree0`
//  posion de los arboles
let posiciones_arboles = [[20, 20], [50, 20], [20, 50], [40, 40], [235, 20], [205, 20], [235, 50], [215, 40], [20, 235], [50, 235], [20, 205], [40, 215], [235, 235], [205, 235], [235, 205], [215, 215]]
//  for para plantarlos
for (let pos of posiciones_arboles) {
    nuevo_arbol = sprites.create(imagen_arbol, SpriteKind.Food)
    nuevo_arbol.setPosition(pos[0], pos[1])
}
//  Cargar Mapa
tiles.setCurrentTilemap(tilemap`nivel3`)
//  CONTROLES Y ANIMACIONES
controller.down.onEvent(ControllerButtonEvent.Pressed, function animar_abajo() {
    animation.runImageAnimation(jugador, assets.animation`myAnim`, 150, false)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function animar_derecha() {
    animation.runImageAnimation(jugador, assets.animation`myAnim1`, 150, false)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function animar_izquierda() {
    animation.runImageAnimation(jugador, assets.animation`myAnim2`, 150, false)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function animar_arriba() {
    animation.runImageAnimation(jugador, assets.animation`myAnim0`, 150, false)
})
//  ACCIÓN BOTÓN A
controller.A.onEvent(ControllerButtonEvent.Pressed, function interactuar() {
    
    //  1. Si estás con el vecino, abrimos tienda
    if (estoy_cerca_vecino) {
        abrir_tienda()
    } else if (estoy_cerca_arbol && arbol_cercano) {
        //  2. Si estás con un árbol, lo talamos
        if (game.ask("¿Talar este árbol?")) {
            arbol_cercano.destroy()
            mi_leña = mi_leña + 10
            game.splash("¡Ganaste 10 kg de leña!", "Tienes: " + ("" + mi_leña))
        }
        
    }
    
})
//  BUCLE PRINCIPAL
//  Activamos el bucle para que se repita siempre
game.onUpdateInterval(100, function vigilar_entorno() {
    let todos_los_arboles: Sprite[];
    let encontrado_uno: boolean;
    let dist_x_arbol: number;
    let dist_y_arbol: number;
    let distancia_arbol: any;
    
    //  MEDIR DISTANCIA AL VECINO
    let dist_x = jugador.x - vecino.x
    let dist_y = jugador.y - vecino.y
    let distancia_vecino = dist_x * dist_x + dist_y * dist_y
    if (distancia_vecino < 1600) {
        if (!estoy_cerca_vecino) {
            jugador.sayText("A: Comerciar", 500, false)
            estoy_cerca_vecino = true
        }
        
        //  Si hablas con el vecino, ignoras árboles
        estoy_cerca_arbol = false
        arbol_cercano = null
    } else {
        estoy_cerca_vecino = false
        //  BUSCAR ÁRBOLES CERCANOS
        todos_los_arboles = sprites.allOfKind(SpriteKind.Food)
        encontrado_uno = false
        for (let arbol of todos_los_arboles) {
            dist_x_arbol = jugador.x - arbol.x
            dist_y_arbol = jugador.y - arbol.y
            distancia_arbol = dist_x_arbol * dist_x_arbol + dist_y_arbol * dist_y_arbol
            //  Si estás cerca 
            if (distancia_arbol < 900) {
                arbol_cercano = arbol
                encontrado_uno = true
                if (!estoy_cerca_arbol) {
                    jugador.sayText("A: Talar", 500, false)
                    estoy_cerca_arbol = true
                }
                
                break
            }
            
        }
        //  Si no hay ninguno cerca
        if (!encontrado_uno) {
            estoy_cerca_arbol = false
            arbol_cercano = null
        }
        
    }
    
})
