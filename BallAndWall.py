from user301_kOICjXGLxt_0 import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
WIDTH = 600
HEIGHT = 400

class Wall:
    def __init__(self, x, border, color):
        self.x = x
        self.border = border
        self.color = color
        self.normal = Vector((1,0))
        self.edgeR = x + 1 + self.border
        self.edgeL = x - 1 - self.border

    def draw(self, canvas):
        canvas.draw_line((self.x, 0),
                         (self.x, HEIGHT),
                         self.border*2+1,
                         self.color)
   # def hit(self, ball):
    #    hR = (ball.offsetL() <= self.edgeR)
     #   hL = (ball.offsetR() >= self.edgeL)
      #  return hR and hL
    
class Wheel:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.radius = max(radius, 10)
        self.colour = 'White'

    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, self.colour, self.colour)
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False

class Interaction:
    def __init__(self, keyboard, wheel):
        self.walls = []
        self.wheel = wheel
        self.keyboard = keyboard
    
    def addWall(self, wall):
        self.walls.append(wall)
        
    def update(self):
        if self.keyboard.right:
            self.wheel.vel.add(Vector(1, 0))
        if self.keyboard.left:
            self.wheel.vel.add(Vector(-1, 0))

wheel = Wheel(Vector(WIDTH/2, HEIGHT-40), 20)

kbd = Keyboard()
i = Interaction(kbd, wheel)


w1 = Wall(100, 5, 'red')
i.addWall(w1)

w2 = Wall(500, 5, 'red')
i.addWall(w2)

def draw(canvas):
            i.update()
            w1.draw(canvas)
            w2.draw(canvas)
            wheel.update()
            wheel.draw(canvas)

frame = simplegui.create_frame("ball-wall", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
