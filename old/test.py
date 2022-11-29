import figures
print(dir(figures.Canvas))


# x = [3, 4]
# y = [1, 2]
# k = list(zip(x, y))
# print(k)

# from scipy import stats as st
#
# a = 100500
# sigma = 3500
#
# bonus_threshold = 111000
# penalty_threshold = 92000
#
# p_bonus = 1 - st.norm(a, sigma).cdf(bonus_threshold)
# p_penalty = st.norm(a, sigma).cdf(penalty_threshold)
# print('Вероятность бонуса:', p_bonus)
# print('Вероятность штрафа:', p_penalty)
#
# a = 420
# sigma = 65
# prob = 0.9
# n_shipment = st.norm(a, sigma).ppf(1 - prob)
# print('Нужно заказать единиц товара:', int(n_shipment))
#
# a = 2400
# sigma = 320
# threshold = 0.75
# max_delivery_price = st.norm(a, sigma).ppf(1 - threshold) / 2
# print('Максимальная стоимость доставки курьером:', max_delivery_price)


# k = []
#
# a = int(input())
# b = int(input())
# m = ''
# for i in range(a):
#     c = input().split(';')
#
#     for i in range(len(c)):
#         x = c[i].split()
#         s = ''
#         for j in x:
#             s += j + ' '
#         c[i] = s[:-1]
#
#     if c[0] == '':
#         c = [m, c[1], c[2]]
#     else:
#         m = c[0]
#
#     k.append('INSERT INTO `Tuning` (`Tuning_ID`, `Transport_ID`, `Tuning_type_ID`, `Name`, `Cost`) VALUES (NULL, (SELECT Transport_ID FROM Transport WHERE Name="{0}"), {1}, "{2}", {3});'.format(c[0], b, c[1], c[2]))
#
# for i in k:
#     print(i)


# k = []
#
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     c = input().split()
#     k.append("INSERT INTO `Transport_price` (`Transport_ID`, `USD`, `EUR`, `RUB`, `Salon_price`, `Used_price`, `Sale_price`) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6});".format(i, c[0], c[1], c[2], c[3], c[4], c[5]))
#
# for i in k:
#     print(i)


# k = []
# a = int(input())
# b = int(input())
# for i in range(a):
#     k.append("INSERT INTO `Transport` (`Transport_ID`, `Type`, `Dealer`, `Engine_type`, `Name`) VALUES (NULL, '5', '{0}', '2', '{1}');".format(b, input()))
#
# for i in k:
#     print(i)
