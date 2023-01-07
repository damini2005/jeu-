def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

emptyobstacley = 0
bird: game.LedSprite = None
tickes = 0
obstacle: List[game.LedSprite] = []
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)

def on_forever():
    global emptyobstacley, tickes
    while len(obstacle) > 0 and obstacle[0].get(LedSpriteProperty.X) == 0:
        obstacle.remove_at(0).delete()
    for obstacle2 in obstacle:
        obstacle2.change(LedSpriteProperty.X, -1)
    if tickes % 3 == 0:
        emptyobstacley = randint(0, 4)
        for index in range(5):
            if index != emptyobstacley:
                obstacle.append(game.create_sprite(4, index))
    for obstacle3 in obstacle:
        if obstacle.get(LedSpriteProperty.X)== bird.get(LedSpriteProperty.X) and obstacle.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y)then 
         game.game_over()
    tickes += None
    basic.pause(1000)
basic.forever(on_forever)
