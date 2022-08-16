import math
import tkinter as tk
from tkinter import messagebox
import pygame

class gol(object):
    cells = []
    w = 500
    rows = 20

    def __init__(self, color):
        self.color = color
    def addcell(self, x, y):
        self.cells.append([x, y])
    def printcell(self):
        return self.cells
    def killcell(self, x, y):
        self.cells.remove([x, y])
    def drawcells(self, surface):
        dis = self.w // self.rows
        for i in range(len(self.cells)):
            pygame.draw.rect(surface, (0, 255, 0), (self.cells[i][0] * dis + 1, self.cells[i][1] * dis + 1, dis - 2, dis - 2))

class cell(object):
    rows = 20
    w = 500
    color = (0, 255, 0)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, surface):
        dis = self.w // self.rows
        pygame.draw.rect(surface, self.color, (self.x*dis+1, self.y*dis+1, dis-2, dis-2))


def create(w, ):
    #a =
    #for i in range(w):

    return 1

def draw(w, rows, surface,data):
    btw = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + btw
        y = y + btw
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
    data.drawcells(surface)

def redraw(w, rows, surface, data):
    surface.fill((0,0,0))
    draw(w, rows, surface, data)
    pygame.display.update()


def find8(live, x, y):
    ring = [[],[],[],[],[],[],[],[]]
    cols = 20
    rows = 20
    #topleft
    if x == 0 and y == 0:
        ring[0] = [19,19]
    elif x == 0:
        ring[0] = [19, y-1]
    elif y == 0:
        ring[0] = [x-1, 19]
    else:
        ring[0] = [x-1, y-1]
    #top
    if y == 0:
        ring[1] = [x, 19]
    else:
        ring[1] = [x, y-1]
    #topright
    if x == 19 and y == 0:
        ring[2] = [0,  19]
    elif x == 19:
        ring[2] = [0, y-1]
    elif y == 0:
        ring[2] = [x+1, 19]
    else:
        ring[2] = [x+1, y-1]
    #right
    if x == 19:
        ring[3] = [0, y]
    else:
        ring[3] = [x+1, y]
    #bottomright
    if x == 19 and y == 19:
        ring[4] = [0, 0]
    elif x == 19:
        ring[4] = [0, y+1]
    elif y == 19:
        ring[4] = [x+1, 0]
    else:
        ring[4] = [x+1, y+1]
    #bottom
    if y == 19:
        ring[5] = [x, 0]
    else:
        ring[5] = [x, y+1]
    #bottomleft
    if x == 0 and y == 19:
        ring[6] = [19, 0]
    elif x == 0:
        ring[6] = [19, y+1]
    elif y == 19:
        ring[6] = [x-1, 0]
    else:
        ring[6] = [x - 1, y+1]
    #left
    if x == 0:
        ring[7] = [19, y]
    else:
        ring[7] = [x-1, y]

    life = 0
    for i in range(len(ring)):
        if ring[i] in live:
            life += 1
    #print(ring)
    return life

def deadoralive(data):
    copy = data.printcell()[:]
    #print(copy)
    for x in range(20):
        for y in range(20):

            #print([x, y])
            neigh = find8(copy, x, y)
            if [x, y] in copy:
                if neigh < 2:
                    data.killcell(x, y)
                elif neigh == 2 or neigh == 3:
                    pass
                elif neigh > 3:
                    data.killcell(x, y)
            else:
                if neigh == 3:

                    #print(data.printcell())
                    data.addcell(x, y)
                    #print(data.printcell())

    #print(data.printcell())





def main():
    width = 500
    rows = 20
    surface = pygame.display.set_mode((width,width))
    flag = True
    clock = pygame.time.Clock()
    data = gol((255, 255, 255))
    #data.addcell(19, 19)
    data.addcell(0, 1)
    data.addcell(1, 1)
    data.addcell(2, 1)

    data.addcell(4, 5)
    data.addcell(4, 6)
    data.addcell(4, 7)

    data.addcell(5, 4)
    data.addcell(5, 5)
    data.addcell(5, 6)
    #print(find8(data.printcell(), 1, 0))

    #data.addcell(19, 0)
    ##data.addcell(19, 1)
    #data.addcell(0, 19)
    #data.addcell(0, 1)
    #data.addcell(1, 19)
    #data.addcell(1, 0)
    #print(data.printcell())
    #deadoralive(data)
    #print(find8(data, 0, 0))


    turn = 0
    while flag:
        turn += 1
        print(turn)
        clock.tick(10)
        redraw(width, rows, surface, data)
        pygame.time.delay(300)
        if len(data.printcell()) == 0 or turn == 150:
            break
        deadoralive(data)

main()


