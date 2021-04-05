play_field = [[" "] * 3 for x in range(0, 3)]
# print(play_field)


# Функция вывода игрового поля на экран
def show_play_field():
    print(f'    0 1 2')
    print("   ------")
    for i in range(3):
        print(f'{i} | {play_field[i][0]} {play_field[i][1]} {play_field[i][2]}')

# show_play_field()

# Проверяем победителя
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(play_field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            show_play_field()
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            show_play_field()
            return True
    return False

# Функция ввода координат точки
def user_data_request():
    while True:
        user_coord = input(" \nВведите координаты точки в диапазоне цифр от 0 до 2:  ").split()
        if len(user_coord) != 2:
            print("Введите две координаты точки!")
            continue
        x, y = user_coord
        if not(x.isdigit()) or not(y.isdigit()):
            print("Вводимые значения должны быть цифрами!")
            continue
        x = int(x)
        y = int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты выходят за допустимый диапазон")
            continue
        if play_field[x][y] != " ":
            print(" Это поле уже занято! ")
            continue
        return x, y


# user_data_request()

def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

greet()
step_counter = 0
while True:
    step_counter += 1
    show_play_field()

    if step_counter % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = user_data_request()

    if step_counter % 2 == 1:
        play_field[x][y] = "X"
    else:
        play_field[x][y] = "Y"

    if check_win():
        break
    if step_counter == 9:
        show_play_field()
        print("Победила дружба!")
        break





