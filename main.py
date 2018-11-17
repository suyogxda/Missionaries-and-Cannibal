import pygame
import time
from pygame.locals import *
from random import randint
fps_count = 0
class character:
    def __init__(self, smiley, no):
        self.no = no
        self.on = 0
        self.board = None
        self.smiley = smiley
        if self.smiley is 0:
            self.y = 210
        else:
            self.y = 280
        if self.no is 1:
            self.x = 25
        if self.no is 2:
            self.x = 95
        if self.no is 3:
            self.x = 165
        
    def coord(self, obj):
        if obj.emo is 1:
            self.y = 280

    def draw(self, image):
        asd = screen.blit(image, (self.x, self.y))
        return asd


class boat:
    def __init__(self):
        self.count = 0
        self.left = None
        self.rite = None
        self.pstn = 0
        self.x = 250
        self.y = 320

    def put(self, emo):
        if self.pstn is 0:
            self.x = 250
            self.y = 320
            self.l = 0
            self.r = 0
            if self.count is 0:
                print(self.count)
                self.left = emo
                emo.board = 0
                self.count = 1
                emo.y = 280
                emo.x = 250
                emo.on = 2
                print(self.count)
                return 1
            elif self.count is 1:
                if emo.on is not 2:
                    print(self.left)
                    if self.left is None:
                        print(self.count)
                        self.left = emo
                        emo.board = 0
                        emo.y = 280
                        #emo.x = 900
                        emo.on = 2
                        self.count = 2      
                        print(self.count)  
                        return 1
                    else:
                        print(self.count)
                        self.rite = emo
                        emo.board = 1
                        self.count = 2
                        emo.y = 280
                        emo.on = 2
                        emo.x = 330
                        print(self.count)
                        return 1
                else:
                    if emo.no is 1:
                        if emo.board is 0:
                            emo.x = 25
                            self.left = None
                            emo.board = 0
                        if emo.board is 1:
                            emo.x = 25
                            self.rite = None
                            emo.board = 0
                    if emo.no is 2:
                        if emo.board is 0:
                            emo.x = 95
                            self.left = None
                            emo.board = 0
                        if emo.board is 1:
                            emo.x = 95
                            self.rite = None
                            emo.board = 0
                    if emo.no is 3:
                        if emo.board is 0:
                            emo.x = 165
                            self.left = None
                            emo.board = 0
                        if emo.board is 1:
                            emo.x = 165
                            self.rite = None
                            emo.board = 0
                    if emo.smiley is 0:
                        emo.y = 210
                    else:
                        emo.y = 280
                    emo.on = 0
                    self.count -= 1
            else:
                if emo.on is not 2:
                    print("Boat is full")
                    return 0
                else:
                    if emo.no is 1:
                        emo.x = 25
                    if emo.no is 2:
                        emo.x = 95
                    if emo.no is 3:
                        emo.x = 165
                    if emo.smiley is 0:
                        emo.y = 210
                    else:
                        emo.y = 280
                    emo.on = 0
                    self.count -= 1

        else:
            self.x = 620
            self.y = 320
            if self.count is 0:
                self.left = emo
                self.count = 1
                emo.y = 280
                emo.x = 250+370
                emo.on = 2
                return 1
            elif self.count is 1:
                if self.left is None:
                    self.left = emo
                    self.count = 2
                    emo.y = 280
                    emo.on = emo.x = 250+370
                    return 1
                else:
                    self.rite = emo
                    self.count = 2
                    emo.y = 280
                    emo.on = 2
                    return 1
            else:
                print("Boat is full")
                return 0

    def change_side(self):
        if self.count > 0:
            if self.pstn is 0:
                self.pstn = 1
                self.x = 620
                self.y = 320

            else:
                self.pstn = 0
                self.x = 250
                self.y = 320
        # if self.count > 0:
        #     if self.pstn is 0:
        #         self.pstn = 1
        #     else:
        #         self.pstn = 0
        # else:
        #     print("Boat is empty -_-")
    def draw(self):
        x = self.x
        y = self.y
        a1 = pygame.draw.polygon(screen, brown, [(x, y), (x+30, y+40), (x+100, y+40), (x+130, y)], 0) 
        pygame.draw.lines(screen, random, True, [(x, y), (x+30, y+40), (x+100, y+40), (x+130, y)], 3) 
        return a1

def background(a, b, c, d):
    pygame.draw.rect(screen, green, [0, 330, 250, sc_hieght])
    pygame.draw.lines(screen, random, True, [(0, 330), (250, 330)] , 3)
    pygame.draw.lines(screen, random, True, [(250, 330), (250, 350)] , 3)

    pygame.draw.rect(screen, green, [sc_width-250, 330, sc_width, sc_width])
    pygame.draw.lines(screen, random, True, [(sc_width-250, 330), (sc_width, 330)] , 3)
    pygame.draw.lines(screen, random, True, [(sc_width-250, 330), (sc_width-250, 350)] , 3)

    pygame.draw.rect(screen, green, [0, 350, sc_width, sc_hieght])

    pygame.draw.polygon(screen, blue, [(250, 350), (256, 439), (307, 525), (379, sc_hieght), (sc_width-379, sc_hieght),
     (sc_width-307, 525), (sc_width-256, 439), (sc_width-250, b), (sc_width-290, a), (sc_width-330, b),
     (sc_width-370, a), (sc_width-410, b), (sc_width-450, a), (sc_width-490, b),
     (490, a), (450, b), (410, a), (370, b), (330, a), (290, b), (250, a)
     ], 0)
    pygame.draw.polygon(screen, random, [(250, 350), (256, 439), (307, 525), (379, sc_hieght), (sc_width-379, sc_hieght),
     (sc_width-307, 525), (sc_width-256, 439), (sc_width-250, b), (sc_width-290, a), (sc_width-330, b),
     (sc_width-370, a), (sc_width-410, b), (sc_width-450, a), (sc_width-490, b),
     (490, a), (450, b), (410, a), (370, b), (330, a), (290, b), (250, a)
     ], 3)
    pygame.draw.lines(screen, random, False, [(c, 379), (c+30, 379) ], 3)
    pygame.draw.lines(screen, random, False, [(c+20, 419), (c+50, 419) ], 3)
    pygame.draw.lines(screen, random, False, [(c, 520), (c+30, 520) ], 3)
    pygame.draw.lines(screen, random, False, [(c, 479), (c+30, 479) ], 3)
    pygame.draw.lines(screen, random, False, [(d+30, 500), (d+70+30, 500) ], 3)
    pygame.draw.lines(screen, random, False, [(450, c), (550, c) ], 3)
    pygame.draw.lines(screen, random, False, [(470, 460), (540, 460) ], 3)
    pygame.draw.lines(screen, random, False, [(d-20, 400), (d-20+20, 400) ], 3)
    pygame.draw.lines(screen, random, False, [(d-40, 479), (d+30-40, 479) ], 3)
    pygame.draw.lines(screen, random, False, [(d-50, 516), (d+30-50, 516) ], 3)
    pygame.draw.lines(screen, random, False, [(d-90, 436), (d+30-90, 436) ], 3)
    a1 = pygame.draw.rect(screen, green, [450, 50, 100, 100])
    return a1

pygame.init()
clock = pygame.time.Clock()

miss = pygame.image.load('miss.png')
miss = pygame.transform.scale(miss, (50, 50))
devil = pygame.image.load('devil.png')
devil = pygame.transform.scale(devil, (50, 50))

miss1 = character(1, 1)
miss2 = character(1, 2)
miss3 = character(1, 3)

devil1 = character(0, 1)
devil2 = character(0, 2)
devil3 = character(0, 3)

sc_width = 1000
sc_hieght = 600
screen_size = [sc_width, sc_hieght]
red = (255, 0, 0)
blue = (135, 206, 235)
white = (255, 255, 255)
random = (0, 0, 0)
green = (0, 255, 0)
brown = (165,42,42)
screen = pygame.display.set_mode(screen_size)
caption = pygame.display.set_caption('Pie-Thon')
a = 340
b = 350
c = 400
d = 600
__boat = boat()
mpos = (0, 0)
while(1):
    Pressed = False
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            Pressed = True
    screen.fill(white)
    fps_count += 1
    clock.tick(30)
    __boat.draw()
    m1 = miss1.draw(miss)
    m2 = miss2.draw(miss)
    m3 = miss3.draw(miss)
    d1 = devil1.draw(devil)
    d2 = devil2.draw(devil)
    d3 = devil3.draw(devil)
    _boat_ = __boat.draw()
    if m1.collidepoint(mpos):
        __boat.put(miss1)
    if m2.collidepoint(mpos):
        __boat.put(miss2)
    if m3.collidepoint(mpos):
        __boat.put(miss3)

    if d1.collidepoint(mpos):
        __boat.put(devil1)
    if d2.collidepoint(mpos):
        __boat.put(devil2)
    if d3.collidepoint(mpos):
        __boat.put(devil3)

    if _boat_.collidepoint(mpos):
       __boat.change_side()
        
    if(fps_count == 10):
        a, b = b, a
        c, d = d, c
        fps_count = 0
    go = background(a, b, c, d)
    # if go.collidepoint(mpos):
    #     __boat.change_side()
    pygame.display.update()