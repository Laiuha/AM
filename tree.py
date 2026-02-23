import random
import math

def draw_tree(x, y, angle, depth, canvas):
    if depth == 0:
        return
    
    length = depth * 2
    x2 = int(x + length * 0.5 * math.cos(angle))
    y2 = int(y - length * 0.5 * math.sin(angle))
    
    draw_line(x, y, x2, y2, canvas)
    
    # две ветки
    draw_tree(x2, y2, angle - random.uniform(0.2, 0.5), depth - 1, canvas)
    draw_tree(x2, y2, angle + random.uniform(0.2, 0.5), depth - 1, canvas)

def draw_line(x1, y1, x2, y2, canvas):
    steps = max(abs(x2-x1), abs(y2-y1))
    if steps == 0:
        return
        
    for i in range(steps + 1):
        x = int(x1 + (x2-x1)*i/steps)
        y = int(y1 + (y2-y1)*i/steps)
        if 0 <= y < len(canvas) and 0 <= x < len(canvas[0]):
            canvas[y][x] = "*"

width, height = 80, 30
canvas = [[" " for _ in range(width)] for _ in range(height)]

draw_tree(width//2, height-1, math.pi/2, 7, canvas)

for row in canvas:
    print("".join(row))
# test