import time

def draw_line(offset=0, length=1, color=222):
    line = ' ' * length
    print(f'{" " * offset}\x1b[48;5;{color}m{line}\x1b[0m')

def rhombus():
    height = 15
    center = height//2
    offset = height//2
    step = 1
    length = 1
    colors = [222, 157]
    print(height, center, offset)
    while True:
        for color in colors:
            for line in range(height):
                draw_line(offset, length, color)
                if line < center:
                    offset -= step
                    length += step * 2
                else:
                    offset += step
                    length -= step*2
            print(f'\x1b[{height+2}A')
            print(f'\x1b[{offset}D')
            length = 1
            offset = height//2
            time.sleep(2)
        

if __name__ == '__main__':
    rhombus()