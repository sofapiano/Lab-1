import time
import os

def draw_line_c(offset=0, color=222):
    print(f'{"   " * offset}\x1b[48;5;{color}m{"   "}\x1b[0m'
          f'{"   " * (4-offset*2)}\x1b[48;5;{color}m{"   "}\x1b[0m'
          f'{"   " * offset}' * 2)

def draw_line(offset=0, color=222, length=1):
    line = '   ' * length
    print(f'{"   " * offset}\x1b[48;5;{color}m{line}\x1b[0m')

def circles():
    height = 6
    center, offset = height//2-1, 2
    step = 1
    color = 255
    for line in range(height-1):
        draw_line_c(offset, color)
        if line == center:
            draw_line_c(offset, color)
            offset += step
        elif line < center:
            offset -= step
        else:
            offset += step
    

def country_flag(color):
    red = f"\x1b[48;5;{color}m{' ' * 3}\x1b[0m"
    white = f"\x1b[48;5;{255}m{' ' * 3}\x1b[0m"
    print(red * 5)
    print(red * 2 + white + red * 2)
    print(red + white * 3 + red)
    print(red * 2 + white + red * 2)
    print(red * 5)
    print()


if __name__ == '__main__':
    #страна
    country_flag(1)
    print()

    #узор
    circles()
    print()

    #график
    print('если принять 6 клеточек (1 клеточка = 3 пробела в ширину) за единицу:')
    for i in range(9):
        draw_line(9*3-i*3, 1, 3)

    #диаграмма
    with open("sequence.txt") as data:
        data = [float(num) for num in data.readlines()]
        yes = 0
        for num in data:
            if -3 <= num <= 3:
                yes += 1
        print("yes", yes)
        line, line_n = " " * (yes//2), " " * ((len(data)-yes)//2)
        print(f'\x1b[48;5;{1}m{line}\x1b[0m')
        print("no", len(data) - yes)
        print(f'\x1b[48;5;{1}m{line_n}\x1b[0m')
    #почему-то диаграмма отображается, только если поставить брейкпоинты на 62, 63 и 
    # 65 строки и запустить дебаггер. хз считается ли это за норм ответ, но что есть то есть

    for i in range(9):
        print()

    #анимация
    colors = [1, 4, 5]
    while True:
        for color in colors:
            country_flag(color)
            time.sleep(2)
            os.system("cls")
