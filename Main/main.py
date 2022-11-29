from math import pi


def to_print(board: list, symbol: str):
    'Функция цветного вывода на экран'

    size = int(len(board) ** 0.5)

    a = list(range(size))

    print('\033[{1}m\033[{0}m    '.format(default_font_color, default_background_color), end='')
    for i in a:
        print('\033[{1}m\033[{0}m '.format(default_font_color, default_background_color) *
              (2 - len(str(i))) + str(i), end=' ')
    print('\n')

    for i in range(size):
        print('\033[{0}m\033[{1}m '.format(default_font_color, default_background_color) *
              (2 - len(str(i))) + str(i), end='   ')

        k = board[i * size: (i + 1) * size]

        for j in k:
            if j == symbol[0]:
                print('\033[{1}m\033[{0}m{2}  '.format(default_font_color, default_background_color, j), end='')
            else:
                print('\033[{1}m\033[{0}m{2}  '.format(font_color, background_color, j), end='')

        print()


def check_input(x: list, size: int):
    'Функция проверки введенных значений'

    s = 'На вход подаются числа от (0) до (размер поля - 1)'

    for i in x:
        if not isinstance(i, int):
            raise Error(s)
        elif i >= size or i < 0:
            raise Error(s)


class Error(Exception):
    pass


class Canvas():
    'Класс для рисования фигур на общем экране'

    def __init__(self, default_symbol: str = '-', size: int = 40):
        self.size = size
        self.default_symbol = default_symbol
        self.Board = [default_symbol] * size * size

    def _check_values(self, *args):
        x, y = [], []

        if len(args) == 0:
            raise Error('У фигуры нет собственных точек')
        else:
            x = list(args)[::2]
            y = list(args)[1::2]

            if len(x) != len(y):
                raise Error('У точки не хватает аргумента x или y')

            check_input(x, self.size)
            check_input(y, self.size)

        return x, y

    def draw_dot(self, symbol: str = '', *args):
        'Функция рисования в точке(ах) на общем экране'

        if symbol == '':
            symbol = self.default_symbol

        x, y = self._check_values(*args)

        for i in range(len(x)):
            self.Board[x[i] + y[i] * self.size] = symbol[0]

    def fill(self, symbol: str = ''):
        'Функция заполнения общего экрана символами'

        if symbol == '':
            symbol = self.default_symbol

        self.Board = [symbol[0]] * self.size * self.size

    def get_dot(self, x: int = 0, y: int = 0):
        'Функция получения значения в точке'

        return self.Board[x + y * self.size]

    def print(self):
        'Функция вывода общего экрана в консоль'

        a = list(range(self.size))

        print('    ', end='')
        for i in a:
            print(' ' * (2 - len(str(i))) + str(i), end=' ')
        print('\n')

        for i in range(self.size):
            print(' ' * (2 - len(str(i))) + str(i) + '  ', '  '.join(self.Board[i * self.size: (i + 1) * self.size]))

    def print_c(self, symbol: str = ''):
        'Функция цветного вывода общего экрана в консоль'

        if symbol == '':
            symbol = self.default_symbol

        to_print(self.Board, symbol[0])

    def mirror_h(self):
        'Функция отражения экрана по горизонтали'

        for i in range(self.size):
            a = self.Board[i * self.size: (i + 1) * self.size]
            a = a[::-1]

            self.Board = self.Board[: i * self.size] + a + self.Board[(i + 1) * self.size:]

    def mirror_v(self):
        'Функция отражения экрана по вертикали'

        for i in range(self.size):
            a = self.Board[i::self.size]
            a = a[::-1]

            for j in range(self.size):
                self.Board[i + j * self.size] = a[j]

    def move_to(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0, x: int = 0, y: int = 0, copy: bool = False):
        'Функция перемещения(копирования) области'

        check_input([x1, x2, x], self.size)
        check_input([y1, y2, y], self.size)

        check_input([x + abs(x1 - x2)], self.size)
        check_input([y + abs(y1 - y2)], self.size)

        a = []
        for i in range(min(y1, y2), max(y1, y2) + 1):
            a.append(self.Board[min(x1, x2) + i * self.size: max(x1, x2) + 1 + i * self.size])

            if not copy:
                self.Board = self.Board[: min(x1, x2) + i * self.size] + \
                             [self.default_symbol] * (abs(x1 - x2) + 1) + self.Board[max(x1, x2) + 1 + i * self.size:]

        for i in range(y, y + abs(y1 - y2) + 1):
            self.Board = self.Board[: x + i * self.size] + a[0] + self.Board[x + abs(x1 - x2) + 1 + i * self.size:]
            del a[0]


class Dot():
    'Класс точки'

    def __init__(self, x: int = 0, y: int = 0):
        self.size = canvas.size
        self.default_symbol = canvas.default_symbol
        self.Board = [self.default_symbol] * self.size * self.size

        self.__x, self.__y = self._check_values(x, y)

    def _check_values(self, *args):
        x = [0]
        y = [0]

        if len(args) == 0:
            try:
                x = self.x
                y = self.y
            except:
                raise Error('У фигуры нет собственных точек. Укажите входные данные')
        else:
            x = list(args)[::2]
            y = list(args)[1::2]

            if len(x) != len(y):
                raise Error('У точки не хватает аргумента x или y')

            check_input(x, self.size)
            check_input(y, self.size)

        return x, y

    def _set_dots(self, x: list, y: list):
        dots = []
        for i in range(len(x)):
            dots.append(x[i])
            dots.append(y[i])

        return dots

    def _set_fill_dots(self, x: list, y: list):
        dots = self._set_dots(x, y)
        x = []
        y = []
        for i in range(0, len(dots), 2):
            x.append(dots[i])
            y.append(dots[i + 1])

        dots = []

        for i in range(len(y)):
            for j in range(len(y)):
                if y[i] == y[j]:
                    for k in range(min(x[i], x[j]) + 1, max(x[i], x[j])):
                        dots.append(k)
                        dots.append(y[i])

        return dots

    def draw(self, symbol: str = '', *args):
        'Функция рисования фигуры на локальном экране. \
                Если нужна обычная функция рисования точек, используйте функцию "draw_dot"'

        if symbol == '':
            symbol = self.default_symbol

        x, y = self._check_values(*args)

        dots = self._set_dots(x, y)

        for i in range(1, len(dots), 2):
            self.Board[dots[i - 1] + dots[i] * self.size] = symbol[0]

    def draw_dot(self, symbol: str = '', *args):
        'Функция рисования точки(ек) на локальном экране'

        if symbol == '':
            symbol = self.default_symbol

        x, y = self._check_values(*args)

        for i in range(len(x)):
            self.Board[x[i] + y[i] * self.size] = symbol[0]

    def fill(self, symbol: str = '', *args):
        'Функция заливки фигуры. Работает для всех классов, кроме точки и линии'

        if self.__class__ != Dot:
            if symbol == '':
                symbol = self.default_symbol

            x, y = self._check_values(*args)

            symbol2 = self.get_dot(x[0], y[0])

            dots = self._set_fill_dots(x, y)
            self.draw_dot(symbol[0], *dots)

            dots = self._set_dots(x, y)
            self.draw_dot(symbol2, *dots)

    def get_dot(self, x: int = 0, y: int = 0):
        'Функция получения значения в точке'

        return self.Board[x + y * self.size]

    def draw_c(self, symbol: str = ''):
        if symbol == '':
            symbol = self.default_symbol

        dots = []
        for y in range(self.size):
            k = self.Board[y * self.size: (y + 1) * self.size]
            if symbol[0] in k:
                for x in range(len(k)):
                    if k[x] == symbol[0]:
                        dots.append(x)
                        dots.append(y)

        canvas.draw_dot(symbol[0], *dots)

    def print(self):
        'Функция вывода локального экрана в консоль'

        a = list(range(self.size))

        print('    ', end='')
        for i in a:
            print(' ' * (2 - len(str(i))) + str(i), end=' ')
        print('\n')

        for i in range(self.size):
            print(' ' * (2 - len(str(i))) + str(i) + '  ', '  '.join(self.Board[i * self.size: (i + 1) * self.size]))

    def print_c(self, symbol: str = ''):
        'Функция цветного вывода локального экрана в консоль'

        if symbol == '':
            symbol = self.default_symbol

        to_print(self.Board, symbol[0])

    def mirror_h(self):
        'Функция отражения экрана по горизонтали'

        for i in range(self.size):
            a = self.Board[i * self.size: (i + 1) * self.size]
            a = a[::-1]

            self.Board = self.Board[: i * self.size] + a + self.Board[(i + 1) * self.size:]

    def mirror_v(self):
        'Функция отражения экрана по вертикали'

        for i in range(self.size):
            a = self.Board[i::self.size]
            a = a[::-1]

            for j in range(self.size):
                self.Board[i + j * self.size] = a[j]

    def move_to(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0, x: int = 0, y: int = 0, copy: bool = False):
        'Функция перемещения(копирования) области'

        check_input([x1, x2, x], self.size)
        check_input([y1, y2, y], self.size)

        check_input([x + abs(x1 - x2)], self.size)
        check_input([y + abs(y1 - y2)], self.size)

        a = []
        for i in range(min(y1, y2), max(y1, y2) + 1):
            a.append(self.Board[min(x1, x2) + i * self.size: max(x1, x2) + 1 + i * self.size])

            if not copy:
                self.Board = self.Board[: min(x1, x2) + i * self.size] + \
                             [self.default_symbol] * (abs(x1 - x2) + 1) + self.Board[max(x1, x2) + 1 + i * self.size:]

        for i in range(y, y + abs(y1 - y2) + 1):
            self.Board = self.Board[: x + i * self.size] + a[0] + self.Board[x + abs(x1 - x2) + 1 + i * self.size:]
            del a[0]

    @property
    def x(self):
        'Свойство: координата(ы) x'

        return self.__x

    @property
    def y(self):
        'Свойство: координата(ы) y'

        return self.__y

    @property
    def xy(self):
        'Свойство: не используется'

        return True

    @xy.setter
    def xy(self, *args):
        'Свойство: смена точек'

        self.__x, self.__y = self._check_values(*args[0])

    @property
    def square(self):
        'Свойство: площадь фигуры'

        return 0


class Line():
    'Класс линии'

    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0):
        self.size = canvas.size
        self.default_symbol = canvas.default_symbol
        self.Board = [self.default_symbol] * self.size * self.size

        self.__x, self.__y = self._check_values(x1, y1, x2, y2)

    def _check_values(self, *args):
        x = list(args)[::2]
        y = list(args)[1::2]

        if len(x) != len(y):
            raise Error('У точки не хватает аргумента x или y')

        check_input(x, self.size)
        check_input(y, self.size)

        return x, y

    def _get_value_y(self, x: int):
        return ((x - self.__x[0]) * (self.__y[1] - self.__y[0])) / (self.__x[1] - self.__x[0]) + self.__y[0]

    def _get_value_x(self, y: int):
        return ((y - self.__y[0]) * (self.__x[1] - self.__x[0])) / (self.__y[1] - self.__y[0]) + self.__x[0]

    def _set_line_y(self, x: list):
        dots = []

        for i in range(min(x[0], x[1]), max(x[0], x[1]) + 1):
            if 0 <= i <= self.size:
                k = self._get_value_y(i)

                if 0 <= int(k) <= self.size:
                    if int(k) == float(k):
                        dots.append(i)
                        dots.append(int(k))
                    else:
                        a = k - int(k)

                        if a >= 0.4:
                            if 0 <= int(k + 1) <= self.size:
                                dots.append(i)
                                dots.append(int(k + 1))
                        if a <= 0.6:
                            if 0 <= int(k) <= self.size:
                                dots.append(i)
                                dots.append(int(k))

        return dots

    def _set_line_x(self, y: list):
        dots = []

        for i in range(min(y[0], y[1]), max(y[0], y[1]) + 1):
            if 0 <= i <= self.size:
                k = self._get_value_x(i)

                if 0 <= int(k) <= self.size:
                    if int(k) == float(k):
                        dots.append(int(k))
                        dots.append(i)
                    else:
                        a = k - int(k)

                        if a >= 0.4:
                            if 0 <= int(k + 1) <= self.size:
                                dots.append(int(k + 1))
                                dots.append(i)
                        if a <= 0.6:
                            if 0 <= int(k) <= self.size:
                                dots.append(int(k))
                                dots.append(i)

        return dots

    def _set_dots(self):
        dots = []

        if abs(self.__y[0] - self.__y[1]) == abs(self.__x[0] - self.__x[1]):
            k = 0
            for i in range(min(self.__x[0], self.__x[1]), max(self.__x[0], self.__x[1]) + 1):
                dots.append(i)
                if self.__y[0] < self.__y[1]:
                    if self.__x[0] < self.__x[1]:
                        dots.append(self.__y[0] + k)
                    else:
                        dots.append(self.__y[1] - k)
                else:
                    if self.__x[0] < self.__x[1]:
                        dots.append(self.__y[0] - k)
                    else:
                        dots.append(self.__y[1] + k)
                k += 1
            print()
        elif self.__x[0] == self.__x[1]:
            for i in range(min(self.__y[0], self.__y[1]), max(self.__y[0], self.__y[1]) + 1):
                dots.append(self.__x[0])
                dots.append(i)
        elif self.__y[0] == self.__y[1]:
            for i in range(min(self.__x[0], self.__x[1]), max(self.__x[0], self.__x[1]) + 1):
                dots.append(i)
                dots.append(self.__y[0])
        else:
            x = [self.__x[0], self.__x[1]]
            dots.extend(self._set_line_y(x))
            y = [self.__y[0], self.__y[1]]
            dots.extend(self._set_line_x(y))

        return dots

    def draw(self, symbol: str = ''):
        'Функция рисования фигуры на локальном экране. \
                Если нужна обычная функция рисования точек, используйте функцию "draw_dot"'

        if symbol == '':
            symbol = self.default_symbol

        dots = self._set_dots()

        for i in range(1, len(dots), 2):
            self.Board[dots[i - 1] + dots[i] * self.size] = symbol[0]

    def draw_c(self, symbol: str = ''):
        if symbol == '':
            symbol = self.default_symbol

        dots = []
        for y in range(self.size):
            k = self.Board[y * self.size: (y + 1) * self.size]
            if symbol[0] in k:
                for x in range(len(k)):
                    if k[x] == symbol[0]:
                        dots.append(x)
                        dots.append(y)

        canvas.draw_dot(symbol[0], *dots)

    def print(self):
        'Функция вывода локального экрана в консоль'

        a = list(range(self.size))

        print('    ', end='')
        for i in a:
            print(' ' * (2 - len(str(i))) + str(i), end=' ')
        print('\n')

        for i in range(self.size):
            print(' ' * (2 - len(str(i))) + str(i) + '  ', '  '.join(self.Board[i * self.size: (i + 1) * self.size]))

    def print_c(self, symbol: str = ''):
        'Функция цветного вывода локального экрана в консоль'

        if symbol == '':
            symbol = self.default_symbol

        to_print(self.Board, symbol[0])

    def mirror_h(self):
        'Функция отражения экрана по горизонтали'

        for i in range(self.size):
            a = self.Board[i * self.size: (i + 1) * self.size]
            a = a[::-1]

            self.Board = self.Board[: i * self.size] + a + self.Board[(i + 1) * self.size:]

    def mirror_v(self):
        'Функция отражения экрана по вертикали'

        for i in range(self.size):
            a = self.Board[i::self.size]
            a = a[::-1]

            for j in range(self.size):
                self.Board[i + j * self.size] = a[j]

    def move_to(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0, x: int = 0, y: int = 0, copy: bool = False):
        'Функция перемещения(копирования) области'

        check_input([x1, x2, x], self.size)
        check_input([y1, y2, y], self.size)

        check_input([x + abs(x1 - x2)], self.size)
        check_input([y + abs(y1 - y2)], self.size)

        a = []
        for i in range(min(y1, y2), max(y1, y2) + 1):
            a.append(self.Board[min(x1, x2) + i * self.size: max(x1, x2) + 1 + i * self.size])

            if not copy:
                self.Board = self.Board[: min(x1, x2) + i * self.size] + \
                             [self.default_symbol] * (abs(x1 - x2) + 1) + self.Board[max(x1, x2) + 1 + i * self.size:]

        for i in range(y, y + abs(y1 - y2) + 1):
            self.Board = self.Board[: x + i * self.size] + a[0] + self.Board[x + abs(x1 - x2) + 1 + i * self.size:]
            del a[0]

    @property
    def x(self):
        'Свойство: координата(ы) x'

        return self.__x

    @property
    def y(self):
        'Свойство: координата(ы) y'

        return self.__y

    @property
    def xy(self):
        'Свойство: не используется'

        return True

    @xy.setter
    def xy(self, *args):
        'Свойство: смена точек'

        self.__x, self.__y = self._check_values(*args[0])

    @property
    def set_dots(self):
        return self._set_dots()


class Rectangle(Dot):
    'Класс прямоугольника'

    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0):
        self.size = canvas.size
        self.default_symbol = canvas.default_symbol
        self.Board = [self.default_symbol] * self.size * self.size

        self.__x, self.__y = self._check_values(x1, y1, x2, y2)

    def _set_dots(self, x: list, y: list):
        dots = []

        for i in range(min(x[0], x[1]), max(x[0], x[1]) + 1):
            dots.append(i)
            dots.append(y[0])
            dots.append(i)
            dots.append(y[1])
        for i in range(min(y[0], y[1]) + 1, max(y[0], y[1])):
            dots.append(x[0])
            dots.append(i)
            dots.append(x[1])
            dots.append(i)

        return dots

    @property
    def x(self):
        'Свойство: координата(ы) x'

        return self.__x

    @property
    def y(self):
        'Свойство: координата(ы) y'

        return self.__y

    @property
    def xy(self):
        'Свойство: не используется'

        return True

    @xy.setter
    def xy(self, *args):
        'Свойство: смена точек'

        self.__x, self.__y = self._check_values(*args[0])

    @property
    def square(self):
        'Свойство: площадь фигуры'

        s = abs(self.__x[0] - self.__y[1]) * abs(self.__x[1] - self.__y[0])

        return s


class Triangle(Dot):
    'Класс треугольника'

    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0, x3: int = 0, y3: int = 0):
        self.size = canvas.size
        self.default_symbol = canvas.default_symbol
        self.Board = [self.default_symbol] * self.size * self.size

        self.__x, self.__y = self._check_values(x1, y1, x2, y2, x3, y3)

        self.a = ((self.__x[0] - self.__x[1]) ** 2 + (self.__y[0] - self.__y[1]) ** 2) ** 0.5
        self.b = ((self.__x[0] - self.__x[2]) ** 2 + (self.__y[0] - self.__y[2]) ** 2) ** 0.5
        self.c = ((self.__x[1] - self.__x[2]) ** 2 + (self.__y[1] - self.__y[2]) ** 2) ** 0.5

        self._check_triangle()

    def _check_triangle(self):
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise Error('Невозможно построить такой треугольник')

    def _set_dots(self, x: list, y: list):
        dots = []

        l1 = Line(x[0], y[0], x[1], y[1])
        l2 = Line(x[0], y[0], x[2], y[2])
        l3 = Line(x[1], y[1], x[2], y[2])
        l = [l1, l2, l3]

        for i in l:
            dots.extend(i._set_dots())

        return dots

    def _med(self, xb, yb, x1, y1, x2, y2):
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2

        r = []

        if int(x) != x:
            if int(y) != y:
                if x1 < x2 and y1 < y2:
                    if y1 < y2:
                        r.append(Line(xb, yb, int(x + 1), int(y + 1)))
                        r.append(Line(xb, yb, int(x), int(y)))
                    else:
                        r.append(Line(xb, yb, int(x + 1), int(y)))
                        r.append(Line(xb, yb, int(x), int(y + 1)))
                else:
                    r.append(Line(xb, yb, int(x), int(y)))
                    r.append(Line(xb, yb, int(x), int(y + 1)))

            else:
                r.append(Line(xb, yb, int(x + 1), int(y)))
                r.append(Line(xb, yb, int(x), int(y)))
        else:
            if int(y) != y:
                r.append(Line(xb, yb, int(x), int(y + 1)))
                r.append(Line(xb, yb, int(x), int(y)))
            else:
                r.append(Line(xb, yb, int(x), int(y)))

        return r

    @property
    def x(self):
        'Свойство: координата(ы) x'

        return self.__x

    @property
    def y(self):
        'Свойство: координата(ы) y'

        return self.__y

    @property
    def xy(self):
        'Свойство: не используется'

        return True

    @xy.setter
    def xy(self, *args):
        'Свойство: смена точек'

        self.__x, self.__y = self._check_values(*args[0])

    @property
    def square(self):
        'Свойство: площадь фигуры'

        p = (self.a + self.b + self.c) / 2

        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

        return s

    @property
    def med_l(self):
        'Медиана для левой вершины'

        return self._med(self.__x[0], self.__y[0], self.__x[1], self.__y[1], self.__x[2], self.__y[2])

    @property
    def med_m(self):
        'Медиана для средней вершины'

        return self._med(self.__x[1], self.__y[1], self.__x[0], self.__y[0], self.__x[2], self.__y[2])

    @property
    def med_r(self):
        'Медиана для правой вершины'

        return self._med(self.__x[2], self.__y[2], self.__x[0], self.__y[0], self.__x[1], self.__y[1])


class Square(Rectangle):
    'Класс квадрата'

    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0):
        self.size = canvas.size
        self.default_symbol = canvas.default_symbol
        self.Board = [self.default_symbol] * self.size * self.size

        self.__x, self.__y = self._check_values(x1, y1, x2, y2)
        self._set_square()

    def _set_square(self):
        if abs(self.__x[0] - self.__x[1]) != abs(self.__y[0] - self.__y[1]):
            if self.__y[0] < self.__y[1]:
                self.__y[1] = self.__y[0] + abs(self.__x[0] - self.__x[1])
            else:
                self.__y[0] = self.__y[1] + abs(self.__x[0] - self.__x[1])

    @property
    def x(self):
        'Свойство: координата(ы) x'

        return self.__x

    @property
    def y(self):
        'Свойство: координата(ы) y'

        return self.__y

    @property
    def xy(self):
        'Свойство: не используется'

        return True

    @xy.setter
    def xy(self, *args):
        'Свойство: смена точек'

        self.__x, self.__y = self._check_values(*args[0])
        self._set_square()

    @property
    def square(self):
        'Свойство: площадь фигуры'

        s = abs(self.__x[0] - self.__y[1]) ** 2

        return s


class Rhomb(Dot):
    'Класс ромба'

    def __init__(self, x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0,
                 x3: int = -1, y3: int = 0, x4: int = 0, y4: int = 0):
        self.size = canvas.size
        self.default_symbol = canvas.default_symbol
        self.Board = [self.default_symbol] * self.size * self.size

        self.__x, self.__y = self._check_rhomb(x1, y1, x2, y2, x3, y3, x4, y4)

    def _check_rhomb(self, *args):
        x = list(args)[::2]
        y = list(args)[1::2]

        if len(x) != len(y):
            raise Error('У точки не хватает аргумента x или y')

        check_input(x[:2], self.size)
        check_input(y[:2], self.size)

        if x[2] == -1:
            if x[1] + x[1] - x[0] >= self.size or y[0] + y[0] - y[1] >= self.size:
                raise Error('Фигура выходит за пределы поля')
        else:
            check_input(x[2:], self.size)
            check_input(y[2:], self.size)

        return x, y

    def _set_dots(self, x: list, y: list):
        dots = []

        if x[2] == -1:
            d1 = Line(x[0], y[0], x[1] + x[1] - x[0], y[0])
            d2 = Line(x[1], y[1], x[1], y[0] + y[0] - y[1])
            l1 = Line(x[0], y[0], x[1], y[1])
            l2 = Line(x[0], y[0], x[1], y[0] + y[0] - y[1])
            l3 = Line(x[1] + x[1] - x[0], y[0], x[1], y[1])
            l4 = Line(x[1] + x[1] - x[0], y[0], x[1], y[0] + y[0] - y[1])
        else:
            d1 = Line(x[0], y[0], x[2], y[2])
            d2 = Line(x[1], y[1], x[3],y[3])
            l1 = Line(x[0], y[0], x[1], y[1])
            l2 = Line(x[1], y[1], x[2], y[2])
            l3 = Line(x[2], y[2], x[3], y[3])
            l4 = Line(x[0], y[0], x[3], y[3])

        l = [d1, d2, l1, l2, l3, l4]

        for i in l:
            dots.extend(i._set_dots())

        return dots

    @property
    def x(self):
        'Свойство: координата(ы) x'

        return self.__x

    @property
    def y(self):
        'Свойство: координата(ы) y'

        return self.__y

    @property
    def xy(self):
        'Свойство: не используется'

        return True

    @xy.setter
    def xy(self, *args):
        'Свойство: смена точек'

        self.__x, self.__y = self._check_rhomb(*args[0])

    @property
    def square(self):
        'Свойство: площадь фигуры'

        if self.__x[2] == -1:
            s = 2 * (self.__x[1] - self.__x[0]) * (self.__y[0] - self.__y[1])
        else:
            s = 0

        return s


class Circle(Dot):
    'Класс круга'

    def __init__(self, x: int = 0, y: int = 0, r: int = 0):
        self.size = canvas.size
        self.default_symbol = canvas.default_symbol
        self.Board = [self.default_symbol] * self.size * self.size

        self.__x, self.__y, self.__r = self._check_circle(x, y, r)

    def _check_circle(self, *args):
        x, y, r = args

        check_input([x], self.size)
        check_input([y], self.size)
        check_input([r], self.size)

        if x + r >= self.size or x + r < 0 or y + r >= self.size or y - r < 0:
            raise Error('Фигура выходит за пределы поля')

        if r == 0:
            raise Error('Радиус должен быть больше 0')

        return [x], [y], r

    def _get_value_y(self, x: int):
        return (self.__r ** 2 - (x - self.__x[0]) ** 2) ** 0.5

    def _get_value_x(self, y: int):
        return (self.__r ** 2 - (y - self.__y[0]) ** 2) ** 0.5

    def _set_line_y(self, x: list):
        dots = []

        for i in range(min(x[0], x[1]), max(x[0], x[1]) + 1):
            if 0 <= i <= self.size:
                k = self._get_value_y(i) + self.__y[0]

                if 0 <= int(k) <= self.size:
                    if int(k) == float(k):
                        dots.append(i)
                        dots.append(int(k))
                    else:
                        a = k - int(k)

                        if a >= 0.4:
                            if 0 <= int(k + 1) <= self.size:
                                dots.append(i)
                                dots.append(int(k + 1))
                        if a <= 0.6:
                            if 0 <= int(k) <= self.size:
                                dots.append(i)
                                dots.append(int(k))

        for i in range(min(x[0], x[1]), max(x[0], x[1]) + 1):
            if 0 <= i <= self.size:
                k = -self._get_value_y(i) + self.__y[0]

                if 0 <= int(k) <= self.size:
                    if int(k) == float(k):
                        dots.append(i)
                        dots.append(int(k))
                    else:
                        a = k - int(k)

                        if a >= 0.4:
                            if 0 <= int(k + 1) <= self.size:
                                dots.append(i)
                                dots.append(int(k + 1))
                        if a <= 0.6:
                            if 0 <= int(k) <= self.size:
                                dots.append(i)
                                dots.append(int(k))

        return dots

    def _set_line_x(self, y: list):
        dots = []

        for i in range(min(y[0], y[1]), max(y[0], y[1]) + 1):
            if 0 <= i <= self.size:
                k = self._get_value_x(i) + self.__x[0]

                if 0 <= int(k) <= self.size:
                    if int(k) == float(k):
                        dots.append(int(k))
                        dots.append(i)
                    else:
                        a = k - int(k)

                        if a >= 0.4:
                            if 0 <= int(k + 1) <= self.size:
                                dots.append(int(k + 1))
                                dots.append(i)
                        if a <= 0.6:
                            if 0 <= int(k) <= self.size:
                                dots.append(int(k))
                                dots.append(i)

        for i in range(min(y[0], y[1]), max(y[0], y[1]) + 1):
            if 0 <= i <= self.size:
                k = -self._get_value_x(i) + self.__x[0]

                if 0 <= int(k) <= self.size:
                    if int(k) == float(k):
                        dots.append(int(k))
                        dots.append(i)
                    else:
                        a = k - int(k)

                        if a >= 0.4:
                            if 0 <= int(k + 1) <= self.size:
                                dots.append(int(k + 1))
                                dots.append(i)
                        if a <= 0.6:
                            if 0 <= int(k) <= self.size:
                                dots.append(int(k))
                                dots.append(i)

        return dots

    def _set_dots(self, x: list, y: list):
        dots = []

        x = [x[0] - self.__r, x[0] + self.__r]
        dots.extend(self._set_line_y(x))
        y = [y[0] - self.__r, y[0] + self.__r]
        dots.extend(self._set_line_x(y))

        return dots

    def fill(self, symbol: str = '', *args):
        if symbol == '':
            symbol = self.default_symbol

        x, y = self._check_values(*args)

        symbol2 = self.get_dot(x[0] - self.__r, y[0])

        dots = self._set_fill_dots(x, y)
        self.draw_dot(symbol[0], *dots)

        dots = self._set_dots(x, y)
        self.draw_dot(symbol2, *dots)

    def cut_piece(self, symbol: str = '', x1: int = 0, y1: int = 0, x2: int = 0, y2: int = 0):
        'Функция вырезания сектора круга'

        if symbol == '':
            symbol = self.default_symbol

        t = Triangle(x1, y1, x2, y2, self.__x[0], self.__y[0])

        dots = t._set_dots(t.x, t.y)
        dots.extend(t._set_fill_dots(t.x, t.y))

        self.draw_dot(symbol[0], *dots)

    @property
    def x(self):
        'Свойство: координата(ы) x'

        return self.__x

    @property
    def y(self):
        'Свойство: координата(ы) y'

        return self.__y

    @property
    def r(self):
        'Свойство: радиус'

        return self.__r

    @property
    def xyr(self):
        'Свойство: не используется'

        return True

    @xyr.setter
    def xyr(self, *args):
        'Свойство: смена точек'

        self.__x, self.__y, self.__r = self._check_circle(*args[0])

    @property
    def square(self):
        'Свойство: площадь фигуры'

        s = pi * self.__r ** 2

        return s


sy = '.'  # Стандартный символ
si = 40  # Размер поля
canvas = Canvas(sy, si)

default_font_color = 0  # Цвет текста для таблицы
default_background_color = 0  # Цвет фона текста для таблицы
font_color = 31  # Цвет текста для фигуры
background_color = 1  # Цвет фона текста для фигуры
# 1120 строк ＼(〇_ｏ)／

'''
Цвет        Текст   Фон
Чёрный	    30      40
Красный	    31	    41
Зелёный	    32	    42
Жёлтый	    33	    43
Синий	    34	    44
Фиолетовый	35	    45
Бирюзовый	36	    46
Белый	    37	    47

Команда     Описание
0           Сброс
1           Жирный
3           Курсив
4           Подчеркивание
7           Цвет фона = цвет текста
'''

canvas = Canvas(' ', 400)
t = Triangle(0, 100, 200, 30, 300, 80)
t.draw('*')
t.draw_c('*')
canvas.print()
input()

# canvas = Canvas(sy, si)
# canvas.draw_dot('*', 0, 1, 2, 3)
# canvas.print()


# canvas = Canvas(sy, si)
# canvas.fill()
# canvas.print()


# canvas = Canvas(sy, si)
# canvas.draw_dot('*', 0, 1, 2, 3)
#
# canvas.mirror_v()
# canvas.print()


# canvas = Canvas(sy, si)
# canvas.draw_dot('*', 0, 1, 2, 3)
#
# canvas.mirror_h()
# canvas.print()


# canvas = Canvas(sy, si)
# canvas.draw_dot('*', 0, 0, 0, 1, 0, 2, 1, 0, 1, 1, 1, 2, 2, 0, 2, 1, 2, 2)
# canvas.print()
#
# canvas.move_to(0, 0, 1, 2, 6, 0, copy=True)
# canvas.print()
#
# canvas.move_to(0, 0, 1, 2, 0, 6)
# canvas.print()


# canvas = Canvas(sy, si)
# canvas.draw_dot('*', 0, 0, 0, 1, 0, 2, 1, 0, 1, 1, 1, 2, 2, 0, 2, 1, 2, 2)
# canvas.print_c()


# a = Dot(39, 0)
# a.draw('*')
#
# a.print()


# a = Dot(39, 0)
# a.draw('*')
#
# a.draw()
#
# a.xy = 1, 1
# a.draw('*')
#
# a.print()


# canvas = Canvas(sy, si)
#
# b = Rectangle(5, 5, 10, 10)
# b.draw('*')
# b.print()
#
# b.draw()
#
# b.xy = 0, 0, 5, 5
# b.fill('*')
#
# b.print()
#
# canvas.print()


# l = Line(0, 0, 20, 5)
# l.draw('*')
#
# l.print()


# d = Triangle(0, 0, 5, 5, 10, 0)
# d.draw('*')
#
# d.print()


# d = Triangle(0, 0, 5, 5, 10, 0)
# d.draw('*')
# d.fill('1')
#
# d.print()


# d = Triangle(0, 0, 5, 2, 20, 0)
# d.draw('*')
#
# d.print()


# d = Triangle(0, 10, 20, 3, 30, 8)
# d.draw('*')
#
# d.print()


# t = Triangle(5, 5, 10, 0, 15, 5)
# t.draw('*')
#
# l = t.med_l
#
# for i in l:
#     t.draw_dot('1', *i.set_dots)
#
# t.print()


# t = Triangle(5, 5, 10, 0, 15, 5)
# t.draw('*')
#
# l = t.med_m
#
# for i in l:
#     t.draw_dot('2', *i.set_dots)
#
# t.print()


# t = Triangle(5, 5, 10, 0, 15, 5)
# t.draw('*')
#
# l = t.med_r
#
# for i in l:
#     t.draw_dot('3', *i.set_dots)
#
# t.print()


# c = Square(3, 4, 0, 0)
# c.draw('*')
#
# c.print()


# r = Rhomb(10, 10, 20, 5)
# r.draw('*')
#
# r.print()


# r = Rhomb(10, 10, 20, 5)
# r.draw('*')
# r.fill('1')
#
# r.print()


# r = Rhomb(5, 5, 12, 3, 20, 4, 15, 30)
# r.draw('*')
#
# r.print()


# canvas = Canvas(sy, si)
#
# a = Dot(3, 3)
# b = Rectangle(5, 5, 10, 3)
# c = Triangle(20, 20, 25, 15, 30, 35)
# d = Line(10, 20, 30, 39)
# e = Square(0, 0, 2, 2)
# l = [a, b, c, d, e]
#
# S = 0
#
# for i in l:
#     i.draw('*')
#     i.draw_c('*')
#
#     s = 0
#     if isinstance(i, Dot):
#         s = i.square
#
#     S += s
#     print(i.__class__.__name__, s)
#
# print('\nAll {0}\n'.format(S))
#
# canvas.print()


# a = 0.0
# for i in range(10):
#     a += 0.1
#     print(a)


# a = Dot(1, 1)
# print(a.x, a.y)
#
# try:
#     a.x = 0
#     a.y = 0
# except:
#     print('Переменные недоступны для изменения')


# c = Circle(10, 10, 3)
# c.draw('*')
#
# c.print()


# c = Circle(10, 10, 3)
# c.draw('*')
# c.fill('+')
#
# c.print()


# c = Circle(10, 10, 3)
#
# c.draw('*')
# c.fill('+')
#
# c.cut_piece(c.default_symbol, 10, 0, 39, 10)
#
# c.print()


# c = Circle(10, 10, 3)
# c.draw('*')
# c.fill('+')
#
# c.cut_piece(c.default_symbol, 10, 0, 39, 39)
#
# c.print()


# c = Circle(10, 10, 3)
# c.draw('*')
# c.fill('+')
#
# c.cut_piece(c.default_symbol, 10, 0, 39, 10)
# c.cut_piece(c.default_symbol, 39, 10, 10, 39)
# c.cut_piece(c.default_symbol, 0, 10, 10, 39)
#
# c.print()


# canvas = Canvas(sy, si)
# c = Circle(10, 10, 3)
#
# c.draw('*')
# c.fill('+')
# c.cut_piece(c.default_symbol, 10, 0, 39, 39)
#
# c.print()
#
# c.draw_c('*')
# canvas.print()


# canvas = Canvas(sy, si)
# c = Circle(10, 10, 3)
#
# c.draw('*')
# c.fill('+')
# c.cut_piece(c.default_symbol, 10, 0, 39, 39)
#
# c.print()
#
# c.draw_c('*')
# c.draw_c('+')
# canvas.print()


# canvas = Canvas('-', 10)
# a = Rectangle(3, 3, 5, 5)
# a.draw('+')
# a.print()
#
# try:
#     b = Rectangle(20, 20, 30, 30)
# except Exception as e:
#     print('\nФигура находится вне поля')
#     print(e)

# а тут 1420 строк (◕‿◕)
