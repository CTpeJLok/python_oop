from pi2143oop import Canvas, Dot, Rectangle

a = Canvas(' ', 10)
a.fill('+')

b = [
    Rectangle(a, 3, 0, 5, 0),
    Dot(a, 1, 1),
    Dot(a, 8, 1),
    Dot(a, 0, 3),
    Dot(a, 3, 3),
    Dot(a, 6, 3),
    Dot(a, 9, 3),
    Dot(a, 4, 5),
    Dot(a, 3, 6),
    Dot(a, 5, 6),
    Rectangle(a, 1, 6, 2, 7),
    Rectangle(a, 6, 6, 8, 7),
    Rectangle(a, 2, 8, 7, 8),
    Dot(a, 0, 9),
    Dot(a, 9, 9),
]

for i in b:
    i.draw_c(' ')

a.print()
