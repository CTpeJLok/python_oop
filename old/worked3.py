class Canvas():
    def __init__(self):
        self.Board = ['-'] * 40 * 40

    def draw_dot(self, *args):
        x = list(args)[::2]
        y = list(args)[1::2]
        for i in range(len(x)):
            self.Board[x[i] + y[i] * 40] = '*'

    def clear_dot(self, *args):
        x = list(args)[::2]
        y = list(args)[1::2]
        for i in range(len(x)):
            self.Board[x[i] + y[i] * 40] = '-'

    def clear(self):
        self.Board = ['-'] * 40 * 40

    def print(self):
        for i in range(40):
            print(*self.Board[i * 40: (i + 1) * 40])


class Dot():
    def __init__(self, *args):
        x, y = 0, 0

        if len(args) == 2:
            x, y = map(int, args[:2])

        self.x = [x]
        self.y = [y]
        self.Board = ['-'] * 40 * 40

    def draw_figure(self, *args):
        x = self.x
        y = self.y

        if len(args) != 0:
            x = list(args)[::2]
            y = list(args)[1::2]

        for i in range(len(x)):
            self.Board[x[i] + y[i] * 40] = '*'

    def clear_figure(self, *args):
        x = self.x
        y = self.y

        if len(args) != 0:
            x = list(args)[::2]
            y = list(args)[1::2]

        for i in range(len(x)):
            self.Board[x[i] + y[i] * 40] = '-'

    def draw(self):
        canvas.draw_dot(self.x, self.y)

    def clear(self):
        canvas.clear_dot(self.x, self.y)

    def change(self, *args):
        self.x = list(args)[::2]
        self.y = list(args)[1::2]

    def print(self):
        for i in range(40):
            print(*self.Board[i * 40: (i + 1) * 40])


class Rectangle(Dot):
    def __init__(self, *args):
        x1, y1, x2, y2 = map(int, args[:4])

        if x1 < x2:
            self.x = [x1, x2]
            self.y = [y1, y2]
        else:
            self.x = [x2, x1]
            self.y = [y2, y1]

        self.Board = ['-'] * 40 * 40

    def draw_figure(self):
        for i in range(self.x[0], self.x[1] + 1):
            super().draw_figure(i, self.y[0])
            super().draw_figure(i, self.y[1])
        for i in range(self.y[0] + 1, self.y[1]):
            super().draw_figure(self.x[0], i)
            super().draw_figure(self.x[1], i)

    def clear_figure(self):
        for i in range(self.x[0], self.x[1] + 1):
            super().clear_figure(i, self.y[0])
            super().clear_figure(i, self.y[1])
        for i in range(self.y[0] + 1, self.y[1]):
            super().clear_figure(self.x[0], i)
            super().clear_figure(self.x[1], i)

    def fill_figure(self):
        for i in range(self.x[0] + 1, self.x[1]):
            for j in range(self.y[0] + 1, self.y[1]):
                super().draw_figure(i, j)

    def empty_figure(self):
        for i in range(self.x[0] + 1, self.x[1]):
            for j in range(self.y[0] + 1, self.y[1]):
                super().clear_figure(i, j)

    def draw(self):
        for i in range(self.x1, self.x2 + 1):
            canvas.draw_dot(i, self.y1)
            canvas.draw_dot(i, self.y2)
        for i in range(self.y1, self.y2 + 1):
            canvas.draw_dot(self.x1, i)
            canvas.draw_dot(self.x2, i)

    def clear(self):
        for i in range(self.x1, self.x2 + 1):
            canvas.clear_dot(i, self.y1)
            canvas.clear_dot(i, self.y2)
        for i in range(self.y1, self.y2 + 1):
            canvas.clear_dot(self.x1, i)
            canvas.clear_dot(self.x2, i)

    def fill(self):
        for i in range(self.x1 + 1, self.x2):
            for j in range(self.y1 + 1, self.y2):
                canvas.draw_dot(i, j)

    def empty(self):
        for i in range(self.x1 + 1, self.x2):
            for j in range(self.y1 + 1, self.y2):
                canvas.clear_dot(i, j)

    def change(self, x1, y1, x2, y2):
        if x1 < x2:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        else:
            self.x1 = x2
            self.y1 = y2
            self.x2 = x1
            self.y2 = y1


canvas = Canvas()

# a = Dot(0, 0)
# a.draw()
# a.clear()
# a.change(1, 1)
# a.draw()
# a.print()

# b = Rectangle(0, 0, 5, 5)
# b.draw_figure()
# b.print()
# b.clear_figure()
# print()
# b.print()
# b.fill()

b = Rectangle(0, 0, 5, 5)
b.fill_figure()
b.print()
print()
b.draw_figure()
b.empty_figure()
b.print()

print()
canvas.print()


# canvas = Canvas()
# canvas.draw_dot(0, 1, 2, 3)
# canvas.print()
#
# print()
#
# a = Dot(1, 1)
# a.draw_figure()
# a.print()
#
# print()
#
# a.draw_figure(2, 2)
# a.print()



