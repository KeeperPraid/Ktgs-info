# Вычисление алгоритма 1
# a, s, p = 1, 150, 200
# while a <= 10:
#     a += 2
#     p += a
#     s += p
# print (s)
# a, s, p = 1, 150, 200
# while True:
#     if a > 10:
#         break
#     a += 2
#     p += a
#     s += p
# print (s)
# Вычисление алгоритма 2
# s = 1
# for n in range (1,6):
#     s *= n
# print (s)

# Вычисление алгоритма 3
# m, n = 12, 5
# while m != n:
#     if m > n:
#         m = m - 2*n
#     else:
#         n = n - 3
# print (m, n)

# m, n = 12, 5
# while True:
#     if m == n:
#         break
#     if m > n:
#         m = m - 2*n
#     else:
#         n = n -3
# print (m, n)

# Вычисление алгоритма 4

# k, l= list(range(1, 11)), list(range(1, 11))
# for i in range(1, 11):
#     k[i-1] = 10 - i
# for i in range(1, 11):
#     l[i-1] = k[6] - k[i-1]
# print (k)
# print (l)
# neg_list = [n<0 for n in l]
# print(neg_list.count(True))