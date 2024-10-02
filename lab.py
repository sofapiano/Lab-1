import time

def draw_line(offset=0, length=1, color=222):
    line = ' ' * length
    print(f'{" " * offset}\x1b[48;5;{color}m{line}\x1b[0m')


red = f"\x1b[48;5;{1}m{' ' * 3}\x1b[0m"
white = f"\x1b[48;5;{255}m{' ' * 3}\x1b[0m"
print(red * 5)
print(red * 2 + white + red * 2)
print(red + white * 3 + red)
print(red * 2 + white + red * 2)
print(red * 5)

'''if __name__ == '__main__':
    rhombus()'''