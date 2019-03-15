from user301_kOICjXGLxt_0 import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

########
# Side (RIGHT) view of character #
SIDE_WIDTH = 800 / 4
SIDE_HEIGHT = 600 / 3
SIDE_CENTER = [SIDE_WIDTH/2, SIDE_HEIGHT/2]
SIDE_SIZE = [SIDE_WIDTH, SIDE_HEIGHT]
SIDE_DIM = [4, 3]
side_image = simplegui.load_image("https://i.imgur.com/JnPVeWH.png")

# Side(LEFT) view of character#
LEFT_WIDTH = 800/4
LEFT_HEIGHT = 600/3
LEFT_CENTER = [LEFT_WIDTH/2, LEFT_HEIGHT/2]
LEFT_SIZE = [LEFT_WIDTH, LEFT_HEIGHT]
LEFT_DIM = [4,3]
left_image = simplegui.load_image("https://i.imgur.com/4cDBV2T.png")

# Back view of character #
BACK_WIDTH = 800/4
BACK_HEIGHT = 600/3
BACK_CENTER = [BACK_WIDTH/2, BACK_HEIGHT/2]
BACK_SIZE = [BACK_WIDTH, BACK_HEIGHT]
BACK_DIM = [4,3]
back_image = simplegui.load_image("https://i.imgur.com/jrnua27.png")

# Background image (Shilling ground floor) #
WIDTH = 768
HEIGHT = 768
image_center = (384, 384)
image_size = (750, 750)
pos = [384, 384]
image = simplegui.load_image("https://i.imgur.com/bFyXh2P.png")


#########
global back 
global left
back = False
def timer_handler():
    global counter
    global back
    global left
    if (back  == False and left == False):
        counter = (counter + 1) % (SIDE_DIM[0] * SIDE_DIM[1])
    if (back == True):
        counter = (counter + 1) % (BACK_DIM[0] * BACK_DIM[1])   
    if (left == True ):
        counter = (counter + 1) % (LEFT_DIM[0] * LEFT_DIM[1])
    
class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.colour = 'White'

    def draw(self, canvas):
        global back
        global counter
        global left
        
        if (back == False and left == False):
            side_index = [counter% SIDE_DIM[0], counter // SIDE_DIM[0]]
            canvas.draw_image(side_image, 
                             [SIDE_CENTER[0] + side_index[0] * SIDE_SIZE[0], 
                              SIDE_CENTER[1] + side_index[1] * SIDE_SIZE[1]], 
                              SIDE_SIZE, self.pos.getP(), SIDE_SIZE)
        if(back == True):
            back_index = [counter % BACK_DIM[0], counter // BACK_DIM[0]]
            canvas.draw_image(back_image, 
                            [BACK_CENTER[0] + back_index[0] * BACK_SIZE[0], 
                             BACK_CENTER[1] + back_index[1] * BACK_SIZE[1]], 
                             BACK_SIZE, self.pos.getP(), BACK_SIZE)
        if (left == True):
            left_index = [counter % LEFT_DIM[0], counter // LEFT_DIM[0]]
            canvas.draw_image(left_image,
                             [LEFT_CENTER[0] + left_index[0] * LEFT_SIZE[0],
                              LEFT_CENTER[1] + left_index[1] * LEFT_SIZE[1]],
                              LEFT_SIZE, self.pos.getP(), LEFT_SIZE)
            
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.15)
    
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['down']:
            self.down = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False
timerR = simplegui.create_timer(100, timer_handler)
timerU = simplegui.create_timer(50, timer_handler)
timerL = simplegui.create_timer(100, timer_handler)

class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        global back
        global left
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
            timerR.start()
        else:
            timerR.stop()
            
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))
            timerL.start()
            left = True
        else:
            timerL.stop()
            left = False
            
        if self.keyboard.up:
            self.wheel.vel.add(Vector(0,-1))
            timerU.start()
            back = True
        else:
            timerU.stop()
            back = False
            
        if self.keyboard.down:
            self.wheel.vel.add(Vector(0,1))

kbd = Keyboard()
wheel = Wheel(Vector(130,80), 40)
inter = Interaction(wheel, kbd)

def draw(canvas):
    canvas.draw_image(image, image_center, image_size, pos, image_size)
    inter.update()
    wheel.update()
    wheel.draw(canvas)

frame = simplegui.create_frame('GAME', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
counter = 0

frame.start()