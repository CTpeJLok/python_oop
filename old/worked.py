class Figure():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Board = ['-'] * 40 * 40

    def draw(self, x, y):
        self.Board[x + y * 40] = '*'

    def clear(self):
        self.Board = ['-'] * 40 * 40

    def print_figure(self):
        for i in range(40):
            print(*self.Board[i * 40: (i + 1) * 40])


class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.Board = ['-'] * 40 * 40

    def draw_line(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        x = x2 - x1
        y = abs(y1 - y2)

        c = (y + 1) / 2
        if c != int(c):
            c = int(c + 1)

        if x > y:
            k = (x + 1) / (y + 1)
            l = 0

            if k == int(k):
                l = int(k)
            else:
                l = int(k + 1)

            t = 0
            tt = 0
            p = 0
            d = 0
            for j in range(x1, x2):
                if t == l:
                    tt += 1
                    t = 0
                    p += 1
                    if p == c:
                        p = 0
                        d = j
                        break
                    if k != int(k):
                        if k < int(k) + 0.5:
                            t += 1
                    if y1 < y2:
                        super().draw(j - 1, y1 + tt)
                    else:
                        super().draw(j - 1, y1 - tt)

                if y1 < y2:
                    super().draw(j, y1 + tt)
                else:
                    super().draw(j, y1 - tt)
                t += 1
            t = 0
            tt = 0
            p = 0
            for j in range(x2, x1, -1):
                if t == l:
                    tt += 1
                    t = 0
                    p += 1
                    if p == c:
                        p = 0
                        if j != d:
                            for i in range(d, j + 1):
                                if y1 < y2:
                                    super().draw(i, y1 + tt - 1)
                                    super().draw(i, y2 - tt + 1)
                                else:
                                    super().draw(i, y1 - tt)
                                    super().draw(i, y2 + tt)
                        break
                    if k != int(k):
                        if k < int(k) + 0.5:
                            t += 1
                    if y1 < y2:
                        super().draw(j + 1, y2 - tt)
                    else:
                        super().draw(j + 1, y2 + tt)

                if y1 < y2:
                    super().draw(j, y2 - tt)
                else:
                    super().draw(j, y2 + tt)
                t += 1
        else:
            pass

    def draw(self):
        if abs(self.y1 - self.y2) == abs(self.x1 - self.x2):
            k = 0
            for i in range(self.x1, self.x2 + 1):
                super().draw(i, self.y1 + k)
                if self.y1 > self.y2:
                    k -= 1
                else:
                    k += 1
        elif self.x1 == self.x2:
            for i in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                super().draw(self.x1, i)
        elif self.y1 == self.y2:
            for i in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                super().draw(i, self.y1)
        else:
            # Line.draw_line(self, self.x1, self.y1, self.x2, self.y2)
            self.draw_line(self.x1, self.y1, self.x2, self.y2)

        # if abs(self.y1 - self.y3) == abs(self.x1 - self.x3):
        #     k = 0
        #     for i in range(self.x1, self.x3 + 1):
        #         super().draw(i, self.y1 + k)
        #         if self.y1 > self.y3:
        #             k -= 1
        #         else:
        #             k += 1
        # elif self.x1 == self.x3:
        #     for i in range(min(self.y1, self.y3), max(self.y1, self.y3) + 1):
        #         super().draw(self.x1, i)
        # elif self.y1 == self.y3:
        #     for i in range(min(self.x1, self.x3), max(self.x1, self.x3) + 1):
        #         super().draw(i, self.y1)
        # else:
        #     # Line.draw_line(self, self.x1, self.y1, self.x3, self.y3)
        #     self.draw_line(self.x1, self.y1, self.x3, self.y3)
        #
        # if abs(self.y2 - self.y3) == abs(self.x2 - self.x3):
        #     k = 0
        #     for i in range(self.x2, self.x3 + 1):
        #         super().draw(i, self.y2 + k)
        #         if self.y2 > self.y3:
        #             k -= 1
        #         else:
        #             k += 1
        # elif self.x2 == self.x3:
        #     for i in range(min(self.y2, self.y3), max(self.y2, self.y3) + 1):
        #         super().draw(self.x2, i)
        # elif self.y2 == self.y3:
        #     for i in range(min(self.x2, self.x3), max(self.x2, self.x3) + 1):
        #         super().draw(i, self.y2)
        # else:
        #     # Line.draw_line(self, self.x1, self.y1, self.x3, self.y3)
        #     self.draw_line(self.x2, self.y2, self.x3, self.y3)


        # if abs(self.y1 - self.y3) == abs(self.x1 - self.x3):
        #     k = 0
        #     for i in range(self.x1, self.x3 + 1):
        #         super().draw(i, self.y1 + k)
        #         if self.y1 > self.y3:
        #             k -= 1
        #         else:
        #             k += 1
        # elif self.x1 == self.x3:
        #     for i in range(min(self.y1, self.y3), max(self.y1, self.y3) + 1):
        #         super().draw(self.x1, i)
        # elif self.y1 == self.y3:
        #     for i in range(min(self.x1, self.x3), max(self.x1, self.x3) + 1):
        #         super().draw(i, self.y1)
        # # else:
        # #     self.draw_line(self.x1, self.y1, self.x3, self.y3)
        #
        # if abs(self.y2 - self.y3) == abs(self.x2 - self.x3):
        #     k = 0
        #     for i in range(self.x2, self.x3 + 1):
        #         super().draw(i, self.y2 + k)
        #         if self.y2 > self.y3:
        #             k -= 1
        #         else:
        #             k += 1
        # elif self.x2 == self.x3:
        #     for i in range(min(self.y2, self.y3), max(self.y2, self.y3) + 1):
        #         super().draw(self.x2, i)
        # elif self.y2 == self.y3:
        #     for i in range(min(self.x2, self.x3), max(self.x2, self.x3) + 1):
        #         super().draw(i, self.y2)
        # # else:
        # #     self.draw_line(self.x2, self.y2, self.x3, self.y3)


# a = Triangle(0, 0, 5, 2, 0, 0)
a = Triangle(0, 5, 2, 0, 5, 3)
# a = Triangle(0, 0, 2, 5, 7, 1)
# a = Triangle(0, 1, 7, 3, 10, 2)
# a = Triangle(7, 0, 0, 1, 10, 2)
# a = Triangle(0, 5, 5, 0, 5, 5)
# a = Triangle(0, 0, 0, 0, 0, 0)
# a = Triangle(0, 0, 3, 2, 0, 0)

a.draw()
a.print_figure()
