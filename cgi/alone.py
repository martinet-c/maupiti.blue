#!/usr/bin/python3
import util
util.header()

w, h = 80, 20
matrix = [[0 for x in range(w)] for y in range(h)] 
for y in range(h):
    for x in range(w):
        matrix[y][x] = ' '

from random import randint
nb = 100
coord = []
coord.append([int(w/2), int(h/2)-1])
for i in range(nb):
    coord.append([randint(0, w-1), randint(-2, h-1)])
coord.sort(key=lambda x: x[1]) # sort on column 1, see https://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column

for i in range(len(coord)):
    x = coord[i][0]
    y = coord[i][1]
    if y>-1 and y<h:
        matrix[y][x]   = '@'
    if y+1>-1 and y+1<h:
        matrix[y+1][x] = '▓'
    if y+2>-1 and y+2<h:
        matrix[y+2][x] = '║'

print('```')
for y in range(h):
    print(''.join(matrix[y]))
print('```')

util.footer_en()