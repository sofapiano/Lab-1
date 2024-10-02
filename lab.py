import time

def draw_line_с(offset=0, color=222):
    print(f'{"   " * offset}\x1b[48;5;{color}m{"   "}\x1b[0m{"   " * (4-offset*2)}\x1b[48;5;{color}m{"   "}\x1b[0m{"   " * offset}' * 2)

def draw_line(offset=0, color=222, length=1):
    line = '   ' * length
    print(f'{"   " * offset}\x1b[48;5;{color}m{line}\x1b[0m')

def circles():
    height = 6
    center, offset = height//2-1, 2
    step = 1
    color = 255
    for line in range(height-1):
        draw_line_с(offset, color)
        if line == center:
            draw_line_с(offset, color)
            offset += step
        elif line < center:
            offset -= step
        else:
            offset += step


#страна
red = f"\x1b[48;5;{1}m{' ' * 3}\x1b[0m"
white = f"\x1b[48;5;{255}m{' ' * 3}\x1b[0m"
print(red * 5)
print(red * 2 + white + red * 2)
print(red + white * 3 + red)
print(red * 2 + white + red * 2)
print(red * 5)

#узор
if __name__ == '__main__':
    circles()

print('если принять 6 клеточек (1 клеточка = 3 пробела в ширину) за единицу:')
for i in range(9):
    draw_line(9*3-i*3, 1, 3)