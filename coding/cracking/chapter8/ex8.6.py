
import copy

sizex = 4
sizey = 4

screen = []

for x in range(sizex):
    tmp = []
    for y in range(sizey):
        if x < sizex//2:
            tmp.append(1)
        else:
            tmp.append(0)
    screen.append(tmp)

def fill(screen, x, y, ocolor, ncolor):
    if y < 0 or y == len(screen[0]) or\
        x < 0 or x == len(screen):
        return

    if screen[x][y] == ocolor:
        screen[x][y] = ncolor
        fill(screen, x+1, y, ocolor, ncolor)
        fill(screen, x-1, y, ocolor, ncolor)
        fill(screen, x, y+1, ocolor, ncolor)
        fill(screen, x, y-1, ocolor, ncolor)

print(screen)
fill(screen, 0, 1, 1, 2)
print(screen)
