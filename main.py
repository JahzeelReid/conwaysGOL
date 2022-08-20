import math
import tkinter as tk
from tkinter import messagebox
import pygame
import sys


class gol(object):
    cells = []
    w = 500
    rows = 20

    def __init__(self, color):
        self.color = color

    def set(self, w, r):
        self.w = w
        self.rows = r

    def setting(self):
        return [self.w, self.rows]

    def addcell(self, x, y):
        self.cells.append([x, y])

    def printcell(self):
        return self.cells

    def killcell(self, x, y):
        self.cells.remove([x, y])

    def drawcells(self, surface):
        dis = self.w // self.rows
        for i in range(len(self.cells)):
            pygame.draw.rect(surface, (0, 255, 0), (self.cells[i][0] * dis + 1, self.cells[i][1] * dis + 1, dis - 2, dis
                                                    - 2))


def draw(w, rows, surface, data):
    btw = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + btw
        y = y + btw
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
    data.drawcells(surface)


def redraw(width, rows, surface, data):
    surface.fill((0, 0, 0))
    draw(width, rows, surface, data)
    pygame.display.update()


def find8(data, live, x, y):
    ring = [[], [], [], [], [], [], [], []]
    # ring[0] // topleft
    # ring[1] // top
    # ring[2] // topright
    # ring[3] // right
    # ring[4] // bottomright
    # ring[5] // bottom
    # ring[6] // bottomleft
    # ring[7] // left
    max = data.setting()[1] - 1
    rows = 20
    # topleft
    if x == 0 and y == 0:
        ring[0] = [max, max]
    elif x == 0:
        ring[0] = [max, y-1]
    elif y == 0:
        ring[0] = [x-1, max]
    else:
        ring[0] = [x-1, y-1]
    # top
    if y == 0:
        ring[1] = [x, max]
    else:
        ring[1] = [x, y-1]
    # topright
    if x == max and y == 0:
        ring[2] = [0,  max]
    elif x == max:
        ring[2] = [0, y-1]
    elif y == 0:
        ring[2] = [x+1, max]
    else:
        ring[2] = [x+1, y-1]
    # right
    if x == max:
        ring[3] = [0, y]
    else:
        ring[3] = [x+1, y]
    # bottomright
    if x == max and y == max:
        ring[4] = [0, 0]
    elif x == max:
        ring[4] = [0, y+1]
    elif y == max:
        ring[4] = [x+1, 0]
    else:
        ring[4] = [x+1, y+1]
    # bottom
    if y == max:
        ring[5] = [x, 0]
    else:
        ring[5] = [x, y+1]
    # bottomleft
    if x == 0 and y == max:
        ring[6] = [max, 0]
    elif x == 0:
        ring[6] = [max, y+1]
    elif y == max:
        ring[6] = [x-1, 0]
    else:
        ring[6] = [x - 1, y+1]
    # left
    if x == 0:
        ring[7] = [max, y]
    else:
        ring[7] = [x-1, y]

    life = 0
    for i in range(len(ring)):
        if ring[i] in live:
            life += 1
    # print(ring)
    return life


def deadoralive(data):
    copy = data.printcell()[:]
    # print(copy)
    for x in range(data.setting()[1]):
        for y in range(data.setting()[1]):

            # print([x, y])
            neigh = find8(data, copy, x, y)
            if [x, y] in copy:
                if neigh < 2:
                    data.killcell(x, y)
                elif neigh == 2 or neigh == 3:
                    pass
                elif neigh > 3:
                    data.killcell(x, y)
            else:
                if neigh == 3:

                    # print(data.printcell())
                    data.addcell(x, y)
                    # print(data.printcell())

    # print(data.printcell())
def glider(data, x, y):
    addlist = [[x, y], [x+1, y+1], [x+2, y+1], [x, y+2], [x+1, y+2]]
    for i in range(len(addlist)):
        data.addcell(addlist[i][0], addlist[i][1])



def startup(data, surface, width, rows):
    size = int(width/rows)
    flag = True
    glide = False
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and glide == False:
                px = event.pos[0]
                px = int(math.floor(px/size))
                py = event.pos[1]
                py = int(math.floor(py / size))
                if [px, py] in data.printcell():
                    data.killcell(px, py)
                else:
                    data.addcell(px, py)
                print(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN and glide == True:
                px = event.pos[0]
                px = int(math.floor(px / size))
                py = event.pos[1]
                py = int(math.floor(py / size))
                glider(data, px, py)
                glide = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("hit")
                    flag = False
                elif event.key == pygame.K_SPACE:
                    glide = True
        redraw(width, rows, surface, data)



def main():
    width = 500
    rows = 50
    surface = pygame.display.set_mode((width,width))
    flag = True
    clock = pygame.time.Clock()
    data = gol((255, 255, 255))
    data.set(width, rows)
    # data.addcell(19, 19)
    #data.addcell(0, 1)
    #data.addcell(1, 1)
    #data.addcell(2, 1)

    #data.addcell(4, 5)
    #data.addcell(4, 6)
    #data.addcell(4, 7)

    #data.addcell(30, 4)
    #data.addcell(30, 5)
    #data.addcell(30, 6)
    #print(find8(data.printcell(), 1, 0))
    startup(data, surface, width, rows)
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
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
        turn += 1
        print(turn)
        clock.tick(10)
        redraw(width, rows, surface, data)
        pygame.time.delay(100)
        if len(data.printcell()) == 0:
            break
        deadoralive(data)

main()


