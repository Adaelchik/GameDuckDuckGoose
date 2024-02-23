@namespace
class SpriteKind:
    spawn = SpriteKind.create()
    buton = SpriteKind.create()
    boom = SpriteKind.create()
    powerup = SpriteKind.create()

def on_on_overlap(sprite5, otherSprite4):
    sprites.destroy(sprite5)
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite4).value += -20
    music.play(music.melody_playable(music.big_crash),
        music.PlaybackMode.UNTIL_DONE)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite4, otherSprite3):
    global spoppo
    spoppo = sprites.create_projectile_from_sprite(assets.image("""
        egg0
    """), mySprite, 50, 0)
    spoppo.set_position(0, 0)
    spoppo.lifespan = 10000
    sprites.destroy(mySprite2)
sprites.on_overlap(SpriteKind.player, SpriteKind.powerup, on_on_overlap2)

def on_b_pressed():
    game.splash("pause ")
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap3(sprite3, otherSprite2):
    sprites.destroy(sprite3)
sprites.on_overlap(SpriteKind.boom, SpriteKind.enemy, on_on_overlap3)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        egg
    """), mySprite, 50, 0)
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    if spoppo and spoppo.lifespan > 0:
        projectile.y += -5
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            egg
        """), mySprite, 50, 0)
        projectile.y += 5
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def edath(enemy: Sprite):
    global mySprite2
    sprites.destroy(enemy, effects.trail, 500)
    if Math.percent_chance(11):
        mySprite2 = sprites.create(assets.image("""
            power up
        """), SpriteKind.powerup)
        mySprite2.x = enemy.x
        mySprite2.y = enemy.y

def on_on_destroyed(sprite2):
    global splaty
    splaty = sprites.create(assets.image("""
        egg plod
    """), SpriteKind.boom)
    splaty.set_position(sprite2.x, sprite2.y)
    splaty.lifespan = 500
sprites.on_destroyed(SpriteKind.projectile, on_on_destroyed)

def on_on_overlap4(sprite6, otherSprite5):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

def on_on_zero(status):
    edath(status.sprite_attached_to())
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

statusbar: StatusBarSprite = None
goos: Sprite = None
myEnemy = 0
splaty: Sprite = None
projectile: Sprite = None
mySprite2: Sprite = None
spoppo: Sprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    proto back02
"""))
mySprite = sprites.create(assets.image("""
    duck
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
info.set_score(0)
iAMSPEED = 10
mySprite.set_stay_in_screen(True)
game.splash("welcome to duck duck goose the GAME", "©2024")

def on_update_interval():
    global iAMSPEED, myEnemy
    iAMSPEED += 10
    myEnemy = min(iAMSPEED, 999999)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global goos, statusbar
    goos = sprites.create(assets.image("""
        myImage
    """), SpriteKind.enemy)
    goos.x = scene.screen_width()
    goos.vx = 0 - iAMSPEED
    goos.y = randint(10, scene.screen_height() - 10)
    statusbar = statusbars.create(15, 2, StatusBarKind.enemy_health)
    statusbar.attach_to_sprite(goos)
game.on_update_interval(2000, on_update_interval2)
