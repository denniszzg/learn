import pygame as g, sys, random, time
g.init()
screen = g.display.set_mode([640,480])
screen.fill([255,255,255])


top = 10
left = 10
x = 1
y = 1

for i in range(1000):
    '''
    r = random.randint(0, 250)
    r = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0 ,500)
    
    
    '''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    r = random.randint(1,40)
    g.draw.circle(screen, [red, green, blue], [left, top], r, 0)
    g.display.flip()
    time.sleep(0.01)
    
    #r -= 5
    #r -= 5

    if top >= 480 - r and x == 1 and y == 1: #↘触底
        top -= 5
        left += 5
        y = -1
    elif top >= 480 - r and x == -1 and y == 1: #↙触底
        top -= 5
        left -= 5
        y = -1
    
    elif left >= 640 - r and x == 1 and y == 1: #↘触右
        left -= 5
        top += 5
        x = -1
    elif left >= 640 - r and x == 1 and y == -1: #↗触右
        left -= 5
        top -=5
        x = -1
        
    elif top <= 0 and x == 1 and y == -1: #↗触顶
        left += 5
        top -= 5
        y = 1
    elif top <= 0 and x == -1 and y == -1: #↖触顶
        left -= 5
        top +=5
        y = 1

    elif left <= 0 and x == -1 and y == -1: #↖触左
        left += 5
        top -= 5
        x = 1
    elif left <= 0 and x == -1 and y == 1: #↙触左
        left += 5
        top +=5
        x = 1
        
    else:
        left += x * 5
        top += y * 5
        

#g.display.flip()
while True:
    
    for event in g.event.get():
        if event.type == g.QUIT: sys.exit()