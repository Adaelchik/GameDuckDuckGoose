namespace SpriteKind {
    export const spawn = SpriteKind.create()
    export const buton = SpriteKind.create()
    export const boom = SpriteKind.create()
    export const powerup = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite5: Sprite, otherSprite4: Sprite) {
    sprites.destroy(sprite5)
    statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite4).value += -20
    music.play(music.melodyPlayable(music.bigCrash), music.PlaybackMode.UntilDone)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.powerup, function on_on_overlap2(sprite4: Sprite, otherSprite3: Sprite) {
    
    spoppo = sprites.createProjectileFromSprite(assets.image`
        egg0
    `, mySprite, 50, 0)
    spoppo.setPosition(0, 0)
    spoppo.lifespan = 10000
    sprites.destroy(mySprite2)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    game.splash("pause ")
})
sprites.onOverlap(SpriteKind.boom, SpriteKind.Enemy, function on_on_overlap3(sprite3: Sprite, otherSprite2: Sprite) {
    sprites.destroy(sprite3)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(assets.image`
        egg
    `, mySprite, 50, 0)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
    if (spoppo && spoppo.lifespan > 0) {
        projectile.y += -5
        projectile = sprites.createProjectileFromSprite(assets.image`
            egg
        `, mySprite, 50, 0)
        projectile.y += 5
    }
    
})
function edath(enemy: Sprite) {
    
    sprites.destroy(enemy, effects.trail, 500)
    if (Math.percentChance(11)) {
        mySprite2 = sprites.create(assets.image`
            power up
        `, SpriteKind.powerup)
        mySprite2.x = enemy.x
        mySprite2.y = enemy.y
    }
    
}

sprites.onDestroyed(SpriteKind.Projectile, function on_on_destroyed(sprite2: Sprite) {
    
    splaty = sprites.create(assets.image`
        egg plod
    `, SpriteKind.boom)
    splaty.setPosition(sprite2.x, sprite2.y)
    splaty.lifespan = 500
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap4(sprite6: Sprite, otherSprite5: Sprite) {
    game.gameOver(false)
})
statusbars.onZero(StatusBarKind.EnemyHealth, function on_on_zero(status: StatusBarSprite) {
    edath(status.spriteAttachedTo())
})
let statusbar : StatusBarSprite = null
let goos : Sprite = null
let myEnemy = 0
let splaty : Sprite = null
let projectile : Sprite = null
let mySprite2 : Sprite = null
let spoppo : Sprite = null
let mySprite : Sprite = null
scene.setBackgroundImage(assets.image`
    proto back02
`)
mySprite = sprites.create(assets.image`
    duck
`, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
info.setScore(0)
let iAMSPEED = 10
mySprite.setStayInScreen(true)
game.splash("welcome to duck duck goose the GAME", "©2024")
game.onUpdateInterval(5000, function on_update_interval() {
    
    iAMSPEED += 10
    myEnemy = Math.min(iAMSPEED, 999999)
})
game.onUpdateInterval(2000, function on_update_interval2() {
    
    goos = sprites.create(assets.image`
        myImage
    `, SpriteKind.Enemy)
    goos.x = scene.screenWidth()
    goos.vx = 0 - iAMSPEED
    goos.y = randint(10, scene.screenHeight() - 10)
    statusbar = statusbars.create(15, 2, StatusBarKind.EnemyHealth)
    statusbar.attachToSprite(goos)
})
