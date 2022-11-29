from pi2143oop import Canvas, Dot, Rectangle

a = Canvas(' ', 10)
a.fill('+')

b = [
    Dot(a),
    Rectangle(a, 2, 0, 4, 3),
    Dot(a, 1, 2),
    Dot(a, 1, 3),
    Rectangle(a, 5, 0, 9, 0),
    Rectangle(a, 6, 1, 8, 1),
    Dot(a, 6, 3),
    Dot(a, 8, 3),
    Rectangle(a, 0, 5, 0, 8),
    Rectangle(a, 3, 7, 4, 8),
    Dot(a, 2, 7),
    Rectangle(a, 7, 5, 9, 5),
    Rectangle(a, 9, 6, 9, 8),
    Rectangle(a, 6, 7, 7, 7),
    Rectangle(a, 7, 8, 8, 8),
]

for i in b:
    i.draw_c(' ')
    # if i.__class__ != Dot:
    #     i.fill_c(' ')

b[1].fill_c(' ')

a.print()
