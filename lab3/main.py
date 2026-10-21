# l = input().split()

# v = [w for w in l if w[0] in ['a', 'e', 'i', 'o', 'u']]

# print(v)

# l = input()

# k = int(input())
# v = [chr(ord(l[i]) - k) if l[i] != ' ' else ' ' for i in range(0, len(l))]

# print(v)

# l = input()

# v = "".join([l[i] + 'p' + l[i].lower() if l[i].lower() in ['a', 'e', 'i', 'o', 'u'] else l[i] for i in range(0, len(l))])

# print(v)

# assert(v == "Apanapa aparepe meperepe")

# s = "".join([chr(i + ord('a')) for i in range(0, 26)])

# print(s)

# 3

# t = input()
# s = input()

# f = s.find(t)
# if f != -1:
#     while f != -1:
#         print(f)
#         f = s.find(t, f + len(t))
# else:
#     print("nu exista")


# t = input()
# s = input()

# try:
#     f = s.index(t)

#     try:
#         while True:
#             print(f)
#             f = s.index(t, f + len(t))
#     except:
#         pass
# except:
#     print("nu exista")

# 4

# s = "re"
# t = "ger"
# prop = "Problemele cu șiruri de caracteger nu sunt ggerle!"
# k = 1

# prop = prop.replace(t, s, k)
# print(prop)

# if prop.find(t) != -1:
#     print(f"textul contine prea multe greseli, doar {k} au fost corectate")

# 5

# s = "ce"
# t = "be"

# prop = "ce, ce; be, a ads gf"

# # l = [w if w != s else t for w in prop.split()]
# l = []

# for w in prop.split():
#     x = len(w) - 1
#     while not w[x].isalpha():
#         x = x - 1

#     if w[:x + 1] != s:
#         l.append(w)
#     else:
#         l.append(t + w[x + 1:])

# print(l)

# 6

# s = "O zi frumoasa!"
# k = 9
# x = ""

# for c in s:
#     if c.isalpha():
#         t = ord('a') if c.islower() else ord('A')
#         x = x + chr(((ord(c) - t + k) % 26) + t)
#     else:
#         x = x + c

# print(x)

# s = "X ir oadvxjbj!"
# k = 9
# x = ""

# for c in s:
#     if c.isalpha():
#         t = ord('a') if c.islower() else ord('A')
#         x = x + chr(((26 + ord(c) - t - k) % 26) + t)
#     else:
#         x = x + c
    
# print(x)

# 7

# print(num)

# l = input()

# s = "".join([l[i] + 'p' + l[i].lower() if l[i].lower() in ['a', 'e', 'i', 'o', 'u'] else l[i] for i in range(0, len(l))])

# print(s)

# s = "Apanapa aparepe meperepe"
# x = ""
# i = 0

# while i < len(s) - 2:
#     x = x + s[i]
#     if s[i].lower() == s[i + 2].lower() and s[i + 1] == 'p':
#         i = i + 3
#     else:
#         i = i + 1

# print(x)

# 8

# s = "Astăzi am cumpărat pâine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumpărat niște cașcaval. De asemenea, mi-am cumpărat și niște papuci cu 50 RON!"
# num = 0

# for w in s.split():
#     try:
#         num = num + int(w)
#     except:
#         pass